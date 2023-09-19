import os
import requests
import subprocess

# Define your GitHub repository information
github_username = "knight-research"
github_repo = "KIDD"

# Get the latest release information from GitHub
url = f"https://api.github.com/repos/{github_username}/{github_repo}/releases/latest"
response = requests.get(url)
if response.status_code == 200:
    latest_version = response.json()["tag_name"]
else:
    print("Failed to fetch the latest version from GitHub.")
    latest_version = None

# Get the current local version
current_version = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()

# Compare versions
if latest_version and latest_version != current_version:
    print(f"Updating from {current_version} to {latest_version}")
    # Run 'git pull' to update
    os.system("git pull")
else:
    print("No update needed.")

# Copy the updated files to your desired location on the Raspberry Pi
if latest_version and latest_version != current_version:
    # Replace with the appropriate path on your Raspberry Pi
    destination_path = "/path/to/your/project/on/raspberry/pi"
    os.system(f"cp -r ./* {destination_path}")
    print("Project updated on the Raspberry Pi.")
