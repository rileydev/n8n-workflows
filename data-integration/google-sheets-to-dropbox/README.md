# Google Sheets to Dropbox Sync

This workflow automatically syncs data from a Google Sheet to Dropbox by converting it to an Excel file and uploading it every 15 minutes.

## Overview

The workflow performs the following steps:
1. Triggers every 15 minutes
2. Reads data from a specified Google Sheet
3. Converts the data to an Excel (.xls) file
4. Uploads the file to a specified Dropbox path

## Requirements

- n8n instance with:
  - Google Sheets API credentials configured
  - Dropbox API credentials configured
- Access to the source Google Sheet
- Dropbox account with write permissions

## Setup

1. Import the workflow JSON into your n8n instance
2. Configure the required credentials:
   - Google Sheets API credentials
   - Dropbox API credentials
3. Update the following parameters:
   - `Read Sheet` node: Set the correct Google Sheet ID
   - `Upload Dropbox` node: Update the path where files should be saved
4. Adjust the interval timing if needed (default: 15 minutes)

## Usage

1. Ensure the Google Sheet is accessible with the configured credentials
2. Activate the workflow
3. The workflow will automatically:
   - Read the latest data from Google Sheets
   - Convert it to Excel format
   - Upload it to Dropbox at the specified interval

## Example Use Cases

- Automated backup of Google Sheets data
- Sharing Google Sheets data with Dropbox users
- Creating Excel snapshots of Google Sheets data
- Maintaining Excel copies of Google Sheets reports

## Additional Notes

- The workflow runs every 15 minutes by default
- Files are saved in .xls format
- Previous versions in Dropbox will be overwritten
- Consider Dropbox storage limits and API rate limits
