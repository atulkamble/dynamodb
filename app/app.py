import os
from decimal import Decimal
from pathlib import Path
import boto3
from botocore.exceptions import ClientError, BotoCoreError, NoCredentialsError, PartialCredentialsError
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)
REGION = os.getenv('AWS_REGION', os.getenv('AWS_DEFAULT_REGION', 'us-east-1'))
TABLE = os.getenv('DYNAMODB_TABLE', 'Employees')
dynamodb = boto3.resource('dynamodb', region_name=REGION)
client = boto3.client('dynamodb', region_name=REGION)

def json_item(item):
    return {k: float(v) if isinstance(v, Decimal) else v for k, v in item.items()}

@app.errorhandler(ClientError)
def aws_error(error):
    return jsonify(error=error.response['Error'].get('Message', str(error))), 400

@app.errorhandler(BotoCoreError)
def sdk_error(error):
    return jsonify(error=f'AWS SDK connection/credentials error: {error}'), 503

@app.get('/api/connection')
def connection():
    identity = boto3.client('sts', region_name=REGION).get_caller_identity()
    return jsonify(account=identity['Account'], arn=identity['Arn'], region=REGION, table=TABLE, backend='AWS DynamoDB')

@app.get('/')
def home():
    return send_from_directory(Path(__file__).parent, 'index.html')

@app.get('/api/status')
def status():
    try:
        desc = client.describe_table(TableName=TABLE)['Table']
        return jsonify(exists=True, status=desc['TableStatus'], region=REGION, table=TABLE)
    except client.exceptions.ResourceNotFoundException:
        return jsonify(exists=False, region=REGION, table=TABLE)

@app.post('/api/table')
def create_table():
    client.create_table(TableName=TABLE, AttributeDefinitions=[{'AttributeName':'EmployeeID','AttributeType':'S'}], KeySchema=[{'AttributeName':'EmployeeID','KeyType':'HASH'}], BillingMode='PAY_PER_REQUEST')
    client.get_waiter('table_exists').wait(TableName=TABLE)
    return jsonify(message='AWS table created', table=TABLE), 201

@app.delete('/api/table')
def delete_table():
    client.delete_table(TableName=TABLE)
    return jsonify(message='AWS table deletion started')

@app.get('/api/employees')
def list_employees():
    table = dynamodb.Table(TABLE)
    items = []
    response = table.scan()
    items.extend(response.get('Items', []))
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response.get('Items', []))
    return jsonify(items=[json_item(x) for x in items])

@app.get('/api/employees/<employee_id>')
def get_employee(employee_id):
    response = dynamodb.Table(TABLE).get_item(Key={'EmployeeID': employee_id})
    if 'Item' not in response:
        return jsonify(error='Employee not found'), 404
    return jsonify(item=json_item(response['Item']))

@app.put('/api/employees/<employee_id>')
def put_employee(employee_id):
    data = request.get_json(silent=True) or {}
    name = str(data.get('Name', '')).strip()
    dept = str(data.get('Department', '')).strip()
    try:
        salary = Decimal(str(data['Salary']))
        if not salary.is_finite() or salary < 0:
            raise ValueError()
    except (ValueError, KeyError, TypeError):
        return jsonify(error='Salary must be a nonnegative number'), 400
    if not name or not dept:
        return jsonify(error='Name and Department are required'), 400
    item = {'EmployeeID': employee_id, 'Name': name, 'Department': dept, 'Salary': salary}
    table = dynamodb.Table(TABLE)
    table.put_item(Item=item)
    verified = table.get_item(Key={'EmployeeID': employee_id}, ConsistentRead=True).get('Item')
    if verified != item:
        return jsonify(error='Write was submitted but AWS read-back verification failed'), 502
    return jsonify(item=json_item(verified), verified_in_aws=True, region=REGION, table=TABLE)

@app.patch('/api/employees/<employee_id>/salary')
def update_salary(employee_id):
    data = request.get_json(silent=True) or {}
    try:
        salary = Decimal(str(data['Salary']))
        if not salary.is_finite() or salary < 0:
            raise ValueError()
    except (ValueError, KeyError, TypeError):
        return jsonify(error='Salary must be a nonnegative number'), 400
    try:
        response = dynamodb.Table(TABLE).update_item(Key={'EmployeeID': employee_id}, UpdateExpression='SET Salary = :s', ConditionExpression='attribute_exists(EmployeeID)', ExpressionAttributeValues={':s': salary}, ReturnValues='ALL_NEW')
    except client.exceptions.ConditionalCheckFailedException:
        return jsonify(error='Employee not found'), 404
    verified = dynamodb.Table(TABLE).get_item(Key={'EmployeeID': employee_id}, ConsistentRead=True).get('Item')
    if not verified or verified['Salary'] != salary:
        return jsonify(error='Update read-back verification failed'), 502
    return jsonify(item=json_item(verified), verified_in_aws=True)

@app.delete('/api/employees/<employee_id>')
def delete_employee(employee_id):
    table = dynamodb.Table(TABLE)
    table.delete_item(Key={'EmployeeID': employee_id})
    if 'Item' in table.get_item(Key={'EmployeeID': employee_id}, ConsistentRead=True):
        return jsonify(error='Delete read-back verification failed'), 502
    return jsonify(message='Deleted and verified in AWS', employee_id=employee_id, verified_in_aws=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.getenv('PORT', '5000')), debug=False)
