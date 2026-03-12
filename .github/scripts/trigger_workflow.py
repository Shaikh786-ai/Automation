import requests

# Replace these
GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"
OWNER = "your-username-or-org"
REPO = "your-repo"
WORKFLOW_ID = "trigger-workflow.yml"  # workflow filename
BRANCH = "main"

url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}
data = {"ref": BRANCH}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 204:
    print("Workflow triggered successfully!")
else:
    print("Error triggering workflow:", response.text)
