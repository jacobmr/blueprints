# Lights Needing Automations - Action Plan

**Date**: 2025-12-12
**Status**: 17 automations exist, ~10 lights still need coverage

---

## ✅ Lights Already Have Automations (17)

| Light Name        | Entity ID                                   | Automation                                |
| ----------------- | ------------------------------------------- | ----------------------------------------- |
| Isla              | `light.shellyprodm2pm_a0dd6c9e5f08_light_1` | ✅ Isla New (on)                          |
| Main Hall         | `light.shellyprodm2pm_a0dd6c9e5f08_light_0` | ✅ Main Hallway Control                   |
| Kitchen Cans      | `light.shellyprodm2pm_2cbcbb9f4bcc_light_1` | ✅ Kitchen Cans Control Automation        |
| Kitchen Box       | `light.shellyprodm2pm_2cbcbba40ca0_light_1` | ✅ Kitchen Box Control automation         |
| Banquette Pendant | `light.shellyprodm2pm_2cbcbb9f4bcc_light_0` | ✅ Banquette Pendant Control              |
| Sideboard Cans    | `light.shellyprodm2pm_2cbcbba38c20_light_0` | ✅ Dining Sideboard cans Control          |
| Dining Pendants   | `light.shellyprodm2pm_2cbcbba1f7c4_light_0` | ✅ Dining Pendants Control Automation     |
| Great Room Cans   | `light.shellyprodm2pm_2cbcbba38c20_light_1` | ✅ Great Room Cans control Automation     |
| Great Room Box    | `light.shellyprodm2pm_2cbcbba1f7c4_light_1` | ✅ Great Room Box Control Automation      |
| Great Room LED    | `light.great_room_limited`                  | ✅ Great Room LED Control                 |
| Courtyard Sconces | `light.shellypro3_ece334ed5278_switch_0`    | ✅ Courtyard Sconces                      |
| Terrace Strip One | `light.shellyprodm2pm_2cbcbba40c84_light_0` | ✅ Terrace Ceiling One Control Automation |
| Outdoor Dining    | `light.shellyprodm2pm_2cbcbba40c84_light_1` | ✅ Outdoor Dining Control Automation      |
| Bench LED         | `light.shellypro3_ece334e97ab8_switch_0`    | ✅ Turn ON Bench LED                      |

**Note**: "Just Isla" automation exists but is turned OFF. "Isla New" is ON.

---

## ❌ Lights WITHOUT Automations (Need to Create)

### Indoor/Entry Lights

| Priority | Light Name      | Entity ID                                   | Suggested Panel Button | Notes                     |
| -------- | --------------- | ------------------------------------------- | ---------------------- | ------------------------- |
| HIGH     | Banquette Spots | `light.shellyprodm2pm_2cbcbba40ca0_light_0` | Kitchen Panel?         | Related to Banquette area |

### Outdoor/Landscape Lights

| Priority | Light Name             | Entity ID                                | Suggested Panel Button | Notes            |
| -------- | ---------------------- | ---------------------------------------- | ---------------------- | ---------------- |
| MED      | Driveway               | `light.shellypro3_ece334e986dc_switch_0` | Other Nine Panel?      | Outdoor lighting |
| MED      | Front Walk             | `light.shellypro3_ece334e977e0_switch_2` | Other Nine Panel?      | Entry path       |
| MED      | Front Walk Sconce      | `light.shellypro3_ece334ed586c_switch_2` | Other Nine Panel?      | Front entrance   |
| MED      | Garage Sconces         | `light.shellypro3_ece334e977e0_switch_1` | Other Nine Panel?      | Garage area      |
| MED      | Guest Walkway          | `light.shellypro3_ece334ed5278_switch_1` | Other Nine Panel?      | Guest path       |
| MED      | Service Walkway        | `light.shellypro3_ece334e986dc_switch_2` | Other Nine Panel?      | Service area     |
| MED      | South Landscape Lights | `light.shellypro3_ece334e977e0_switch_0` | Other Nine Panel?      | Landscape        |
| MED      | Tree                   | `light.shellypro3_ece334e986dc_switch_1` | Other Nine Panel?      | Tree uplighting  |
| LOW      | Planter By Pool        | `light.shellypro3_ece334e97ab8_switch_2` | Nine Panel NINE3?      | Pool area        |
| LOW      | Pool Lights            | `light.shellypro3_ece334e97ab8_switch_1` | Terrace Panel?         | Pool             |
| SKIP     | Not Connected          | `light.shellypro3_ece334ed5278_switch_2` | -                      | Skip this one    |

**Total to Create**: ~10 new automations

---

## 📋 Available Panel Buttons (Currently Offline)

### Panel Buttons Already Mapped to Automations:

Based on entity names in existing automations, these buttons are likely already in use:

- Kitchen Panel UP: KPU3 → Isla
- Kitchen Panel UP: KPU2 → Main Hallway
- Kitchen Panel UP: KPU1 → Kitchen Cans
- Kitchen Panel UP: KPU4 → Kitchen Box
- Kitchen Panel DN: KPL3 → Banquette Pendant
- Kitchen Panel DN: KPL2 → Great Room LED
- Kitchen Panel DN: KPL1 → Courtyard Sconces
- Dining Panel: DR1 → Sideboard Cans
- Dining Panel: DR2 → Dining Pendants
- Dining Panel: DR3 → Great Room Cans
- Dining Panel: DR4 → Great Room Box
- Nine Panel: NINE1 → Terrace Strip One
- Nine Panel: NINE2 → Outdoor Dining
- Nine Panel: NINE3 → Bench LED

