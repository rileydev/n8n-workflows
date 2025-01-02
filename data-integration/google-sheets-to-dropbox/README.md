# Google Sheets to Dropbox Data Integration

This workflow automates the process of exporting data from Google Sheets to Dropbox.

## Requirements

1. n8n instance
2. Google Sheets API credentials
3. Dropbox API credentials
4. Google Sheet with data to export

## Setup

1. Import the workflow JSON into your n8n instance
2. Configure the following credentials:
   - Google Sheets: Set up OAuth2 credentials
   - Dropbox: Set up OAuth2 credentials
3. Update the workflow nodes:
   - Google Sheets: Specify the spreadsheet ID and range
   - Dropbox: Configure the target file path and format

## Usage

1. Ensure your Google Sheet is accessible to the API
2. Activate the workflow
3. The workflow will:
   - Read data from the specified Google Sheet
   - Convert the data to the desired format
   - Upload the file to Dropbox

## Example Use Cases

- Automating regular data backups
- Sharing spreadsheet data with team members
- Migrating data between cloud services

## Notes

- The workflow supports multiple file formats (CSV, JSON, etc.)
- Can be scheduled to run automatically
- Includes error handling for API rate limits
