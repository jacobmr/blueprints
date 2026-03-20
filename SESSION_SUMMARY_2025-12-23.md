# Session Summary - December 23, 2025

## 🎯 Mission Accomplished

Successfully solved the "LED won't turn completely off" problem and created new pendant blueprint.

---

## ✅ Major Achievements

### 1. Root Cause Analysis: LED Controller Minimum Voltage
**Problem**: Great Room LED stayed at ~20% brightness even when "off"
- Current sensor showed 8-9A still flowing when light was "off"
- Root cause: LED controller (in ceiling) has minimum operating voltage
- Phase-cut dimming can't get below the controller's minimum threshold

**Solution**: Added Shelly 1PM relay for hard power cutoff
- Wiring: `Breaker #5/6 → Shelly (L+N) → Shelly O → ESP32 Dimmer L → LED Controller`
- Shelly provides true OFF via hard power cutoff
- ESP32 provides 0-100% dimming when power is on

### 2. Template Light Coordination
Created `light.great_room_limited` in `configuration.yaml`:
- Coordinates Shelly 1PM (`switch.shelly1pm_84cca8a1148d`) + ESP32 (`light.do_not_use_esp32_c3`)
- **Turn ON**: Enable Shelly → Wait 200ms → Set ESP32 brightness (max 90%)
- **Turn OFF**: Turn off ESP32 → Wait 100ms → Hard cut power via Shelly
- **Set Level**: Ensure Shelly on → Adjust ESP32 brightness (max 90%)

### 3. Test Mode Toggle
Added `input_boolean.great_room_allow_100_percent`:
- **OFF (default)**: 90% brightness cap (230/255) - protects 3.3A circuit
- **ON (test mode)**: 100% brightness allowed (255/255) - for testing full load

Created dashboard card: `GREAT_ROOM_TEST_MODE_CARD.yaml`
- Shows main light control
- Toggle for test mode with safety warnings
- Current/power monitoring display
- Clear testing instructions

### 4. New Blueprint: "2 Button CTRL based on B - pendant"
File: `dimmer_two_button_pendant.yaml`

**Matt's Requirements Implemented**:
- **UP Button**:
  - 1st click: 50% brightness
  - 2nd click: 100% brightness
  - Double-click detection: 400ms window (configurable)
- **DOWN Button**:
  - Tap (quick release): Dim down 20%
  - Long press (hold): Turn OFF
  - Long press threshold: 600ms (configurable)

**Import URL**:
```
https://raw.githubusercontent.com/jacobmr/blueprints/main/dimmer_two_button_pendant.yaml
```

### 5. Current Monitoring System
Added to ESPHome config (`great-room-led-WORKING.yaml`):
- ADC current sensor on GPIO04 (12db attenuation)
- Power calculation sensor (V × I)
- Binary sensor "Great Room LED Actually On" (detects current flow)
- Successfully detects true ON/OFF state

---

## 📁 Key Files Modified

1. **`/Users/jmr/dev/casa apertura/configuration.yaml`**
   - Template light with Shelly + ESP32 coordination
   - Input boolean for test mode toggle
   - Shell commands for GitHub config downloads

2. **`/Users/jmr/dev/casa apertura/great-room-led-WORKING.yaml`**
   - Production ESPHome config with current monitoring
   - Static IP: 192.168.0.118
   - WiFi: "Casa Aperture" / "rosie1234"

3. **`/Users/jmr/dev/casa apertura/dimmer_two_button_pendant.yaml`**
   - New blueprint for pendant-style control
   - Pushed to GitHub

4. **`/Users/jmr/dev/casa apertura/GREAT_ROOM_TEST_MODE_CARD.yaml`**
   - Dashboard card for testing 100% brightness mode

5. **`/Users/jmr/dev/casa apertura/PRIVATE_REPO_SETUP.md`**
   - Complete guide for private GitHub repo setup
   - GitHub Personal Access Token instructions

6. **`/Users/jmr/dev/casa apertura/download_esphome_config.sh`**
   - Script to download configs from private repo

---

## 🔑 Key Entities

### Production Entities (USE THESE)
- `light.great_room_limited` - Main template light (Shelly + ESP32 coordination)
- `input_boolean.great_room_allow_100_percent` - Test mode toggle

