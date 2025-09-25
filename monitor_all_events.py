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
    "Accept": "text/event-stream",
}

INTERESTING_PREFIXES = (
    'binary_sensor.',
    'light.',
    'automation.',
    'script.dimming_loop',
)

def monitor_events():
    print("Home Assistant Event Monitor (filtered)")
    print("Showing state_changed for binary_sensor/light/automation/script.dimming_loop")
    print("-" * 80)
    
    try:
        with requests.get(
            f"{BASE_URL}/api/stream",
            headers=HEADERS,
            stream=True,
            timeout=(10, 600)
        ) as response:
            response.raise_for_status()
            
            for line in response.iter_lines():
                if not line:
                    continue
                if not line.startswith(b"data:"):
                    continue
                try:
                    event = json.loads(line[6:])
                    if event.get('event_type') != 'state_changed':
                        continue
                    data = event.get('data', {})
                    entity_id = data.get('entity_id', '')
                    if not entity_id.startswith(INTERESTING_PREFIXES):
                        continue
                    timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                    old_state = data.get('old_state', {}).get('state') if data.get('old_state') else None
                    new_state = data.get('new_state', {}).get('state') if data.get('new_state') else None
                    print(f"{timestamp} {entity_id}: {old_state} -> {new_state}")
                except Exception:
                    continue
                        
    except KeyboardInterrupt:
        print("\nMonitoring stopped")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    monitor_events()
