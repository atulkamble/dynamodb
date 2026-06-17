# Amazon DynamoDB - Complete Training Guide

## Course Objectives

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
