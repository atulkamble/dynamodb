# AWS DynamoDB 

Topics: Introduction • Table Creation • Inserting Items • AWS CLI Practice

## 1. Introduction to AWS DynamoDB

Amazon DynamoDB is a fully managed, serverless NoSQL database service provided by AWS. It stores data as key-value pairs and documents, with low-latency access at scale.

### Key points to remember

- Fully managed NoSQL database.
- No database server installation required.
- Stores data in tables, items and attributes.
- Uses primary keys to identify items.
- Automatically scales to handle workloads.
- Supports on-demand and provisioned capacity modes.
- Supports backup, encryption and point-in-time recovery.
- Integrates with AWS Lambda, API Gateway and IAM.

## 2. DynamoDB Architecture

Flow: Client → API Gateway → Lambda → DynamoDB Table → Data Storage

## 3. Important Terms & Definitions

| Term             | Definition                                    |
| ---------------- | --------------------------------------------- |
| Table            | Collection of items                           |
| Item             | Single record in a table                      |
| Attribute        | Field within an item                          |
| Partition Key    | Primary key component used to distribute data |
| Sort Key         | Optional second key component                 |
| Primary Key      | Uniquely identifies an item                   |
| RCU              | Read Capacity Unit                            |
| WCU              | Write Capacity Unit                           |
| GSI              | Global Secondary Index                        |
| LSI              | Local Secondary Index                         |
| TTL              | Time to Live, automatic item expiration       |
| DynamoDB Streams | Captures item-level changes                   |

## 4. DynamoDB vs RDS

| Feature     | DynamoDB               | Amazon RDS               |
| ----------- | ---------------------- | ------------------------ |
| Database    | NoSQL                  | Relational               |
| Data format | Items and attributes   | Rows and columns         |
| Schema      | Flexible attributes    | Defined table schema     |
| Query       | DynamoDB API / PartiQL | SQL                      |
| Scaling     | Managed scaling        | Instance/storage scaling |
| Joins       | Not supported natively | Supported                |

## 5. Creating a Table in DynamoDB

### AWS Console steps

1. Open AWS Console → DynamoDB.
2. Select Tables → Create table.
3. Table name: `Employees`.
4. Partition key: `EmployeeID` (String).
5. Sort key: Optional (leave blank).
6. Table settings: Default settings (on-demand).
7. Click Create table.
8. Wait for status Active.

### AWS CLI – Create Table

```
aws dynamodb create-table \
  --table-name Employees \
  --attribute-definitions \
    AttributeName=EmployeeID,AttributeType=S \
  --key-schema \
    AttributeName=EmployeeID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

Verify:

```
aws dynamodb list-tables

aws dynamodb describe-table \
  --table-name Employees
```

## 6. Inserting Values into DynamoDB

### AWS Console steps

1. DynamoDB → Tables → `Employees`.
2. Select Explore table items.
3. Click Create item.
4. Add attributes and values.
5. Click Create item.

### Sample data

| EmployeeID | Name  | Department | Salary |
| ---------- | ----- | ---------- | ------ |
| E101       | Atul  | IT         | 80000  |
| E102       | Ravi  | DevOps     | 65000  |
| E103       | Sneha | HR         | 55000  |

### AWS CLI – Insert Single Item

```
aws dynamodb put-item \
  --table-name Employees \
  --item '{
    "EmployeeID": {"S": "E101"},
    "Name": {"S": "Atul"},
    "Department": {"S": "IT"},
    "Salary": {"N": "80000"}
  }'
```

### Insert Another Item

```
aws dynamodb put-item \
  --table-name Employees \
  --item '{
    "EmployeeID": {"S": "E102"},
    "Name": {"S": "Ravi"},
    "Department": {"S": "DevOps"},
    "Salary": {"N": "65000"}
  }'
```

## 7. Read, Update and Delete Items

| Operation      | AWS CLI command                                      |
| -------------- | ---------------------------------------------------- |
| List tables    | `aws dynamodb list-tables`                           |
| Read all items | `aws dynamodb scan --table-name Employees`           |
| Describe table | `aws dynamodb describe-table --table-name Employees` |
| Delete table   | `aws dynamodb delete-table --table-name Employees`   |

### Read One Item

```
aws dynamodb get-item \
  --table-name Employees \
  --key '{"EmployeeID":{"S":"E101"}}'
```

### Update Salary

```
aws dynamodb update-item \
  --table-name Employees \
  --key '{"EmployeeID":{"S":"E101"}}' \
  --update-expression "SET Salary = :s" \
  --expression-attribute-values \
    '{":s":{"N":"90000"}}'
