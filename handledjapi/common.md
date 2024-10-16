import requests
from .models import UnifiedData
import os

# Environment variables for authentication
HUBSPOT_ACCESS_TOKEN = os.environ.get("HUBSPOT_ACCESS_TOKEN")
CLICKUP_API_KEY = os.environ.get("CLICKUP_API_KEY")

# URLs for the APIs
HUBSPOT_URL = "https://api.hubapi.com/crm/v3/objects/contacts/"
CLICKUP_LIST_ID = "901204705980"
CLICKUP_URL = f"https://api.clickup.com/api/v2/list/{CLICKUP_LIST_ID}/task"

# Function to fetch data from both tools
def fetch_data_from_tools():
    # Fetch data from HubSpot
    hubspot_contacts = fetch_hubspot_data()

    # Fetch data from ClickUp
    clickup_tasks = fetch_clickup_data()

    # Save both to Django database
    save_to_db(hubspot_contacts, "HubSpot")
    save_to_db(clickup_tasks, "ClickUp")

    return hubspot_contacts, clickup_tasks


def fetch_hubspot_data():
    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.get(HUBSPOT_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error fetching HubSpot data: {response.status_code}")
        return []


def fetch_clickup_data():
    headers = {
        "Authorization": CLICKUP_API_KEY,
    }
    response = requests.get(CLICKUP_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get("tasks", [])
    else:
        print(f"Error fetching ClickUp data: {response.status_code}")
        return []


def save_to_db(data, source):
    for item in data:
        # Determine name based on the source
        if source == "HubSpot":
            # Extract first and last name from properties
            first_name = item.get("properties", {}).get("firstname", "Unknown")
            last_name = item.get("properties", {}).get("lastname", "Unknown")
            name = f"{first_name} {last_name}"  # Combine first and last name
        elif source == "ClickUp":
            name = item.get("name", "Unknown")  # Get name from ClickUp task
        else:
            name = "Unknown"  # Fallback if source is unknown

        # Create a unified JSON structure
        payload_data = {
            "id": item.get("id"),
            "name": name,
            "url": item.get("url", ""),  # Safely get the URL
            "source": source,
            "data": item,  # Saving the entire item as payload
        }

        print(f"Saving to DB: {payload_data}")  # Debug print

        # Save to the database
        UnifiedData.objects.create(
            name=name,  # Set the dynamically extracted name
            description=f"Data from {source}",  # Description indicating the source
            url=item.get("url", ""),  # URL field from the item
            payload=payload_data,  # JSONField to store payload data
        )
