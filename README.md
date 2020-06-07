# GateFlow
**GateFlow** is an open-source project to build ETL (Extract Transform and Load) data pipeline.

### Import Library
```python
import gateflow
```

### Supported Data Sources
- RDBMS ```SQLReader()```
    - MySQL or MariaDB
    - PostgreSQL
    - SQLite
    - Microsoft SQL Server
    - Oracle
- NoSQL
    - MongoDB ```MongoReader()```
- Spreadsheet
    - Google Sheet ```GoogleSheetReader()```
- External API
    - Curv ```CurvReader()```
    - Indodax ```IndodaxReader()```
    - Binance ```BinanceReader()```
    
### Supported Target
- BigQuery ```GBQWriter()```

### Sample Code
```python

## Import Library
import gateflow as gf

## Initiate database information
db_info = {
    'host': '<hostname>',
    'port': '<port number>',
    'dialect': '<database dialect>',
    'driver': '<database driver for python>',
    'db_name': '<database name>',
    'username': '<username to access>',
    'password': '<password to access>',
    'additional_string': '<additional_string>'
}

db_uri = gf.construct_uri(db_info)

## Read table using SQLReader

reader = gf.SQLReader(db_uri)
df = reader.read_table('<table_name>')

## Initiate BigQuery project_id and service_account_path
## You can get the service account key from
## https://console.cloud.google.com/apis/credentials/serviceaccountkey

project_id = '<GCP Project ID>'
service_account_path = '/absolute/path/to/service_account.json'

writer = gf.GbqWriter(project_id, service_account_path)
writer.from_frame(df, '<dataset name>', '<table_name>')
```
