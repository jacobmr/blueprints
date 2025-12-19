#!/usr/bin/env python3
"""
Monitor light service calls and state changes to debug dimmer issues.
Shows exactly what brightness values are being sent and what the light reports.
"""

import requests
import json
from datetime import datetime
import sys

# Configuration
BASE_URL = "http://192.168.0.22:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def monitor_light_events(target_light=None):
    """
    Monitor light service calls and state changes.
    If target_light is provided, only show events for that light.
    """
    print("=" * 80)
    print("LIGHT DEBUGGING MONITOR")
    print("=" * 80)
    if target_light:
        print(f"Filtering for: {target_light}")
    else:
        print("Showing all light entities")
    print("=" * 80)
    print("\nListening for:")
    print("  - light.turn_on service calls (with brightness values)")
    print("  - light.turn_off service calls")
    print("  - Light state changes (actual reported state)")
    print("\nPress Ctrl+C to stop")
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
                        # Skip 'data: ' prefix and parse JSON
                        if line.startswith(b'data: '):
                            event = json.loads(line[6:])
                        else:
                            continue

                        event_type = event.get('event_type')

                        # Watch for service calls
                        if event_type == 'call_service':
                            domain = event['data'].get('domain', '')
                            service = event['data'].get('service', '')
                            service_data = event['data'].get('service_data', {})

                            if domain == 'light':
                                entity_id = service_data.get('entity_id', '')

                                # Filter if target specified
                                if target_light and target_light not in str(entity_id):
                                    continue

                                timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                                print(f"\n[{timestamp}] 🔧 SERVICE CALL: light.{service}")
                                print(f"  Entity: {entity_id}")

                                if service == 'turn_on':
                                    # Check for brightness
                                    if 'brightness' in service_data:
                                        brightness = service_data['brightness']
                                        brightness_pct = round(brightness / 255 * 100, 1)
                                        print(f"  ✨ Brightness: {brightness}/255 ({brightness_pct}%)")
                                    elif 'brightness_pct' in service_data:
                                        brightness_pct = service_data['brightness_pct']
                                        brightness = round(brightness_pct / 100 * 255)
                                        print(f"  ✨ Brightness: {brightness}/255 ({brightness_pct}%)")
                                    else:
                                        print(f"  ✨ No brightness specified (will use default or last state)")

                                    # Show other parameters
                                    for key in service_data:
                                        if key not in ['entity_id', 'brightness', 'brightness_pct']:
                                            print(f"  {key}: {service_data[key]}")

                                elif service == 'turn_off':
                                    print(f"  🔌 Turning OFF")

                        # Watch for state changes
                        elif event_type == 'state_changed':
                            entity_id = event['data'].get('entity_id', '')

                            # Only show light entities
                            if not entity_id.startswith('light.'):
                                continue

                            # Filter if target specified
                            if target_light and target_light not in entity_id:
                                continue

                            new_state = event['data'].get('new_state', {})
                            old_state = event['data'].get('old_state', {})

                            if new_state:
                                state = new_state.get('state', 'N/A')
                                attributes = new_state.get('attributes', {})

                                timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
                                print(f"\n[{timestamp}] 📊 STATE CHANGE: {entity_id}")
                                print(f"  State: {state}")

                                if 'brightness' in attributes:
                                    brightness = attributes['brightness']
                                    brightness_pct = round(brightness / 255 * 100, 1)
                                    print(f"  💡 Reported Brightness: {brightness}/255 ({brightness_pct}%)")

                                # Show transition from old to new
                                if old_state and old_state.get('state') != state:
                                    old_brightness = old_state.get('attributes', {}).get('brightness')
                                    new_brightness = attributes.get('brightness')

                                    if old_brightness is not None and new_brightness is not None:
                                        old_pct = round(old_brightness / 255 * 100, 1)
                                        new_pct = round(new_brightness / 255 * 100, 1)
                                        print(f"  📈 Changed: {old_pct}% → {new_pct}%")

                    except (json.JSONDecodeError, KeyError) as e:
                        # Skip malformed events
                        continue

    except KeyboardInterrupt:
        print("\n" + "=" * 80)
        print("Monitoring stopped")
        print("=" * 80)
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Connection error: {e}")
        print("\nTroubleshooting:")
        print("  1. Check Home Assistant is running at http://192.168.0.22:8123")
        print("  2. Verify the access token is still valid")
        print("  3. Check network connectivity")

if __name__ == "__main__":
    # Allow filtering by light entity from command line
    target = sys.argv[1] if len(sys.argv) > 1 else None

    if target:
        print(f"\nFiltering for light: {target}")
    else:
        print("\nTip: Run with a light entity ID to filter:")
        print("  python3 monitor_light_debug.py light.your_light_name")

    monitor_light_events(target)
