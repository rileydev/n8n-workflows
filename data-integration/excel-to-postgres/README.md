# Excel to PostgreSQL Data Import

This workflow reads data from an Excel spreadsheet file and automatically imports it into a PostgreSQL database table.

## Overview

The workflow performs the following steps:
1. Reads a binary Excel file from the filesystem
2. Processes the spreadsheet data using the Spreadsheet node
3. Inserts the data into a PostgreSQL table

## Requirements

- n8n instance with access to:
  - Local filesystem (for reading Excel file)
  - PostgreSQL database
- PostgreSQL credentials configured in n8n
- Excel file (.xls format) with data to import

## Setup

1. Import the workflow JSON into your n8n instance
2. Configure PostgreSQL credentials in n8n if not already done
3. Update the following parameters:
   - `Read Binary File` node: Set the correct path to your Excel file
   - `Insert Rows` node: Update table name and column mappings if different from "product" and "name,ean"

## Usage

1. Place your Excel file at the specified path
2. Activate the workflow
3. Run the workflow manually or trigger it as needed

## Example Use Cases

- Importing product catalogs from Excel to a database
- Syncing inventory data from spreadsheets to a database
- Migrating legacy data stored in Excel files to PostgreSQL

## Additional Notes

- The workflow expects the Excel file to be in .xls format
- Make sure the PostgreSQL table schema matches your Excel data structure
- Consider adding error handling for missing files or data format issues
