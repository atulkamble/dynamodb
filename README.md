# AWS DynamoDB 

Topics: Introduction, Key Concepts, Comparisons, Table Creation, CRUD Operations, Query vs Scan, GSI, and AWS CLI.

## 1. What is DynamoDB?

Amazon DynamoDB is a fully managed, serverless NoSQL database service that provides fast, scalable key-value and document storage.

### Points to Remember

- No server installation or maintenance.
- Stores data in tables, items, and attributes.
- Supports automatic scaling.
- Uses partition keys and optional sort keys.
- Supports on-demand and provisioned capacity.
- Integrates with Lambda, IAM, and CloudWatch.
- Supports backup, encryption, and recovery.

## 2. Important Terms

| Term          | Definition                                |
| ------------- | ----------------------------------------- |
| Table         | Collection of items                       |
| Item          | Single record                             |
| Attribute     | Field in a record                         |
| Partition Key | Key used to distribute data               |
| Sort Key      | Optional key for organizing related items |
| Primary Key   | Uniquely identifies an item               |
| RCU           | Read Capacity Unit                        |
| WCU           | Write Capacity Unit                       |
| GSI           | Global Secondary Index                    |
| LSI           | Local Secondary Index                     |
| TTL           | Time to Live                              |
| Streams       | Captures item changes                     |

## 3. DynamoDB vs RDS

| DynamoDB                  | RDS                      |
| ------------------------- | ------------------------ |
| NoSQL                     | Relational               |
| Flexible schema           | Defined schema           |
| Items and attributes      | Rows and columns         |
| DynamoDB API / PartiQL    | SQL                      |
| No native joins           | Supports joins           |
| Managed partition scaling | Instance/storage scaling |

## 4. Partition Key vs Sort Key

| Partition Key    | Sort Key                            |
| ---------------- | ----------------------------------- |
| Mandatory        | Optional                            |
| Distributes data | Orders items within a partition key |
| HASH             | RANGE                               |
| Example: Artist  | Example: SongTitle                  |

## 5. Hands-on Practice – Employees Table

### Step 1 – Create Table

```
aws dynamodb create-table \
  --table-name Employees \
  --attribute-definitions \
    AttributeName=EmployeeID,AttributeType=S \
  --key-schema \
    AttributeName=EmployeeID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

### Step 2 – List Tables

```
aws dynamodb list-tables
```

### Step 3 – Describe Table

```
aws dynamodb describe-table \
  --table-name Employees
```

### Step 4 – Insert Records

```
aws dynamodb put-item \
  --table-name Employees \
  --item '{
    "EmployeeID":{"S":"E101"},
    "Name":{"S":"Atul"},
    "Department":{"S":"IT"},
    "Salary":{"N":"80000"}
  }'
```

```
aws dynamodb put-item \
  --table-name Employees \
  --item '{
    "EmployeeID":{"S":"E102"},
    "Name":{"S":"Ravi"},
    "Department":{"S":"DevOps"},
    "Salary":{"N":"65000"}
  }'
```

### Step 5 – View All Records

```
aws dynamodb scan \
  --table-name Employees
```

### Step 6 – Get Specific Record

```
aws dynamodb get-item \
  --table-name Employees \
  --key '{"EmployeeID":{"S":"E101"}}'
```

### Step 7 – Update Salary

```
aws dynamodb update-item \
  --table-name Employees \
  --key '{"EmployeeID":{"S":"E101"}}' \
  --update-expression "SET Salary = :s" \
  --expression-attribute-values \
    '{":s":{"N":"90000"}}'
```

### Step 8 – Query Record

```
aws dynamodb query \
  --table-name Employees \
  --key-condition-expression "EmployeeID = :id" \
  --expression-attribute-values \
    '{":id":{"S":"E101"}}'
```

### Step 9 – Delete Record

```
aws dynamodb delete-item \
  --table-name Employees \
  --key '{"EmployeeID":{"S":"E102"}}'
