import requests
import json
from datetime import datetime
import time

# Configuration
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

# Button configurations
BUTTONS = {
    'UP': 'binary_sensor.kitchen_panel_up_kpu3',
    'DOWN1': 'binary_sensor.kitchen_panel_dn_kpl3',
    'DOWN2': 'binary_sensor.kitchen_panel_dn_kpld3'
}

# Track button states and timings
button_states = {button: {'last_state': None, 'press_time': None} for button in BUTTONS}

# Set up headers with authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "text/event-stream",
}

def format_duration(seconds):
    """Format duration in seconds to human-readable format."""
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    return f"{seconds:.2f}s"

def monitor_buttons():
    """Monitor specific button states and detect taps/holds."""
    print("Kitchen Button Monitor")
    print("Watching buttons:")
    for name, entity in BUTTONS.items():
        print(f"- {name}: {entity}")
    print("\nPress Ctrl+C to stop\n")
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
                # Only handle SSE data lines
                if not line.startswith(b"data:"):
                    continue
                try:
                        event = json.loads(line[6:])  # Skip 'data: ' prefix
                        if event.get('event_type') != 'state_changed':
                            continue
                            
                        entity_id = event['data'].get('entity_id')
                        if entity_id not in BUTTONS.values():
                            continue
                            
                        # Get button name from entity_id
                        button_name = [name for name, eid in BUTTONS.items() if eid == entity_id][0]
                        new_state = event['data']['new_state']['state']
                        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                        
                        # Handle button state change
                        if new_state == 'on':
                            button_states[button_name]['press_time'] = datetime.now()
                            print(f"\n{timestamp} - {button_name} PRESSED")
                            
                        elif new_state == 'off' and button_states[button_name]['press_time']:
                            release_time = datetime.now()
                            press_duration = (release_time - button_states[button_name]['press_time']).total_seconds()
                            
                            # Determine if tap or hold
                            action = "TAP" if press_duration < 0.4 else "HOLD"
                            
                            print(f"{timestamp} - {button_name} RELEASED after {format_duration(press_duration)} ({action})")
                            print("-" * 60)
                            
                    except (json.JSONDecodeError, KeyError) as e:
                        # Malformed event chunk; ignore
                        continue
                        
    except KeyboardInterrupt:
        print("\nMonitoring stopped")
    except Exception as e:
        print(f"Error: {e}")
        print("Falling back to polling mode (200ms)…")
        poll_buttons()

def poll_buttons(poll_interval=0.2):
    """Fallback: poll button states via REST and detect tap/hold."""
    last_states = {name: None for name in BUTTONS}
    press_times = {name: None for name in BUTTONS}
    print("Polling button states every 200ms (Ctrl+C to stop)…")
    # Initial existence check and current states
    for name, entity in BUTTONS.items():
        try:
            r = requests.get(f"{BASE_URL}/api/states/{entity}", headers=HEADERS, timeout=5)
            status = r.status_code
            curr = r.json().get('state') if status == 200 else 'unknown'
            print(f"- {name} {entity}: {curr} (HTTP {status})")
            last_states[name] = curr if status == 200 else None
        except Exception:
            print(f"- {name} {entity}: unreachable")
    try:
        while True:
            for name, entity in BUTTONS.items():
                try:
                    r = requests.get(f"{BASE_URL}/api/states/{entity}", headers=HEADERS, timeout=5)
                    if r.status_code != 200:
                        continue
                    state = r.json().get('state')
                    prev = last_states[name]
                    if prev != state:
                        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                        if state == 'on':
                            press_times[name] = datetime.now()
                            print(f"\n{timestamp} - {name} PRESSED")
                        elif state == 'off' and press_times[name]:
                            duration = (datetime.now() - press_times[name]).total_seconds()
                            action = "TAP" if duration < 0.4 else "HOLD"
                            print(f"{timestamp} - {name} RELEASED after {format_duration(duration)} ({action})")
                            print("-" * 60)
                            press_times[name] = None
                        last_states[name] = state
                except Exception:
                    pass
            time.sleep(poll_interval)
    except KeyboardInterrupt:
        print("\nPolling stopped")

if __name__ == "__main__":
    monitor_buttons()