### Available Unmapped Panel Buttons:

These buttons are registered in HA but may not have automations yet:

**Master Panel** (8 buttons - all available):

- `binary_sensor.master_panel_mstr1` + `mstr1d`
- `binary_sensor.master_panel_mstr2` + `mstr2d`
- `binary_sensor.master_panel_mstr3` + `mstr3d`
- `binary_sensor.master_panel_mstr4` + `mstr4d`

**Other Nine Panel** (8 buttons - all available):

- `binary_sensor.other_nine_panel_nine1` through `nine8`
- **PERFECT for the outdoor/landscape lights!**

**Terrace Panel** (8 buttons - all available):

- `binary_sensor.terrace_panel_terr1` through `terr4`
- Plus DOWN versions `terr1d` through `terr4d`
- **Good for pool lights and outdoor areas**

**Nine Panel** (possibly some available):

- NINE5, NINE6 might be available for additional controls

---

## 🎯 RECOMMENDED AUTOMATION PLAN

### Phase 1: Banquette Spots (High Priority - Indoor)

**Light**: `light.shellyprodm2pm_2cbcbba40ca0_light_0` (Banquette Spots)
**Suggested Buttons**: Need to determine - possibly unused kitchen panel buttons?
**Action**:

1. First, check if panels are online
2. Determine which button physically controls this light
3. Create automation using blueprint

### Phase 2: Outdoor/Landscape Lights (Use Other Nine Panel)

Map the 8 outdoor lights to "Other Nine Panel" buttons:

| Button       | Light             | Entity ID                                |
| ------------ | ----------------- | ---------------------------------------- |
| NINE1 + DOWN | Driveway          | `light.shellypro3_ece334e986dc_switch_0` |
| NINE2 + DOWN | Front Walk        | `light.shellypro3_ece334e977e0_switch_2` |
| NINE3 + DOWN | Front Walk Sconce | `light.shellypro3_ece334ed586c_switch_2` |
| NINE4 + DOWN | Garage Sconces    | `light.shellypro3_ece334e977e0_switch_1` |
| NINE5 + DOWN | Guest Walkway     | `light.shellypro3_ece334ed5278_switch_1` |
| NINE6 + DOWN | Service Walkway   | `light.shellypro3_ece334e986dc_switch_2` |
| NINE7 + DOWN | South Landscape   | `light.shellypro3_ece334e977e0_switch_0` |
| NINE8 + DOWN | Tree              | `light.shellypro3_ece334e986dc_switch_1` |

**8 automations to create**

### Phase 3: Pool Area (Use Terrace Panel)

| Button       | Light           | Entity ID                                |
| ------------ | --------------- | ---------------------------------------- |
| TERR1 + DOWN | Pool Lights     | `light.shellypro3_ece334e97ab8_switch_1` |
| TERR2 + DOWN | Planter By Pool | `light.shellypro3_ece334e97ab8_switch_2` |

**2 automations to create**

---

## 📝 STEP-BY-STEP CREATION GUIDE

### Method 1: Using HA Blueprint UI (Recommended)

For each light above:

1. **Go to Home Assistant**
   - Navigate to: Settings → Automations & Scenes
   - Click "+ Create Automation"
   - Click "Use a blueprint"

2. **Select Blueprint**
   - Choose "Dimmer Two Button (Click Only)"
   - Or find your `dimmer_two_button.yaml` blueprint

3. **Fill in Parameters**
   - **Automation Name**: `[Light Name] Control` (e.g., "Driveway Control")
   - **Up Button**: Select the UP button entity
   - **Down Button**: Select the corresponding DOWN button entity
   - **Target Light**: Select the light entity
   - **Brightness Step**: 20% (default)
   - **Double Click Window**: 400ms (default)

4. **Save and Test**
   - Save the automation
   - Test single-click (brightness change)
   - Test double-click (on/off or 100%)

### Method 2: YAML File (Bulk Creation)

I can generate a YAML file with all 10 automations pre-configured. You would:

1. Copy the YAML
2. Paste into HA: Configuration → Automations → (kebab menu) → Edit in YAML
3. Save all at once

---

## ⚠️ IMPORTANT: Panels Must Be Online First!

**Current Status**: All panel devices showing as UNAVAILABLE

**Before creating automations**:

1. Power cycle all ESP32 panel devices
2. Wait for them to reconnect to WiFi "24"
3. Verify panels show as "Online" in HA
4. Test that button presses register in Developer Tools → Events

**How to test button is working**:

1. Go to Developer Tools → States
2. Find the button entity (e.g., `binary_sensor.other_nine_panel_nine1`)
3. Watch the state while pressing the physical button
4. Should change from "off" to "on" and back to "off"

---

## 🎯 NEXT STEPS

1. **Get Panels Online**
   - [ ] Power cycle all 7 panel ESP32 devices
   - [ ] Verify they connect to WiFi
   - [ ] Check status in Home Assistant

2. **Verify Button Mapping**
   - [ ] Test each button physically
   - [ ] Confirm which button is which entity
   - [ ] Update mapping table if needed

3. **Create Automations** (in priority order)
   - [ ] Banquette Spots (1 automation)
   - [ ] Other Nine Panel → Outdoor lights (8 automations)
   - [ ] Terrace Panel → Pool area (2 automations)

4. **Test Each Automation**
   - [ ] Single-click increases/decreases brightness
   - [ ] Double-click turns on to 100% or off
   - [ ] Timing feels responsive (adjust if needed)

---

**Want me to generate the YAML file for all 10 automations now?**
Or would you prefer to create them one-by-one in the HA UI first?
