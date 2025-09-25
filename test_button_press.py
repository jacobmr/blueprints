import requests
import time
from datetime import datetime

# Configuration - using the same as before
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

# Set up headers with authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def simulate_button_press(button_entity, press_duration=0.3):
    """Simulate a button press with the specified duration in seconds."""
    try:
        # Press the button (turn on)
        print(f"Pressing {button_entity}...")
        requests.post(
            f"{BASE_URL}/api/events/state_changed",
            headers=HEADERS,
            json={
                "entity_id": button_entity,
                "old_state": {"state": "off", "last_changed": datetime.now().isoformat()},
                "new_state": {"state": "on", "last_changed": (datetime.now().isoformat())}
            },
            timeout=5
        )
        
        # Hold for the specified duration
        time.sleep(press_duration)
        
        # Release the button (turn off)
        print(f"Releasing {button_entity} after {press_duration:.1f}s...")
        requests.post(
            f"{BASE_URL}/api/events/state_changed",
            headers=HEADERS,
            json={
                "entity_id": button_entity,
                "old_state": {"state": "on", "last_changed": datetime.now().isoformat()},
                "new_state": {"state": "off", "last_changed": (datetime.now().isoformat())}
            },
            timeout=5
        )
        
        print(f"✓ Simulated {press_duration:.1f}s press on {button_entity}")
        return True
        
    except Exception as e:
        print(f"Error simulating button press: {e}")
        return False

def main():
    # Replace these with your actual button entities
    UP_BUTTON = "binary_sensor.dimmer_up_button"
    DOWN_BUTTON = "binary_sensor.dimmer_down_button"
    
    print("Button Press Simulator")
    print("1. Short press (tap)")
    print("2. Long press (hold)")
    print("3. Test both buttons")
    print("0. Exit")
    
    while True:
        choice = input("\nSelect an option (0-3): ")
        
        if choice == '0':
            break
            
        elif choice == '1':
            # Test short press (300ms - should trigger tap)
            simulate_button_press(UP_BUTTON, 0.3)
            
        elif choice == '2':
            # Test long press (1.5s - should trigger hold)
            simulate_button_press(UP_BUTTON, 1.5)
            
        elif choice == '3':
            # Test both buttons with different durations
            print("\nTesting UP button (short press - tap)")
            simulate_button_press(UP_BUTTON, 0.3)
            
            time.sleep(1)  # Small delay between tests
            
            print("\nTesting DOWN button (long press - hold)")
            simulate_button_press(DOWN_BUTTON, 1.5)
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
