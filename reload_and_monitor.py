import requests
import json
import time
from datetime import datetime

# Configuration - using the same as dump_ha_entities.py
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

# Set up headers with authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def reload_blueprints():
    """Reload all blueprints in Home Assistant."""
    print("Reloading blueprints...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/services/blueprint/reload",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        print("✓ Blueprints reloaded successfully")
        return True
    except Exception as e:
        print(f"Error reloading blueprints: {e}")
        return False

def get_automations():
    """Get list of automations to find our blueprint."""
    try:
        response = requests.get(
            f"{BASE_URL}/api/states",
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        return [e for e in response.json() if e['entity_id'].startswith('automation.')]
    except Exception as e:
        print(f"Error getting automations: {e}")
        return []

def watch_logs():
    """Stream and display Home Assistant logs in real-time."""
    print("Starting log stream (Ctrl+C to stop)...")
    print("-" * 80)
    
    try:
        with requests.get(
            f"{BASE_URL}/api/error_log",
            headers=HEADERS,
            stream=True,
            timeout=30
        ) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line:
                    print(f"{datetime.now().strftime('%H:%M:%S')} - {line.decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nLog monitoring stopped by user")
    except Exception as e:
        print(f"Error reading logs: {e}")

def main():
    # First, reload the blueprints
    if not reload_blueprints():
        print("Failed to reload blueprints. Check your configuration and try again.")
        return
    
    # Then start watching logs
    watch_logs()

if __name__ == "__main__":
    main()
