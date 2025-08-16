Here’s an updated **README** section for your **DynamoDB** example, formatted and structured for clarity:

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

⚡ With this setup, you can now test **CRUD operations** on DynamoDB using AWS CLI and PartiQL.

---

Do you want me to also extend this README with **UpdateItem**, **DeleteItem**, and **Query/Scan** examples for completeness? That way it will cover full DynamoDB CRUD.