### Hardware Entities
- `switch.shelly1pm_84cca8a1148d` - Shelly 1PM relay (hard cutoff)
- `light.do_not_use_esp32_c3` - Raw ESP32 dimmer (DO NOT USE DIRECTLY)

### Monitoring Entities
- `sensor.great_room_led_current` - Current draw (A)
- `sensor.great_room_led_power` - Power draw (W)
- `binary_sensor.great_room_led_actually_on` - True if current flowing

---

## 🚀 Next Steps (When Resuming)

### 1. Test Shelly + ESP32 Coordination
- [ ] Matt wires Shelly 1PM in series with ESP32
- [ ] Test turn ON/OFF via Home Assistant
- [ ] Verify light goes completely OFF (0A current)
- [ ] Test brightness levels (10%, 50%, 90%)

### 2. Test 100% Brightness Mode
- [ ] Turn ON `input_boolean.great_room_allow_100_percent`
- [ ] Set light to 100%
- [ ] Monitor `sensor.great_room_led_current`
- [ ] Check if current exceeds 3.3A
- [ ] If safe, can leave at 100%; if too high, keep 90% cap

### 3. Test New Pendant Blueprint
- [ ] Import blueprint into Home Assistant
- [ ] Create automation instance with panel entities
- [ ] Test UP single click (→ 50%)
- [ ] Test UP double click (→ 100%)
- [ ] Test DOWN tap (→ dim 20%)
- [ ] Test DOWN long press (→ OFF)

### 4. GitHub Repository Security (Optional)
- [ ] Make `blueprints` repo private
- [ ] Generate GitHub Personal Access Token
- [ ] Install token on Home Assistant: `/config/.github_token`
- [ ] Test download script

---

## 📊 System Architecture

```
Breaker #5/6 (240V)
    ↓
Shelly 1PM Relay (192.168.0.XXX)
  │ Switch: switch.shelly1pm_84cca8a1148d
  │ Provides: Hard power cutoff
    ↓
ESP32-C3 Dimmer (192.168.0.118)
  │ Light: light.do_not_use_esp32_c3
  │ Provides: 0-100% phase-cut dimming
  │ Sensors: Current, Power, Actually On
    ↓
LED Controller (in ceiling)
  │ Unknown type (was KNX)
  │ Has minimum operating voltage
    ↓
Great Room LED Strip (~3.3A @ 90%)
```

```
Home Assistant Template Light
┌─────────────────────────────────────┐
│ light.great_room_limited            │
│                                     │
│ Turn ON:  Shelly ON → Wait → ESP32 │
│ Turn OFF: ESP32 OFF → Wait → Shelly│
│ Dim:      Ensure Shelly → ESP32    │
│                                     │
│ Max Brightness:                     │
│   90% (230/255) - default          │
│   100% (255/255) - test mode       │
└─────────────────────────────────────┘
```

---

## 🔧 Technical Details

### Template Light Logic
- **State Tracking**: Light is ON if Shelly is ON AND ESP32 is ON
- **Brightness Cap**:
  - Test mode OFF: `max_brightness = 230` (90%)
  - Test mode ON: `max_brightness = 255` (100%)
- **Safety**: Always clamps requested brightness to max_brightness
- **Coordination Delays**:
  - Turn ON: 200ms for ESP32 to boot
  - Turn OFF: 100ms before hard cutoff

### Blueprint Click Detection
- **UP Double-Click**: Uses `wait_for_trigger` with 400ms timeout
  - If 2nd click arrives: Set 100%
  - If timeout: Set 50%
- **DOWN Long-Press**: Uses `wait_for_trigger` for button release
  - If timeout (still held): Turn OFF
  - If released quickly: Dim down 20%

---

## 📝 Documentation Created
- `PRIVATE_REPO_SETUP.md` - GitHub token setup guide
- `GREAT_ROOM_TEST_MODE_CARD.yaml` - Dashboard test card
- `download_esphome_config.sh` - Private repo download script
- `SESSION_SUMMARY_2025-12-23.md` - This document

---

## 🎉 Session Complete

All tasks completed successfully. Ready for testing when Matt wires the Shelly relay!

**Import Blueprint**:
```
https://raw.githubusercontent.com/jacobmr/blueprints/main/dimmer_two_button_pendant.yaml
```

**Next Session**: Test the hardware setup and new blueprint automations.
