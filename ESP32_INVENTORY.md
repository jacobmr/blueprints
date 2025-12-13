# ESP32 Device Inventory - Casa Apertura
**Last Updated**: 2025-12-12
**Home Assistant**: http://192.168.0.22:8123

## Summary
- **Total Custom ESP32 Panels**: 7 devices
- **Total Button Entities**: 51 binary sensors
- **Current Status**: All devices showing as **UNAVAILABLE** in Home Assistant
- **ESPHome Integration**: Installed and loaded in HA

## Registered Devices in Home Assistant

### 1. Dining Room Light Panel
- **Device Name**: `dining_room_light_panel`
- **Status**: Unavailable
- **Button Count**: 8 (4 UP + 4 DOWN)
- **Entities**:
  - `binary_sensor.dining_room_light_panel_dr1` - 1 - UP - Dining Sideboard
  - `binary_sensor.dining_room_light_panel_dr2` - 2 - UP - Dining Pendant
  - `binary_sensor.dining_room_light_panel_dr3` - 3 - UP - Great Room Cans
  - `binary_sensor.dining_room_light_panel_dr4` - 4 - UP - Great Room Box Lights
  - `binary_sensor.dining_room_light_panel_dr1d` - 1 - DN - Dining Sideboard
  - `binary_sensor.dining_room_light_panel_dr2d` - 2 - DN - Dining Pendant
  - `binary_sensor.dining_room_light_panel_dr3d` - 3 - DN - Great Room Cans
  - `binary_sensor.dining_room_light_panel_dr4d` - 4 - DN - Great Room Box Lights

### 2. Kitchen Panel (DOWN)
- **Device Name**: `kitchen_panel_dn`
- **Status**: Unavailable
- **Button Count**: 6 buttons
- **Entities**:
  - `binary_sensor.kitchen_panel_dn_kpl1` - 1- Courtyard ON/OFF
  - `binary_sensor.kitchen_panel_dn_kpl2` - 2 - UP - Great Room LED
  - `binary_sensor.kitchen_panel_dn_kpl3` - 3 - UP - Banquette Pendant ⭐ (Used in dimmer automation)
  - `binary_sensor.kitchen_panel_dn_kpl4` - 4 - Pool Planter
  - `binary_sensor.kitchen_panel_dn_kpld2` - 2 - DN - Great Room LED
  - `binary_sensor.kitchen_panel_dn_kpld3` - 3 - DN - Banquette Pendant

### 3. Kitchen Panel (UP)
- **Device Name**: `kitchen_panel_up`
- **Status**: Unavailable
- **Button Count**: 8 (4 UP + 4 DOWN)
- **Entities**:
  - `binary_sensor.kitchen_panel_up_kpu1` - 2 - UP - Kitchen Cans
  - `binary_sensor.kitchen_panel_up_kpu2` - 1 - UP - Main Hallway
  - `binary_sensor.kitchen_panel_up_kpu3` - 3 - UP - Isla ⭐ (Used in dimmer automation)
  - `binary_sensor.kitchen_panel_up_kpu4` - 4 - UP - Kitchen Box Lights
  - `binary_sensor.kitchen_panel_up_kpud1` - 2 - DN - Kitchen Cans
  - `binary_sensor.kitchen_panel_up_kpud2` - 1 - DN - Main Hallway
  - `binary_sensor.kitchen_panel_up_kpud3` - 3 - DN - Isla
  - `binary_sensor.kitchen_panel_up_kpud4` - 4 - DN - Kitchen Box Lights

### 4. Master Panel
- **Device Name**: `master_panel`
- **Status**: Unavailable
- **Button Count**: 8 buttons
- **Entities**:
  - `binary_sensor.master_panel_mstr1` - Master 3 UP
  - `binary_sensor.master_panel_mstr2` - Master 1 Up
  - `binary_sensor.master_panel_mstr3` - Master 3 DN
  - `binary_sensor.master_panel_mstr4` - Master 1 Down
  - `binary_sensor.master_panel_mstr1d`
  - `binary_sensor.master_panel_mstr2d`
  - `binary_sensor.master_panel_mstr3d`
  - `binary_sensor.master_panel_mstr4d`

