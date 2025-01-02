# Excel to PostgreSQL Data Integration

This workflow automates the process of inserting data from an Excel file into a PostgreSQL database.

## Requirements

1. n8n instance
2. PostgreSQL database credentials
3. Excel file accessible to n8n

## Setup

1. Import the workflow JSON into your n8n instance
2. Configure the following credentials:
   - PostgreSQL: Enter your database connection details
3. Update the workflow nodes:
   - Excel File: Set the path to your Excel file
   - PostgreSQL: Configure the target table and columns

## Usage

1. Place your Excel file in the specified location
2. Activate the workflow
3. The workflow will:
   - Read the Excel file
   - Transform the data as needed
   - Insert records into the PostgreSQL database

## Example Use Cases

- Migrating data from spreadsheets to a database
- Automating regular data imports
- Syncing spreadsheet data with a database

## Notes

- Ensure the Excel file structure matches the database table schema
- The workflow can be scheduled to run automatically
- Error handling is included to manage data validation issues