```

### Step 10 – Delete Table

```
aws dynamodb delete-table \
  --table-name Employees
```

## 6. Query vs Scan

| Query                        | Scan                             |
| ---------------------------- | -------------------------------- |
| Uses partition key           | No key required                  |
| Efficient for specific items | Reads across table/index         |
| Generally faster             | Can be slower                    |
| Preferred for key lookups    | Useful for full-table inspection |

Remember: Prefer Query over Scan when the access pattern supports it.

## 7. GSI vs LSI

| GSI                             | LSI                          |
| ------------------------------- | ---------------------------- |
| Different partition key allowed | Same partition key           |
| Can be created later            | Must be created with table   |
| Eventually consistent           | Strong consistency supported |
| Alternative access pattern      | Alternative sort order       |

## 8. On-Demand vs Provisioned

| On-Demand                     | Provisioned                     |
| ----------------------------- | ------------------------------- |
| Pay per request               | Configure RCU/WCU               |
| Automatic capacity management | Capacity planning required      |
| Variable workloads            | Predictable workloads           |
| Recommended for labs          | Useful for controlled workloads |

## 9. Music Table – Composite Key Practice

Create table with partition key and sort key:

```
aws dynamodb create-table \
  --table-name Music \
  --attribute-definitions \
    AttributeName=Artist,AttributeType=S \
    AttributeName=SongTitle,AttributeType=S \
  --key-schema \
    AttributeName=Artist,KeyType=HASH \
    AttributeName=SongTitle,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
```

Insert record:

```
aws dynamodb put-item \
  --table-name Music \
  --item '{
    "Artist":{"S":"Acme Band"},
    "SongTitle":{"S":"Happy Day"},
    "AlbumTitle":{"S":"Songs About Life"},
    "Awards":{"N":"10"}
  }'
```

Read record:

```
aws dynamodb get-item \
  --table-name Music \
  --key '{
    "Artist":{"S":"Acme Band"},
    "SongTitle":{"S":"Happy Day"}
  }'
```

Query using partition key:

```
aws dynamodb query \
  --table-name Music \
  --key-condition-expression "Artist = :a" \
  --expression-attribute-values \
    '{":a":{"S":"Acme Band"}}'
```

Delete table after practice:

```
aws dynamodb delete-table \
  --table-name Music
```

## 10. Additional Features

| Feature          | Purpose                                   |
| ---------------- | ----------------------------------------- |
| DynamoDB Streams | Capture insert, modify, and delete events |
| TTL              | Automatically delete expired records      |
| PITR             | Restore table to a previous point         |
| Global Tables    | Multi-Region replication                  |
| IAM              | Access control                            |
| KMS              | Encryption key management                 |
| CloudWatch       | Monitoring and alarms                     |
| Boto3            | Python SDK integration                    |

## 11. Important Commands – Quick Revision

| Operation     | Command          |
| ------------- | ---------------- |
| Create        | `create-table`   |
| List          | `list-tables`    |
| Describe      | `describe-table` |
| Insert        | `put-item`       |
| Read          | `get-item`       |
| Update        | `update-item`    |
| Delete record | `delete-item`    |
| Query         | `query`          |
| Scan          | `scan`           |
| Delete table  | `delete-table`   |

All commands use the `aws dynamodb` prefix.

## 12. Final Points to Remember

1. DynamoDB is a fully managed NoSQL database.
2. Partition key is mandatory; sort key is optional.
3. Maximum item size is 400 KB.
4. `PutItem` inserts or replaces an item.
5. `GetItem` requires the complete primary key.
6. Query is generally preferable to Scan for key-based access.
7. GSI allows querying by alternative keys.
8. Streams integrates with Lambda.
9. TTL removes expired records asynchronously.
10. PITR supports recovery from accidental changes.
11. Global Tables enables multi-Region replication.
12. DynamoDB is suitable for serverless and high-scale applications.