### 5. Nine Panel
- **Device Name**: `nine_panel`
- **Status**: Unavailable
- **Button Count**: 5 buttons
- **Entities**:
  - `binary_sensor.nine_panel_nine1` - 1 - UP - Terrace Ceiling One
  - `binary_sensor.nine_panel_nine2` - 1 - UP - Outdoor Dining Lights
  - `binary_sensor.nine_panel_nine3` - Outdoor Bench LED
  - `binary_sensor.nine_panel_nine5` - 1 - DN - Terrace Ceiling One
  - `binary_sensor.nine_panel_nine6` - 1 - DN - Outdoor Dining Lights

### 6. Other Nine Panel
- **Device Name**: `other_nine_panel`
- **Status**: Unavailable
- **Button Count**: 8 buttons
- **Entities**:
  - `binary_sensor.other_nine_panel_nine1`
  - `binary_sensor.other_nine_panel_nine2`
  - `binary_sensor.other_nine_panel_nine3`
  - `binary_sensor.other_nine_panel_nine4`
  - `binary_sensor.other_nine_panel_nine5`
  - `binary_sensor.other_nine_panel_nine6`
  - `binary_sensor.other_nine_panel_nine7`
  - `binary_sensor.other_nine_panel_nine8`

### 7. Terrace Panel
- **Device Name**: `terrace_panel`
- **Status**: Unavailable
- **Button Count**: 8 (4 UP + 4 DOWN)
- **Entities**:
  - `binary_sensor.terrace_panel_terr1`
  - `binary_sensor.terrace_panel_terr2`
  - `binary_sensor.terrace_panel_terr3`
  - `binary_sensor.terrace_panel_terr4`
  - `binary_sensor.terrace_panel_terr1d`
  - `binary_sensor.terrace_panel_terr2d`
  - `binary_sensor.terrace_panel_terr3d`
  - `binary_sensor.terrace_panel_terr4d`

## Device Naming Pattern Analysis

The devices follow a clear naming convention:
- **Panel Name**: Location identifier (e.g., `kitchen_panel_up`, `dining_room_light_panel`)
- **Button Naming**: `{panel}_{button_id}` where button_id indicates:
  - UP buttons: `kpu1`, `kpu2`, `dr1`, `dr2`, etc.
  - DOWN buttons: `kpud1`, `kpld3`, `dr1d`, `terr1d`, etc.
  - Pattern: Add `d` suffix for DOWN button variant

## Next Steps Required

### Immediate Actions Needed:

1. **Locate ESPHome Configuration Files**
   - Access HA via web UI → ESPHome Dashboard
   - Or SSH into HA and navigate to `/config/esphome/`
   - Download/backup all `.yaml` config files

2. **Determine Device Network Status**
   - Are devices powered on?
   - Check physical network connections
   - Scan local network for ESP32 devices

3. **Review Firmware Versions**
   - Check ESPHome dashboard for installed versions
   - Determine if OTA updates needed

4. **Identify Missing Devices**
   - We expect 6-10 total devices
   - Currently have 7 in HA
   - Are there 2-3 more that need to be flashed/added?

### Questions to Answer:

1. **Physical Status**:
   - Are these panels physically installed and powered?
   - Do they have known IP addresses?
   - Are they on WiFi or wired?

2. **Configuration Backup**:
   - Where are the ESPHome YAML configs stored?
   - Do we have a backup of firmware configs?

3. **Unregistered Devices**:
   - Do you have ESP32s that haven't been flashed yet?
   - If yes, how many and what are they for?

## Access Methods

### Through Home Assistant Web UI
1. Navigate to http://192.168.0.22:8123
2. Go to Settings → Add-ons → ESPHome
3. View dashboard to see:
   - Device online/offline status
   - IP addresses
   - Firmware versions
   - Configuration files

### Through HA SSH Addon
1. Access Terminal addon in HA
2. Navigate to `/config/esphome/`
3. List configs: `ls -la /config/esphome/*.yaml`

### Through ESPHome Web Interface
- If ESPHome dashboard addon is installed
- Access via HA sidebar → ESPHome

## Automation Integration

Currently using in `kitchen_dimmer_automation.yaml`:
- UP Button: `binary_sensor.kitchen_panel_up_kpu3`
- DOWN Button: `binary_sensor.kitchen_panel_dn_kpl3`
- Target Light: `light.shellyprodm2pm_a0dd6c9e5f08_light_0`

**Note**: These sensors are currently unavailable, so automation won't work until devices are online.

## Recommended Documentation

Once configs are accessible, document for each device:
- Hardware model (ESP32, ESP8266, variant)
- GPIO pin mapping for buttons
- WiFi configuration method
- OTA update credentials
- Physical location in house
- Installation date / firmware version
