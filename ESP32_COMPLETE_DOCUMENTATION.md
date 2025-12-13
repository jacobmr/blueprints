# ESP32 Complete System Documentation
**Project**: Casa Apertura Lighting & Automation
**Last Updated**: 2025-12-12
**Home Assistant**: http://192.168.0.22:8123

---

## Table of Contents
1. [System Overview](#system-overview)
2. [Device Inventory](#device-inventory)
3. [Configuration Files](#configuration-files)
4. [Network & Connectivity](#network--connectivity)
5. [Blueprint Automation System](#blueprint-automation-system)
6. [Action Plan](#action-plan)

---

## System Overview

### Two Independent ESP32 Systems

#### System 1: 96-Channel Dimmer System (General Lighting)
- **Location**: `/Users/jmr/dev/esp_project/`
- **Purpose**: Whole-house dimmable and on/off lighting control
- **Devices**: 7 ESP32 boards controlling 96 lighting zones
- **Status**: Configuration files located, deployment status unknown
- **Integration**: Home Assistant via ESPHome API

#### System 2: Panel Control System (Wall Switch Panels)
- **Location**: Configs likely on HA server at `/config/esphome/`
- **Purpose**: Wall-mounted control panels for room-specific lighting
- **Devices**: 7 panel devices with 51 button entities
- **Status**: All currently UNAVAILABLE (offline)
- **Integration**: Home Assistant via ESPHome API

---

## Device Inventory

### Panel Control Devices (Currently Offline)

| Panel Name | Device Name in HA | Buttons | Location | Status |
|------------|-------------------|---------|----------|--------|
| 1 | `dining_room_light_panel` | 8 (4 UP/4 DOWN) | Dining Room | Offline |
| 2 | `kitchen_panel_up` | 8 (4 UP/4 DOWN) | Kitchen (Upper) | Offline |
| 3 | `kitchen_panel_dn` | 6 buttons | Kitchen (Lower) | Offline |
| 4 | `master_panel` | 8 buttons | Master Bedroom | Offline |
| 5 | `nine_panel` | 5 buttons | Terrace/Outdoor | Offline |
| 6 | `other_nine_panel` | 8 buttons | TBD | Offline |
| 7 | `terrace_panel` | 8 buttons | Terrace | Offline |

**Total**: 7 panels, 51 button entities

### Panel Button Details

#### Dining Room Light Panel (8 buttons)
- `binary_sensor.dining_room_light_panel_dr1` - 1 - UP - Dining Sideboard
- `binary_sensor.dining_room_light_panel_dr2` - 2 - UP - Dining Pendant
- `binary_sensor.dining_room_light_panel_dr3` - 3 - UP - Great Room Cans
- `binary_sensor.dining_room_light_panel_dr4` - 4 - UP - Great Room Box Lights
- `binary_sensor.dining_room_light_panel_dr1d` - 1 - DN - Dining Sideboard
- `binary_sensor.dining_room_light_panel_dr2d` - 2 - DN - Dining Pendant
- `binary_sensor.dining_room_light_panel_dr3d` - 3 - DN - Great Room Cans
- `binary_sensor.dining_room_light_panel_dr4d` - 4 - DN - Great Room Box Lights

#### Kitchen Panel UP (8 buttons)
- `binary_sensor.kitchen_panel_up_kpu1` - 2 - UP - Kitchen Cans
- `binary_sensor.kitchen_panel_up_kpu2` - 1 - UP - Main Hallway
- `binary_sensor.kitchen_panel_up_kpu3` - 3 - UP - Isla ⭐ **Used in dimmer automation**
- `binary_sensor.kitchen_panel_up_kpu4` - 4 - UP - Kitchen Box Lights
- `binary_sensor.kitchen_panel_up_kpud1` - 2 - DN - Kitchen Cans
- `binary_sensor.kitchen_panel_up_kpud2` - 1 - DN - Main Hallway
- `binary_sensor.kitchen_panel_up_kpud3` - 3 - DN - Isla
- `binary_sensor.kitchen_panel_up_kpud4` - 4 - DN - Kitchen Box Lights

#### Kitchen Panel DOWN (6 buttons)
- `binary_sensor.kitchen_panel_dn_kpl1` - 1- Courtyard ON/OFF
- `binary_sensor.kitchen_panel_dn_kpl2` - 2 - UP - Great Room LED
- `binary_sensor.kitchen_panel_dn_kpl3` - 3 - UP - Banquette Pendant ⭐ **Used in dimmer automation**
- `binary_sensor.kitchen_panel_dn_kpl4` - 4 - Pool Planter
- `binary_sensor.kitchen_panel_dn_kpld2` - 2 - DN - Great Room LED
- `binary_sensor.kitchen_panel_dn_kpld3` - 3 - DN - Banquette Pendant

#### Master Panel (8 buttons)
- `binary_sensor.master_panel_mstr1` - Master 3 UP
- `binary_sensor.master_panel_mstr2` - Master 1 Up
- `binary_sensor.master_panel_mstr3` - Master 3 DN
- `binary_sensor.master_panel_mstr4` - Master 1 Down
- `binary_sensor.master_panel_mstr1d` - Master-Panel MSTR1D
- `binary_sensor.master_panel_mstr2d` - Master-Panel MSTR2D
- `binary_sensor.master_panel_mstr3d` - Master-Panel MSTR3D
- `binary_sensor.master_panel_mstr4d` - Master-Panel MSTR4D

#### Nine Panel (5 buttons)
- `binary_sensor.nine_panel_nine1` - 1 - UP - Terrace Ceiling One
- `binary_sensor.nine_panel_nine2` - 1 - UP - Outdoor Dining Lights
- `binary_sensor.nine_panel_nine3` - Outdoor Bench LED
- `binary_sensor.nine_panel_nine5` - 1 - DN - Terrace Ceiling One
- `binary_sensor.nine_panel_nine6` - 1 - DN - Outdoor Dining Lights

#### Other Nine Panel (8 buttons)
- `binary_sensor.other_nine_panel_nine1` through `nine8`
- (Labels need to be configured in HA)

#### Terrace Panel (8 buttons)
- `binary_sensor.terrace_panel_terr1` through `terr4`
- `binary_sensor.terrace_panel_terr1d` through `terr4d`
- (Labels need to be configured in HA)

### 96-Channel Dimmer System Devices

| Board | Device Name | Channels | Hardware | Config File |
|-------|-------------|----------|----------|-------------|
| 1 | `dimmerboard1` | 1-16 (Dimmable) | ESP32-S3 + MCP23017 | DimmerBoard1.yaml |
| 2 | `dimmerboard2` | 17-32 (Dimmable) | ESP32-S3 + MCP23017 | DimmerBoard2.yaml |
| 3 | `dimmerboard3` | 33-48 (Dimmable) | ESP32-S3 + MCP23017 | DimmerBoard3.yaml |
| 4 | `dimmerboard4` | 49-64 (Dimmable) | ESP32-S3 + MCP23017 | DimmerBoard4.yaml |
| 5 | `dimmerboard5` | 65-80 (Dimmable) | ESP32-S3 + MCP23017 | DimmerBoard5.yaml |
| 6 | `onoffboard6` | 81-96 (On/Off) | ESP32 + PCF8574 | OnOffBoard6.yaml |
| 7 | `onoffboard7` | Future expansion | ESP32 + PCF8574 | OnOffBoard7.yaml |

**Total**: 96 independently controlled lighting zones

---

## Configuration Files

### Panel Configs
- **Location**: Likely at `/config/esphome/` on Home Assistant server
- **Access Method**: HA Web UI → ESPHome Dashboard
- **File Names**: Unknown (need to access HA ESPHome dashboard)
- **Backup Status**: ❌ Need to download/backup configs

### Dimmer System Configs
- **Location**: `/Users/jmr/dev/esp_project/`
- **Backup Status**: ✅ Locally backed up
- **Key Files**:
  - `DimmerBoard1.yaml` through `DimmerBoard5.yaml` - Dimmer boards
  - `OnOffBoard6.yaml`, `OnOffBoard7.yaml` - On/off boards
  - `ALARMBOARD.yaml` - Special function board
  - `secrets.yaml` - WiFi and encryption credentials
  - `claude.md` - Comprehensive technical documentation

### Shared Secrets (`secrets.yaml`)
```yaml
wifi_ssid: "24"
wifi_password: "1234567890"
api_encryption_key: "yvBVlHtbCQJaCH4GPwA4NW4p9CXcWYWcA+Xvv3XdnjE="
ota_password: "34d5891ea1b99f7a447d08d15fc6c737"
fallback_password: "RNaWqpHp6lz1"
```

---

## Network & Connectivity

### WiFi Configuration
- **SSID**: `24`
- **Password**: `1234567890`
- **Network**: Local WiFi (recently experienced brief outage)
- **Effect**: All panel devices offline after WiFi restoration

### Device Network Names
Expected mDNS names (if using ESPHome defaults):
- `dimmerboard1.local` through `dimmerboard5.local`
- `onoffboard6.local`, `onoffboard7.local`
- Panel device names unknown (check HA ESPHome dashboard)

### Home Assistant Integration
- **URL**: http://192.168.0.22:8123
- **API Token**: (stored in monitoring scripts)
- **Integration**: ESPHome components loaded
  - `esphome`
  - `esphome.binary_sensor`
  - `esphome.sensor`
  - `esphome.light`

---

## Blueprint Automation System

### Current Blueprint
**File**: `dimmer_two_button.yaml`
**Location**: `/Users/jmr/dev/casa apertura/`

**Functionality**:
- Single click: Brightness adjustment
- Double click: On/off or 100% brightness
- Configurable brightness step (default 20%)
- Configurable double-click window (default 400ms)

### Current Automation
**File**: `kitchen_dimmer_automation.yaml`
**Uses**:
- UP Button: `binary_sensor.kitchen_panel_up_kpu3`
- DOWN Button: `binary_sensor.kitchen_panel_dn_kpl3`
- Target Light: `light.shellyprodm2pm_a0dd6c9e5f08_light_0`

**Status**: ❌ Not working (devices offline)

### Blueprint Application Plan

Each panel has UP/DOWN button pairs that can use the dimmer blueprint. The plan is to apply the blueprint to ALL panel buttons for comprehensive control.

**Button Pairs to Automate** (26 total automations):

#### Dining Room Panel (4 automations)
1. DR1 (UP) + DR1D (DOWN) → Dining Sideboard
2. DR2 (UP) + DR2D (DOWN) → Dining Pendant
3. DR3 (UP) + DR3D (DOWN) → Great Room Cans
4. DR4 (UP) + DR4D (DOWN) → Great Room Box Lights

#### Kitchen Panel UP (4 automations)
1. KPU1 (UP) + KPUD1 (DOWN) → Kitchen Cans
2. KPU2 (UP) + KPUD2 (DOWN) → Main Hallway
3. KPU3 (UP) + KPUD3 (DOWN) → Isla ⭐ (already configured)
4. KPU4 (UP) + KPUD4 (DOWN) → Kitchen Box Lights

#### Kitchen Panel DOWN (2 automations)
1. KPL2 (UP) + KPLD2 (DOWN) → Great Room LED
2. KPL3 (UP) + KPLD3 (DOWN) → Banquette Pendant ⭐ (already configured)

Note: KPL1 and KPL4 don't have DOWN pairs in the entity list

#### Master Panel (4 automations)
1. MSTR1 (UP) + MSTR1D (DOWN)
2. MSTR2 (UP) + MSTR2D (DOWN)
3. MSTR3 (UP) + MSTR3D (DOWN)
4. MSTR4 (UP) + MSTR4D (DOWN)

#### Nine Panel (2 automations)
1. NINE1 (UP) + NINE5 (DOWN) → Terrace Ceiling One
2. NINE2 (UP) + NINE6 (DOWN) → Outdoor Dining Lights

Note: NINE3 has no DOWN pair

#### Other Nine Panel (4 automations)
- Needs button mapping review after device comes online
- Potentially 4 UP/DOWN pairs

#### Terrace Panel (4 automations)
1. TERR1 (UP) + TERR1D (DOWN)
2. TERR2 (UP) + TERR2D (DOWN)
3. TERR3 (UP) + TERR3D (DOWN)
4. TERR4 (UP) + TERR4D (DOWN)

**Total Automations to Create**: ~26 automations using the dimmer blueprint

---

## Action Plan

### Phase 1: Get Devices Online ⚡ IMMEDIATE

1. **Power Cycle Panel Devices**
   - Physically power cycle all 7 panel ESP32s
   - Wait 2-3 minutes for WiFi reconnection
   - Check Home Assistant for device status

2. **Verify Network Connectivity**
   - Confirm WiFi "24" is stable
   - Check if devices appear in router DHCP list
   - Scan network for ESP32 devices

3. **Check Home Assistant**
   - Navigate to http://192.168.0.22:8123
   - Go to Settings → Devices & Services → ESPHome
   - Verify which devices come online
   - Note IP addresses and status

### Phase 2: Access and Backup Configs 📁

1. **Access ESPHome Dashboard**
   - In Home Assistant, navigate to ESPHome addon
   - Or: Settings → Add-ons → ESPHome → Open Web UI
   - View list of all ESPHome devices

2. **Download Panel Configs**
   - For each panel device (dining_room_light_panel, kitchen_panel_up, etc.)
   - Download the `.yaml` configuration file
   - Save to `/Users/jmr/dev/casa apertura/panel_configs/`

3. **Document Device Information**
   - Record IP addresses
   - Note firmware versions
   - Screenshot ESPHome dashboard
   - Document any warning/error messages

### Phase 3: Documentation 📝

1. **Create Device Mapping Document**
   - Map each ESPHome device name to physical location
   - Map button entities to controlled lights
   - Document GPIO pin assignments from configs
   - Create wiring diagrams if needed

2. **Update CLAUDE.md**
   - Add panel device information
   - Include troubleshooting steps
   - Document automation system architecture
   - Add panel config file locations

3. **Create Automation Inventory**
   - List all current automations
   - Identify gaps in coverage
   - Plan automation priorities

### Phase 4: Apply Blueprint to All Panels 🎯

1. **Test Current Automation**
   - Verify kitchen dimmer automation works
   - Test single-click and double-click functionality
   - Adjust timing parameters if needed

2. **Create Automation Templates**
   - Create script to generate automations from blueprint
   - Or: Create HA automation YAML file with all 26 automations
   - Use consistent naming convention

3. **Deploy Automations Systematically**
   - **Priority 1**: Kitchen panels (highest use)
   - **Priority 2**: Dining room panel
   - **Priority 3**: Master bedroom panel
   - **Priority 4**: Outdoor/terrace panels

4. **Testing Protocol**
   - Test each automation after creation
   - Verify both UP and DOWN buttons work
   - Check single-click vs double-click behavior
   - Test all light transitions

### Phase 5: Additional Devices (If Needed) 🔧

1. **Identify Unflashed Devices**
   - Count physical ESP32s vs registered devices
   - You mentioned 6-10 total, we have 7 panels + 7 dimmers = 14 total
   - Determine if more devices need setup

2. **Flash New Devices** (if applicable)
   - Create config file based on template
   - Compile firmware
   - Flash via USB or OTA
   - Add to Home Assistant

---

## Quick Reference Commands

### Check Device Status
```bash
python3 monitor_kitchen_buttons.py
```

### Update HA Entities Export
```bash
python3 dump_ha_entities.py
```

### ESPHome Commands (from esp_project directory)
```bash
# Compile configuration
esphome compile DimmerBoard1.yaml

# Upload via OTA (if device online)
esphome run DimmerBoard1.yaml --device <IP_ADDRESS>

# Upload via USB
esphome run DimmerBoard1.yaml
```

### Network Scan for ESP32s
```bash
nmap -sn 192.168.0.0/24 | grep -B 2 "Espressif"
```

---

## Troubleshooting

### Devices Won't Connect After WiFi Restore

**Solution 1**: Power cycle devices
- Unplug power for 10 seconds
- Plug back in
- Wait 2-3 minutes for connection

**Solution 2**: Check WiFi credentials
- Verify SSID "24" is broadcasting
- Verify password "1234567890" is correct
- Check router for MAC filtering

**Solution 3**: Fallback AP mode
- If device can't connect, it creates fallback AP
- Look for WiFi network named `<devicename>_fallback`
- Connect using password `RNaWqpHp6lz1`
- Reconfigure WiFi through captive portal

### Device Shows as Unavailable in HA

**Possible Causes**:
- Device not powered on
- WiFi connection issues
- API encryption key mismatch
- Device IP changed and HA hasn't updated
- ESPHome integration needs reload

**Solutions**:
1. Check device power and network LED
2. Restart ESPHome integration in HA
3. Check HA logs for connection errors
4. Verify API keys match between device and HA

---

## Next Steps - IMMEDIATE ACTIONS

1. ✅ **Documentation Complete** - This file created
2. 🔄 **Power Cycle Panels** - Physically reset all 7 panel devices
3. 🔄 **Access HA ESPHome Dashboard** - Download panel configs
4. 🔄 **Test Connectivity** - Verify all devices online
5. ⏳ **Apply Blueprint** - Create 26 automations for full panel control
6. ⏳ **Update Scripts** - Fix IP addresses in monitoring scripts
7. ⏳ **Flash Any Missing Devices** - If additional ESP32s need setup

---

**Documentation Maintained By**: Claude Code
**Project Owner**: JMR
**Last System Review**: 2025-12-12
