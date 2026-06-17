import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Student')

table.put_item(
 Item={
  'StudentID':'STU001',
  'Name':'Atul Kamble',
  'City':'Pune'
 }
)

print("Student Added Successfully")
