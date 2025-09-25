import requests
import json
from datetime import datetime

# Configuration
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

# Set up headers with authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def print_event(timestamp, event_type, data):
    """Print event in a clean format."""
    print(f"\n{timestamp} - {event_type}")
    if 'entity_id' in data:
        print(f"Entity: {data['entity_id']}")
    if 'old_state' in data:
        print(f"Old state: {data.get('old_state', {}).get('state')}")
    if 'new_state' in data:
        print(f"New state: {data.get('new_state', {}).get('state')}")
    if 'context' in data.get('new_state', {}):
        context = data['new_state']['context']
        print(f"Context ID: {context.get('id')}")

def monitor_automation_flow():
    print("Home Assistant Automation Flow Monitor")
    print("Watching for button presses and automation triggers...")
    print("-" * 80)
    
    try:
        with requests.get(
            f"{BASE_URL}/api/stream",
            headers=HEADERS,
            stream=True,
            timeout=30
        ) as response:
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    try:
                        event = json.loads(line[6:])  # Skip 'data: ' prefix
                        event_type = event.get('event_type')
                        data = event.get('data', {})
                        
                        # Only show relevant events
                        if event_type in ['state_changed', 'automation_triggered']:
                            entity_id = data.get('entity_id', '')
                            
                            # Show all button and light state changes
                            if ('binary_sensor.kitchen' in entity_id or 
                                'light.shelly' in entity_id or
                                'automation.' in entity_id):
                                timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                                print_event(timestamp, event_type, data)
                                
                    except (json.JSONDecodeError, KeyError) as e:
                        continue
                        
    except KeyboardInterrupt:
        print("\nMonitoring stopped")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_automation_flow()
