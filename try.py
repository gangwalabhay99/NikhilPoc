import json
from jinja2 import Template
import os
import requests


with open("test.json", "r") as json_file:
    json_data = json_file.read()

# Parse the JSON data
data = json.loads(json_data)

# Extract the controls results
controls_results = data.get("profiles", [])[0].get("controls", [])

# Count the number of passed occurrences
passed_count = sum(1 for control in controls_results for result in control.get("results", []) if result.get("status") == "passed")
failed_count = sum(1 for control in controls_results for result in control.get("results", []) if result.get("status") == "failed")
total_count = failed_count + passed_count 

# printing count 
print("Number of failed occurrences:", failed_count)
print("Number of passed occurrences:", passed_count)
print("Number of total cases occurrences:", total_count)

with open("templateResults.md", "r") as f:
 template = Template(f.read())

 markdown = template.render(context)

repository_full_name = os.getenv("GITHUB_REPOSITORY")
owner = repository_full_name.split('/')[0]
repo = repository_full_name.split('/')[1]

repository_owner = owner
repository_name = repo

# Set your GitHub token as an environment variable or replace with your actual token
github_token = os.environ.get("GITHUB_TOKEN")

# Set the commit SHA for which you want to create the check run
commit_sha = os.getenv("GITHUB_SHA")

# Set the URL for creating a check run
check_run_url = f"https://api.github.com/repos/{repository_owner}/{repository_name}/check-runs"

print(repository_owner)
print(repository_name)
print(github_token)
print(commit_sha)
print(markdown)

# Set the headers for the API request
headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github.antiope-preview+json"
}

# Set the payload for creating the check run
payload = {
    "name": "Detailed Result",
    "head_sha": commit_sha,
    "status": "completed",
    "conclusion": "success",
    "output": {
        "title": "Detailed Results",
        "summary": markdown
        
    }
}

# Send the API request to create the check run
response = requests.post(check_run_url, json=payload, headers=headers)
# Check if the API request was successful
if response.status_code == 201:
    print("Check run created successfully!")
else:
    print(f"Failed to create check run. Status code: {response.status_code}")
    print("Response:", response.text)


