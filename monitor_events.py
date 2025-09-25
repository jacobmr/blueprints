import requests
import json
from datetime import datetime

# Configuration - using the same as before
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

# Set up headers with authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def monitor_events():
    """Monitor Home Assistant events in real-time."""
    print("Starting event monitoring... (Press Ctrl+C to stop)")
    print("-" * 80)
    
    try:
        # First, get the current event stream
        with requests.get(
            f"{BASE_URL}/api/stream",
            headers=HEADERS,
            stream=True,
            timeout=30
        ) as response:
            response.raise_for_status()
            
            print("Connected to Home Assistant event stream")
            print("Listening for events...")
            print("-" * 80)
            
            for line in response.iter_lines():
                if line:
                    try:
                        # Parse the event data
                        event = json.loads(line[6:])  # Skip 'data: ' prefix
                        event_type = event.get('event_type')
                        
                        # Show all state_changed events
                        if event_type == 'state_changed':
                            entity_id = event['data'].get('entity_id', '')
                            print(f"\n{datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
                            print(f"Entity: {entity_id}")
                            print(f"Event type: {event_type}")
                            
                            if 'old_state' in event['data']:
                                old_state = event['data']['old_state']
                                print(f"Old state: {old_state.get('state', 'N/A')}")
                                if 'last_changed' in old_state:
                                    print(f"Old state changed: {old_state['last_changed']}")
                            
                            if 'new_state' in event['data']:
                                new_state = event['data']['new_state']
                                print(f"New state: {new_state.get('state', 'N/A')}")
                                if 'last_changed' in new_state:
                                    print(f"New state changed: {new_state['last_changed']}")
                            
                            # Calculate duration if we have both timestamps
                            if ('old_state' in event['data'] and 'new_state' in event['data'] and
                                'last_changed' in event['data']['old_state'] and
                                'last_changed' in event['data']['new_state']):
                                old_time = datetime.fromisoformat(event['data']['old_state']['last_changed'])
                                new_time = datetime.fromisoformat(event['data']['new_state']['last_changed'])
                                duration = (new_time - old_time).total_seconds() * 1000  # in ms
                                print(f"State duration: {duration:.0f}ms")
                    except json.JSONDecodeError:
                        continue
                    except KeyError as e:
                        print(f"Error parsing event: {e}")
                        
    except KeyboardInterrupt:
        print("\nStopped monitoring events")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_events()
