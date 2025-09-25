import os
import json
import time
from datetime import datetime
import requests

# Home Assistant connection
BASE_URL = "http://172.28.133.210:8123"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMTk3YjM4NGVlNzk0ZjdjODBjY2U5MTkyZjJjZmNhZCIsImlhdCI6MTc1Nzc5NTkxMiwiZXhwIjoyMDczMTU1OTEyfQ.D8tR8X-ZwfzcotfAOBo9l5FgeTLUzyY06-tkTMEg1o8"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "text/event-stream",
}

# What to log
BUTTON_KEYWORDS = os.getenv("HA_BUTTON_FILTERS", "button,panel,kpu,kpl").split(",")
SCRIPT_ENTITY = "script.dimming_loop"

LOG_FILE = os.path.join(os.path.dirname(__file__), "salida.out")


def now_ts():
    return datetime.now().strftime('%H:%M:%S.%f')[:-3]


def log(line: str):
    ts_line = f"{now_ts()} {line}"
    print(ts_line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(ts_line + "\n")


def discover_button_entities():
    try:
        r = requests.get(f"{BASE_URL}/api/states", headers=HEADERS, timeout=20)
        r.raise_for_status()
        entities = r.json()
    except Exception as e:
        log(f"ERROR discovering entities: {e}")
        return []

    def is_button_like(eid: str, attrs: dict):
        if not eid.startswith("binary_sensor."):
            return False
        name = eid.lower()
        if any(kw for kw in BUTTON_KEYWORDS if kw and kw.lower() in name):
            return True
        # Fallback: ESPHome often exposes buttons as binary_sensor without device_class
        dev_class = (attrs or {}).get("device_class", "").lower()
        return dev_class == "button"

    button_ids = []
    for e in entities:
        eid = e.get("entity_id", "")
        attrs = e.get("attributes", {})
        if is_button_like(eid, attrs):
            button_ids.append(eid)

    return sorted(set(button_ids))


def stream_events(monitored_buttons):
    # Track press durations
    press_times = {eid: None for eid in monitored_buttons}

    log("Starting SSE event stream…")
    try:
        with requests.get(
            f"{BASE_URL}/api/stream",
            headers=HEADERS,
            stream=True,
            timeout=(10, 600),
        ) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line:
                    continue
                if not line.startswith(b"data:"):
                    continue
                try:
                    event = json.loads(line[6:])
                except Exception:
                    continue

                if event.get("event_type") != "state_changed":
                    continue
                data = event.get("data", {})
                eid = data.get("entity_id", "")

                if eid == SCRIPT_ENTITY:
                    old_s = (data.get("old_state") or {}).get("state")
                    new_s = (data.get("new_state") or {}).get("state")
                    log(f"{SCRIPT_ENTITY}: {old_s} -> {new_s}")
                    continue

                if eid not in monitored_buttons:
                    continue

                new_state = (data.get("new_state") or {}).get("state")
                if new_state == "on":
                    press_times[eid] = datetime.now()
                    log(f"{eid} PRESSED")
                elif new_state == "off" and press_times[eid]:
                    duration = (datetime.now() - press_times[eid]).total_seconds()
                    action = "TAP" if duration < 0.4 else "HOLD"
                    log(f"{eid} RELEASED after {duration*1000:.0f}ms ({action})")
                    press_times[eid] = None
    except Exception as e:
        log(f"SSE error: {e}")
        raise


def poll_events(monitored_buttons, interval=0.2):
    log("Falling back to polling mode…")
    last_states = {eid: None for eid in monitored_buttons}
    press_times = {eid: None for eid in monitored_buttons}

    # Also poll the dimming loop script
    last_script = None

    # Initial snapshot
    for eid in monitored_buttons:
        try:
            r = requests.get(f"{BASE_URL}/api/states/{eid}", headers=HEADERS, timeout=8)
            if r.status_code == 200:
                last_states[eid] = r.json().get("state")
                log(f"Init: {eid} = {last_states[eid]}")
        except Exception:
            pass

    try:
        while True:
            # Buttons
            for eid in monitored_buttons:
                try:
                    r = requests.get(f"{BASE_URL}/api/states/{eid}", headers=HEADERS, timeout=8)
                    if r.status_code != 200:
                        continue
                    state = r.json().get("state")
                    prev = last_states[eid]
                    if state != prev:
                        if state == "on":
                            press_times[eid] = datetime.now()
                            log(f"{eid} PRESSED")
                        elif state == "off" and press_times[eid]:
                            duration = (datetime.now() - press_times[eid]).total_seconds()
                            action = "TAP" if duration < 0.4 else "HOLD"
                            log(f"{eid} RELEASED after {duration*1000:.0f}ms ({action})")
                            press_times[eid] = None
                        last_states[eid] = state
                except Exception:
                    pass

            # Script
            try:
                r = requests.get(f"{BASE_URL}/api/states/{SCRIPT_ENTITY}", headers=HEADERS, timeout=8)
                if r.status_code == 200:
                    s = r.json().get("state")
                    if s != last_script:
                        log(f"{SCRIPT_ENTITY}: {last_script} -> {s}")
                        last_script = s
            except Exception:
                pass

            time.sleep(interval)
    except KeyboardInterrupt:
        log("Polling stopped by user")


def main():
    log("Discovering button-like entities…")
    buttons = discover_button_entities()
    if not buttons:
        log("No button-like entities found. Adjust HA_BUTTON_FILTERS if needed.")
    else:
        log(f"Monitoring {len(buttons)} button entities:")
        for eid in buttons:
            log(f"- {eid}")

    # Try SSE first, then fallback to polling
    try:
        stream_events(buttons)
    except Exception:
        poll_events(buttons)


if __name__ == "__main__":
    main()