```

### Delete One Item

```
aws dynamodb delete-item \
  --table-name Employees \
  --key '{"EmployeeID":{"S":"E102"}}'
```

## 8. DynamoDB Data Types

| Type       | Symbol | Example           |
| ---------- | ------ | ----------------- |
| String     | S      | `"Atul"`          |
| Number     | N      | `"80000"`         |
| Boolean    | BOOL   | `true`            |
| Binary     | B      | Binary data       |
| List       | L      | `["AWS","Azure"]` |
| Map        | M      | Nested attributes |
| Null       | NULL   | `true`            |
| String Set | SS     | `["AWS","GCP"]`   |

## 9. Points to Remember for Interviews

- DynamoDB is a NoSQL, not a relational database.
- Every item requires a primary key.
- Primary keys can be partition-only or partition + sort key.
- `PutItem` creates or replaces an item with the same primary key.
- `GetItem` retrieves an item using its complete primary key.
- `Query` efficiently retrieves items using a partition key.
- `Scan` reads items across the table or index and can be expensive.
- On-demand billing charges for consumed requests and storage.
- DynamoDB supports eventual and strong consistency for applicable reads.
- DynamoDB Streams integrates with Lambda for event-driven processing.

## 10. Quick Hands-On Practice

Lab checklist

0/7 completed

Create Employees table

Insert E101 and E102

View all items using Scan

Get Employee E101

Update E101 salary

Delete Employee E102

Delete table after practice

Learning outcome: Create a DynamoDB table, insert employee records, retrieve records, update attributes and delete items using the AWS Console and CLI.

Cost reminder: DynamoDB can incur charges for requests, storage, backups and other features. Delete unused lab resources after practice.


# Amazon DynamoDB 

## Objectives

After completing this module, students will understand:

* DynamoDB Fundamentals
* NoSQL Concepts
* Tables, Items, Attributes
* Partition Keys and Sort Keys
* CRUD Operations
* Query vs Scan
* GSIs and LSIs
* DynamoDB Streams
* Global Tables
* TTL
* Backup and Recovery
* Security Best Practices
* Python (Boto3) Integration
* AWS CLI Commands
* Real-World Architectures
* Interview Questions
* Hands-On Project

---

# What is DynamoDB?

Amazon DynamoDB is a fully managed, serverless NoSQL database service provided by AWS.

Features:

* Fully Managed
* Serverless
* Highly Available
* Millisecond Latency
* Automatic Scaling
* Multi-AZ Replication
* Backup & Recovery
* IAM Integration

---

# Why DynamoDB?

Traditional Databases:

* Server Management
* Patch Management
* Backup Configuration
* Scaling Challenges

DynamoDB:

* No Servers
* No OS Management
* Automatic Scaling
* Pay-As-You-Go

---

# RDBMS vs DynamoDB

| Relational Database | DynamoDB           |
| ------------------- | ------------------ |
| Table               | Table              |
| Row                 | Item               |
| Column              | Attribute          |
| Primary Key         | Partition Key      |
| Join                | Not Supported      |
| Fixed Schema        | Flexible Schema    |
| Vertical Scaling    | Horizontal Scaling |

---

# Core Components

## Table

Collection of Items.

Example:

Student Table

---

## Item

Individual Record.

Example:

```json
{
 "StudentID":"STU001",
 "Name":"Atul Kamble",
 "City":"Pune"
}
```

---

## Attribute

Individual Data Field.

Examples:

```text
StudentID
Name
Email
City
Department
```

---

# DynamoDB Data Types

## String

```json
{
 "Name":"Atul"
}
```

## Number

```json
{
 "Age":24
}
```

## Boolean

```json
{
 "Active":true
}
```

## List

```json
{
 "Skills":["AWS","Azure","Docker"]
}
```

## Map

```json
{
 "Address":{
   "City":"Pune",
   "State":"Maharashtra"
 }
}
```

---

# Primary Keys

## Partition Key

Unique Identifier.

Example:

```text
StudentID
```

Values:

```text
STU001
STU002
STU003
```

---

## Composite Key

Partition Key + Sort Key

Example:

```text
StudentID + Semester
```

| StudentID | Semester |
| --------- | -------- |
| STU001    | Sem1     |
| STU001    | Sem2     |
| STU001    | Sem3     |

---

# Capacity Modes

## On-Demand

AWS manages scaling.

Best For:

* Labs
* Student Practice
* Unknown Traffic

Benefits:

* No Capacity Planning
* Automatic Scaling

---

## Provisioned

Specify:

* Read Capacity Units (RCU)
* Write Capacity Units (WCU)

Best For:

* Production Workloads
* Predictable Traffic

---

# DynamoDB Architecture

```text
User
 |
