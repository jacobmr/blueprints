# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Home Assistant automation project for controlling dimmable lights using dual button input from ESPHome binary sensors. The project implements a blueprint-based automation that distinguishes between single-click and double-click gestures on UP/DOWN buttons to provide fine-grained dimmer control.

**Project Name**: casa apertura (Home Assistant Dimmer Control)

## Home Assistant Configuration

- **Base URL**: http://192.168.0.22:8123 (updated 2025-12-12)
  - _Historical IP_: 172.28.133.210 (may appear in older scripts)
- **Authentication**: Uses long-lived access token stored in Python monitoring scripts
- **Target Devices**:
  - UP Button: `binary_sensor.kitchen_panel_up_kpu3`
  - DOWN Button: `binary_sensor.kitchen_panel_dn_kpl3`
  - Target Light: `light.shellyprodm2pm_a0dd6c9e5f08_light_0`

## Architecture

### Blueprint System (`dimmer_two_button.yaml`)

The core automation is implemented as a Home Assistant blueprint that:
- Listens for state changes on two binary sensors (UP/DOWN buttons)
- Implements double-click detection using `wait_for_trigger` with configurable timeout (default 400ms)
- Uses `mode: single` with `max_exceeded: silent` to prevent overlapping executions

**Button Behavior**:
- **UP Single Click**: Turn on to 50% if off, increase by brightness_step% if on
- **UP Double Click**: Set brightness to 100%
- **DOWN Single Click**: Turn on to 20% if off, decrease by brightness_step% if on
- **DOWN Double Click**: Turn light off

**Key Design Decisions**:
- Click detection happens at button press (`to: 'on'`), not release
- Double-click window is configurable (default 400ms)
- Brightness calculations handle edge cases (min/max clamping)
- Uses Jinja2 templates for brightness math: `(state_attr(target_light, 'brightness') | int(0) / 255 * 100)`

### Automation Instance (`kitchen_dimmer_automation.yaml`)

References the blueprint with specific entity bindings for the kitchen installation.

## Development Tools

### Python Monitoring Scripts

All scripts use the Home Assistant REST API and WebSocket streaming API for real-time monitoring:

- **`monitor_kitchen_buttons.py`**: Real-time button event monitor
  - Tracks UP/DOWN button presses with duration measurement
  - Distinguishes TAP (<400ms) vs HOLD (>=400ms)
  - Falls back to 200ms polling if streaming fails
  - Primary tool for debugging button behavior

- **`dump_ha_entities.py`**: Export all HA entities to CSV
  - Useful for discovering entity IDs
  - Output: `~/ha_entities_export.csv` (371 entities exported)

- **`monitor_events.py`**: Generic HA event stream monitor
  - Displays all Home Assistant events in real-time

- **`test_button_press.py`**: Simulate button press events
  - Send synthetic `state_changed` events to test automations
  - Configurable press duration for testing tap vs hold

### Testing

Run the button monitor while physically testing:
```bash
python3 monitor_kitchen_buttons.py
```

Expected output format:
```
14:23:45.123 - UP PRESSED
14:23:45.321 - UP RELEASED after 198ms (TAP)
```

## Common Development Workflows

### Debugging Button Issues

1. Start the monitor: `python3 monitor_kitchen_buttons.py`
2. Physical test: Press buttons on the ESPHome device
3. Verify events are firing with correct timing
4. Check if TAP/HOLD classification matches expected behavior

### Testing Blueprint Changes

1. Edit `dimmer_two_button.yaml`
2. Reload automations in Home Assistant (Developer Tools > YAML > Automations)
3. Test with `python3 monitor_kitchen_buttons.py` running
4. Monitor Home Assistant logs for errors: Developer Tools > Logs

### Blueprint Development Guidelines

- Always use `!input` for configurable parameters
- Entity selectors should specify domain for type safety
- Use `mode: single` with `max_exceeded: silent` to prevent race conditions
- Brightness calculations must handle light off state: `{% if is_state(target_light, 'off') %}`
- Include source_url pointing to GitHub repo for blueprint sharing

## Project Evolution

**Original Design (prd.md)**: Tap vs hold with continuous dimming loops
- Tap: brightness step
- Hold: start dimming_loop script

**Current Design**: Single/double click detection
- More reliable than duration-based detection
- Eliminates need for external dimming_loop scripts
- Better user experience for discrete brightness control

**Key Change**: Switched from `event_type: state_changed` triggers to `platform: state` triggers with `to: 'on'` for cleaner event handling.

## Files Not in Use

- `script_dimming_loop.yaml`: Deprecated continuous dimming approach
- `test_button_press.yaml`: Old YAML-based test automation
- `simple_button_test.yaml`: Early prototype
- `debug_light_state.yaml`: One-off debugging automation

These files remain for reference but are not part of the active system.

## ESP32 Device Management

**📁 COMPLETE DOCUMENTATION**: See **ESP32_COMPLETE_DOCUMENTATION.md** for:
- Full system overview (2 independent ESP32 systems)
- 7 panel devices + 96-channel dimmer system
- Configuration file locations and backups
- Complete action plan for deployment
- 26 blueprint automations to create
- Troubleshooting guides

**📋 Quick Inventory**: See **ESP32_INVENTORY.md** for device entity listing

## Important Notes

- The blueprint is designed to work with any dimmable light + binary sensor pair
- ESPHome button sensors must report `on` when pressed, `off` when released
- Home Assistant WebSocket API may timeout; scripts include polling fallbacks
- Token in scripts expires: 2073155912 (Unix timestamp)
- **Current Issue**: All ESP32 panels showing as unavailable - need to bring devices online
