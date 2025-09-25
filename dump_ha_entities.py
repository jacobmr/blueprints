import os
import requests
import csv
import json
import sys
from datetime import datetime

# Configuration
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"
OUTPUT_FILE = os.path.expanduser("~/ha_entities_export.csv")

# Set up headers with authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def main():
    print(f"Connecting to Home Assistant at {BASE_URL}...")
    
    try:
        # Test the connection first
        response = requests.get(f"{BASE_URL}/api/", headers=HEADERS, timeout=10)
        response.raise_for_status()
        print("✓ Successfully connected to Home Assistant API")
        
        # Get all states
        print("Fetching entity states...")
        response = requests.get(f"{BASE_URL}/api/states", headers=HEADERS, timeout=30)
        response.raise_for_status()
        
        entities = response.json()
        print(f"Found {len(entities)} entities")
        
        # Write to CSV
        with open(OUTPUT_FILE, mode="w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Entity ID", "Friendly Name", "Domain", "Device Class", "State", "Last Updated"])
            
            for entity in entities:
                try:
                    entity_id = entity.get("entity_id", "")
                    attributes = entity.get("attributes", {})
                    name = attributes.get("friendly_name", "")
                    domain = entity_id.split(".")[0] if entity_id else ""
                    device_class = attributes.get("device_class", "")
                    state = entity.get("state", "")
                    last_updated = entity.get("last_updated", "")
                    
                    writer.writerow([entity_id, name, domain, device_class, state, last_updated])
                except Exception as e:
                    print(f"Error processing entity {entity_id}: {str(e)}")
        
        print(f"✅ Successfully exported {len(entities)} entities to {OUTPUT_FILE}")
        print(f"File size: {os.path.getsize(OUTPUT_FILE) / 1024:.2f} KB")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to Home Assistant: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Status code: {e.response.status_code}")
            try:
                print(f"Response: {e.response.text}")
            except:
                pass
        sys.exit(1)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
