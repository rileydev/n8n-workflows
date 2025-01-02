import os
import json
import shutil
from pathlib import Path

# Configuration
WORKFLOWS_SOURCE = "../extracted_workflows/automation"
WORKFLOWS_DEST = "."
CATEGORIES = {
    "data-integration": ["excel", "google", "database", "sync"],
    "data-transformation": ["transform", "convert", "process"],
    "automation": ["automation", "workflow", "task"],
    "api-webhooks": ["api", "webhook", "integration"],
    "document-processing": ["document", "file", "pdf"],
    "communication": ["email", "message", "notification"],
    "analytics": ["report", "analysis", "statistics"]
}

def determine_category(workflow_name):
    """Determine the category based on workflow name keywords"""
    workflow_name = workflow_name.lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in workflow_name for keyword in keywords):
            return category
    return "automation"  # Default category

def generate_readme(workflow_path, workflow_name):
    """Generate a basic README file for the workflow"""
    readme_content = f"""# {workflow_name.replace('-', ' ').title()}

This workflow automates the process of {workflow_name.replace('-', ' ')}.

## Requirements

1. n8n instance
2. Relevant credentials (if applicable)

## Setup

1. Import the workflow JSON into your n8n instance
2. Configure any required credentials
3. Update the workflow nodes as needed

## Usage

1. Activate the workflow
2. The workflow will execute the automated process

## Notes

- Review and test the workflow before production use
- Modify as needed for your specific use case
"""
    with open(os.path.join(workflow_path, "README.md"), "w") as f:
        f.write(readme_content)

def process_workflows():
    """Process all workflows from source to destination"""
    for workflow_file in os.listdir(WORKFLOWS_SOURCE):
        if workflow_file.endswith(".json"):
            workflow_name = os.path.splitext(workflow_file)[0]
            category = determine_category(workflow_name)
            
            # Create destination directory
            dest_dir = os.path.join(WORKFLOWS_DEST, category, workflow_name)
            os.makedirs(dest_dir, exist_ok=True)
            
            # Copy workflow file
            src_path = os.path.join(WORKFLOWS_SOURCE, workflow_file)
            dest_path = os.path.join(dest_dir, "workflow.json")
            shutil.copy(src_path, dest_path)
            
            # Generate README
            generate_readme(dest_dir, workflow_name)
            
            print(f"Processed: {workflow_name} -> {category}")

if __name__ == "__main__":
    process_workflows()