Application
 |
Boto3 SDK
 |
DynamoDB
 |
Multi-AZ Storage
```

---

# CRUD Operations

## Create

```python
table.put_item(
 Item={
  'StudentID':'STU001',
  'Name':'Atul Kamble'
 }
)
```

---

## Read

```python
table.get_item(
 Key={
  'StudentID':'STU001'
 }
)
```

---

## Update

```python
table.update_item(
 Key={'StudentID':'STU001'},
 UpdateExpression="SET City=:c",
 ExpressionAttributeValues={
  ':c':'Pune'
 }
)
```

---

## Delete

```python
table.delete_item(
 Key={'StudentID':'STU001'}
)
```

---

# Query vs Scan

## Query

* Uses Key
* Faster
* Cheaper

## Scan

* Reads Entire Table
* Slower
* Expensive

Memory Trick:

```text
Q = Quick

S = Slow
```

Interview Favorite Question.

---

# Global Secondary Index (GSI)

Problem:

Need to search using Email.

Without GSI:

```text
Scan Entire Table
```

With GSI:

```text
EmailIndex
```

Search:

```text
student@example.com
```

Benefits:

* Faster Search
* Lower Cost

---

# Local Secondary Index (LSI)

Uses:

* Same Partition Key
* Different Sort Key

Must be created during table creation.

Memory Trick:

```text
G = Global = Flexible

L = Local = Same Partition Key
```

---

# DynamoDB Streams

Tracks:

* INSERT
* UPDATE
* DELETE

Architecture:

```text
DynamoDB
   |
Stream
   |
Lambda
   |
SNS
   |
Email
```

Memory Formula:

```text
I U D

Insert
Update
Delete
```

---

# Time To Live (TTL)

Automatically deletes expired records.

Use Cases:

* OTP
* Session Data
* Temporary Records

Example:

```text
OTP Expires
     |
TTL Trigger
     |
Record Deleted
```

---

# Backup and Recovery

## On-Demand Backup

Manual Backup.

---

## Point-In-Time Recovery (PITR)

Restore table to a specific point.

Benefits:

* Accident Recovery
* Disaster Recovery

---

# Global Tables

Multi-Region Replication.

Architecture:

```text
Mumbai
   ↔
Singapore
   ↔
US-East-1
```

Benefits:

* Disaster Recovery
* Low Latency
* Active-Active Architecture

---

# Security

## IAM

Controls Access.

Examples:

* Read Only
* Full Access
* Custom Policies

---

## Encryption

Using:

* AWS Managed Keys
* AWS KMS

---

# Monitoring

Using CloudWatch.

Monitor:

* Read Requests
* Write Requests
* Throttling
* Latency
* Errors

---

# Hands-On Project

## Project Name

Student Management System

### Requirements

Store:

* Student ID
* Name
* Email
* Department
* Phone
* City

---

# Create Table

```bash
aws dynamodb create-table \
--table-name Student \
--attribute-definitions AttributeName=StudentID,AttributeType=S \
--key-schema AttributeName=StudentID,KeyType=HASH \
--billing-mode PAY_PER_REQUEST
```

---

# List Tables

```bash
aws dynamodb list-tables
```

---

# Describe Table

```bash
aws dynamodb describe-table \
--table-name Student
```

---

# Delete Table

```bash
aws dynamodb delete-table \
--table-name Student
```

---

# Install Boto3

```bash
pip install boto3
```

Configure AWS:

```bash
aws configure
```

---

# Python Application

## app.py

```python
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
```

---

# Real-World Use Cases

## Shopping Cart

Table:

```text
UserID
ProductID
Quantity
```

Why?

* Millions of Users
* Fast Reads
* Fast Writes

---

## Netflix User Profiles

Store:

* Preferences
* Watch History
* Recommendations

Why?

Millisecond Response Time.

---

## OTP Verification

Store:

* Mobile Number
* OTP
* Expiry Time

Use:

TTL

---

## Banking Sessions

Store:

* Session ID
* Expiry Time

Use:

TTL Auto Deletion

---

## IoT Sensor Data

Keys:

```text
DeviceID
Timestamp
```

Millions of Writes Per Second.

---

## Gaming Leaderboards

Store:

* Player
* Score

Fast Ranking Queries.

---

## Employee Attendance

Composite Key:

```text
EmployeeID
Date
```

---

## Student Management

Store:

* Student Information
* Email GSI
* Department Search

---

## DevOps Build Logs

Store:

* ProjectID
* BuildID
* Status

Architecture:

```text
GitHub
   |
