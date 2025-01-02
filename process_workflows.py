import os
import json
import shutil
from pathlib import Path

# Configuration
WORKFLOWS_SOURCE = "extracted_workflows/automation"
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
    """Generate a detailed README file for the workflow"""
    # Load workflow JSON
    with open(os.path.join(workflow_path, "workflow.json")) as f:
        workflow_data = json.load(f)
    
    # Extract workflow details
    workflow_title = workflow_name.replace('-', ' ').title()
    nodes = workflow_data.get('nodes', [])
    
    # Extract node types and credentials
    node_types = set()
    credentials = set()
    for node in nodes:
        node_types.add(node.get('type'))
        if 'credentials' in node:
            for cred in node['credentials']:
                credentials.add(cred)
    
    # Analyze workflow with AI
    ai_analysis = analyze_workflow_with_ai(workflow_data)
    
    # Generate detailed README content
    readme_content = f"""# {workflow_title}

## Description

{ai_analysis.get('description', 'This workflow provides automation for ' + workflow_name.replace('-', ' '))}

## Key Features

{ai_analysis.get('key_features', '- Automated data processing using {len(nodes)} nodes\n- Integration with {len(credentials)} services: {", ".join(credentials) or "None"}\n- Error handling and logging\n- Customizable configuration')}

## Requirements

1. n8n instance (version 0.200.0 or higher recommended)
2. Required credentials for:
   - {', '.join(credentials) or 'No external services'}
3. Access to necessary data sources and destinations

## Setup Instructions

{ai_analysis.get('setup_instructions', generate_credentials_setup(credentials))}

## Usage

{ai_analysis.get('usage', '1. Ensure all required services are accessible\n2. Activate the workflow\n3. Monitor execution through n8n\'s interface\n4. Review logs and outputs for verification')}

## Example Use Cases

{ai_analysis.get('example_use_cases', generate_example_use_cases(nodes))}

## Notes

{ai_analysis.get('notes', '- Review and test the workflow thoroughly before production use\n- Modify node configurations as needed for your specific requirements\n- Consider implementing error notifications for critical failures\n- The workflow can be scheduled for regular execution')}

## Troubleshooting

{ai_analysis.get('troubleshooting', generate_troubleshooting_guide(nodes))}

## Additional Resources

- n8n documentation: https://docs.n8n.io
- Workflow best practices guide
- Community forum for workflow discussions
"""

import requests

DEEPSEEK_API_URL = "https://api.deepseek.com/v1/analyze"
DEEPSEEK_API_KEY = "sk-276fac83062844ac9c6465fd5bf627fe"

def analyze_workflow_with_ai(workflow_data):
    """Analyze workflow using DeepSeek AI to generate insights"""
    if not DEEPSEEK_API_KEY:
        return {}
        
    try:
        # Prepare prompt for DeepSeek
        prompt = f"""Analyze this n8n workflow JSON and provide:
1. A concise description of its purpose and functionality
2. Key features and capabilities
3. Setup instructions
4. Usage guidelines
5. Example use cases
6. Important notes
7. Troubleshooting tips

Workflow JSON: {json.dumps(workflow_data)}
"""
        
        # Call DeepSeek API
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        response = requests.post(
            DEEPSEEK_API_URL,
            headers=headers,
            json={"prompt": prompt}
        )
        response.raise_for_status()
        
        # Parse DeepSeek response
        analysis = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
        
        # Extract sections from analysis
        return {
            'description': extract_section(analysis, "Description"),
            'key_features': extract_section(analysis, "Key Features"),
            'setup_instructions': extract_section(analysis, "Setup Instructions"),
            'usage': extract_section(analysis, "Usage Guidelines"),
            'example_use_cases': extract_section(analysis, "Example Use Cases"),
            'notes': extract_section(analysis, "Important Notes"),
            'troubleshooting': extract_section(analysis, "Troubleshooting Tips")
        }
    except Exception as e:
        print(f"DeepSeek analysis failed: {str(e)}")
        return {}

def extract_section(text, section_name):
    """Extract a specific section from the analysis text"""
    start = text.find(f"{section_name}:")
    if start == -1:
        return ""
    start += len(section_name) + 1
    end = text.find("\n\n", start)
    return text[start:end].strip() if end != -1 else text[start:].strip()

def generate_workflow_description(nodes):
    """Generate workflow description based on nodes"""
    description = []
    for node in nodes:
        node_type = node.get('type', 'unknown')
        description.append(f"- {node_type} node: {node.get('notes', 'No description available')}")
    return '\n'.join(description) if description else 'No detailed description available'

def generate_credentials_setup(credentials):
    """Generate credentials setup instructions"""
    if not credentials:
        return "No external credentials required"
    setup = []
    for cred in credentials:
        setup.append(f"   - {cred}: [Add instructions for {cred} credentials]")
    return '\n'.join(setup)

def generate_node_configuration(nodes):
    """Generate node configuration instructions"""
    if not nodes:
        return "No specific node configuration required"
    config = []
    for node in nodes:
        node_type = node.get('type', 'unknown')
        config.append(f"   - {node_type}: [Add configuration details]")
    return '\n'.join(config)

def generate_example_use_cases(nodes):
    """Generate example use cases based on nodes"""
    use_cases = []
    for node in nodes:
        node_type = node.get('type', 'unknown')
        use_cases.append(f"- {node_type} node: [Add use case description]")
    return '\n'.join(use_cases) if use_cases else "No specific use cases defined"

def generate_troubleshooting_guide(nodes):
    """Generate troubleshooting guide based on nodes"""
    issues = []
    for node in nodes:
        node_type = node.get('type', 'unknown')
        issues.append(f"- {node_type} node: [Add common issues and solutions]")
    return '\n'.join(issues) if issues else "No specific troubleshooting information available"

    # Write README file
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