Jenkins
   |
Lambda
   |
DynamoDB
```

---

# Best Practices

1. Choose Good Partition Keys
2. Avoid Hot Partitions
3. Prefer Query Over Scan
4. Use GSIs Carefully
5. Enable PITR
6. Enable CloudWatch Monitoring
7. Use IAM Least Privilege
8. Use TTL for Temporary Data
9. Avoid Unnecessary Indexes
10. Use On-Demand for Labs

---

# Points to Remember

## Golden Rules

### Rule 1

DynamoDB is NoSQL.

### Rule 2

No Server Management.

### Rule 3

Query > Scan.

### Rule 4

No Traditional JOINS.

### Rule 5

Design Based on Access Patterns.

### Rule 6

Partition Key Selection is Critical.

### Rule 7

GSI is Better Than Full Table Scan.

---

# Interview Questions

## What is DynamoDB?

Fully Managed NoSQL Database Service.

---

## SQL or NoSQL?

NoSQL.

---

## What is a Partition Key?

Unique Identifier used to distribute data.

---

## Difference Between Query and Scan?

Query:

* Fast
* Uses Key

Scan:

* Slow
* Reads Entire Table

---

## What are GSIs?

Alternative Query Mechanism.

---

## What are LSIs?

Indexes using the same Partition Key.

---

## What is DynamoDB Streams?

Tracks Insert, Update, Delete events.

---

## What is TTL?

Automatically deletes expired records.

---

## What is PITR?

Point-In-Time Recovery.

---

## What are Global Tables?

Multi-Region Active-Active Replication.

---

# Exam Keywords

| Requirement           | Service          |
| --------------------- | ---------------- |
| NoSQL                 | DynamoDB         |
| Key Value Database    | DynamoDB         |
| Document Database     | DynamoDB         |
| Millisecond Latency   | DynamoDB         |
| Auto Scaling          | DynamoDB         |
| Serverless Database   | DynamoDB         |
| Multi Region Database | Global Tables    |
| Event Trigger         | Streams + Lambda |
| Monitoring            | CloudWatch       |
| Encryption            | KMS              |
| Backup                | PITR             |

---

# One-Minute Revision

```text
Table = Collection

Item = Record

Attribute = Column

Partition Key = Unique Identifier

Sort Key = Additional Identifier

Query > Scan

No JOINS

GSI = Faster Search

Streams = Change Tracking

TTL = Auto Delete

PITR = Recovery

CloudWatch = Monitoring

IAM = Security

KMS = Encryption

Global Tables = Multi-Region
```

---

# Practice Lab

Task 1:
Create Student Table.

Task 2:
Insert 10 Records.

Task 3:
Update Student City.

Task 4:
Delete Student.

Task 5:
Create Email GSI.

Task 6:
Enable Streams.

Task 7:
Trigger Lambda.

Task 8:
Send SNS Notification.

Task 9:
Enable PITR.

Task 10:
Monitor Using CloudWatch.

---

# Final Interview Formula

Remember:

```text
Fast + Scalable + Serverless + NoSQL

= DynamoDB
```

Whenever AWS asks for:

* Key-Value Database
* Document Database
* Millisecond Latency
* Massive Scale
* Serverless Architecture

The answer is usually DynamoDB.

---

# 🎵 DynamoDB Example – Music Table

This guide demonstrates how to create a **DynamoDB table**, insert sample records, and query data.

---

## 1️⃣ Create DynamoDB Table

```bash
aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --table-class STANDARD
```

* **Partition key (HASH):** `Artist`
* **Sort key (RANGE):** `SongTitle`
* **Billing mode:** On-demand (`PAY_PER_REQUEST`)

---

## 2️⃣ Insert Sample Records

```bash
aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'

aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Howdy"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "2"}}'

aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}, "AlbumTitle": {"S": "Songs About Life"}, "Awards": {"N": "10"}}'

aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "PartiQL Rocks"}, "AlbumTitle": {"S": "Another Album Title"}, "Awards": {"N": "8"}}'
```

---

## 3️⃣ Retrieve a Single Item

```bash
aws dynamodb get-item --consistent-read \
    --table-name Music \
    --key '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}}'
```

---

## 4️⃣ Query with PartiQL (SQL-compatible)

```sql
SELECT * FROM Music
WHERE Artist = 'Acme Band';
```

👉 PartiQL support in DynamoDB allows you to run SQL-like queries directly.

---
