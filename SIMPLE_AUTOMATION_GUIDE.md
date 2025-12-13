# Simple Guide: Create Automations Using Blueprint in HA

**Goal**: Create 10 automations for the remaining lights
**Method**: Use the blueprint directly in Home Assistant UI (no YAML needed!)

---

## ✅ Step 1: Wait for Panels to Come Online

You just power cycled them. Give it 2-3 minutes, then:

1. Go to http://192.168.0.22:8123
2. Navigate to: **Settings → Devices & Services → ESPHome**
3. Look for these panels to show "Online":
   - other_nine_panel
   - terrace_panel
   - master_panel (if needed for Banquette Spots)

Once they're online, buttons will work and you can proceed.

---

## 📱 Step 2: Create Each Automation (Repeat 10 times)

### For Each Light That Needs Control:

1. **Go to Automations**
   - Settings → Automations & Scenes
   - Click the blue **"+ Create Automation"** button (bottom right)

2. **Select Blueprint**
   - Click **"Create new automation"**
   - Scroll down and click **"Dimmer Two Button (Click Only)"**
   - (This is your `dimmer_two_button.yaml` blueprint)

3. **Fill in the Form**
   - **Automation Name**: Give it a clear name (e.g., "Driveway Control")
   - **Up Button**: Click the dropdown, search for the UP button entity
   - **Down Button**: Click the dropdown, search for the DOWN button entity
   - **Target Light**: Click the dropdown, select the light to control
   - **Brightness Step**: Leave at 20% (or adjust if you want)
   - **Double Click Window**: Leave at 400ms

4. **Save**
   - Click **"Save"** at the bottom
   - Done! That's one automation.

5. **Repeat** for the next light

---

## 🎯 The 10 Automations to Create

### Outdoor/Landscape Lights (Use "Other Nine Panel")

#### 1. Driveway
- **Name**: Driveway Control
- **UP Button**: `binary_sensor.other_nine_panel_nine1`
- **DOWN Button**: `binary_sensor.other_nine_panel_nine1` (same button for UP/DOWN, or find the corresponding DOWN entity)
- **Light**: `light.shellypro3_ece334e986dc_switch_0` (Driveway)

#### 2. Front Walk
- **Name**: Front Walk Control
- **UP Button**: `binary_sensor.other_nine_panel_nine2`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334e977e0_switch_2` (Front Walk)

#### 3. Front Walk Sconce
- **Name**: Front Walk Sconce Control
- **UP Button**: `binary_sensor.other_nine_panel_nine3`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334ed586c_switch_2` (Front Walk Sconce)

#### 4. Garage Sconces
- **Name**: Garage Sconces Control
- **UP Button**: `binary_sensor.other_nine_panel_nine4`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334e977e0_switch_1` (Garage Sconces)

#### 5. Guest Walkway
- **Name**: Guest Walkway Control
- **UP Button**: `binary_sensor.other_nine_panel_nine5`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334ed5278_switch_1` (Guest Walkway)

#### 6. Service Walkway
- **Name**: Service Walkway Control
- **UP Button**: `binary_sensor.other_nine_panel_nine6`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334e986dc_switch_2` (Service Walkway)

#### 7. South Landscape Lights
- **Name**: South Landscape Control
- **UP Button**: `binary_sensor.other_nine_panel_nine7`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334e977e0_switch_0` (South Landscape Lights)

#### 8. Tree
- **Name**: Tree Light Control
- **UP Button**: `binary_sensor.other_nine_panel_nine8`
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellypro3_ece334e986dc_switch_1` (Tree)

### Pool Area (Use "Terrace Panel")

#### 9. Pool Lights
- **Name**: Pool Lights Control
- **UP Button**: `binary_sensor.terrace_panel_terr1`
- **DOWN Button**: `binary_sensor.terrace_panel_terr1d`
- **Light**: `light.shellypro3_ece334e97ab8_switch_1` (Pool Lights)

#### 10. Planter By Pool
- **Name**: Planter By Pool Control
- **UP Button**: `binary_sensor.terrace_panel_terr2`
- **DOWN Button**: `binary_sensor.terrace_panel_terr2d`
- **Light**: `light.shellypro3_ece334e97ab8_switch_2` (Planter By Pool)

### Bonus: Banquette Spots (If Needed)

#### 11. Banquette Spots
- **Name**: Banquette Spots Control
- **UP Button**: Find available kitchen or master panel button
- **DOWN Button**: Corresponding DOWN button
- **Light**: `light.shellyprodm2pm_2cbcbba40ca0_light_0` (Banquette Spots)

---

## ⚙️ About the Blueprint Settings

### What Each Setting Does:

**Brightness Step Percentage (default 20%)**
- How much the light brightens/dims with each single click
- 20% = 5 clicks to go from 0% to 100%
- Adjust if you want finer (10%) or coarser (30%) control

**Double Click Window (default 400ms)**
- Maximum time between clicks to register as "double-click"
- 400ms = 0.4 seconds works well for most people
- Increase if you find double-clicks not registering
- Decrease if accidental double-clicks happening

### Blueprint Behavior:

**Single Click:**
- **UP button**: Increases brightness by step % (or turns on to 50% if off)
- **DOWN button**: Decreases brightness by step % (or turns on to 20% if off)

**Double Click:**
- **UP button**: Sets to 100% brightness
- **DOWN button**: Turns light OFF

---

## 🧪 Testing Each Automation

After creating each automation, test it:

1. **Single-click UP button**
   - Light should increase brightness
   - If off, should turn on to 50%

2. **Double-click UP button**
   - Light should go to 100% brightness

3. **Single-click DOWN button**
   - Light should decrease brightness
   - If off, should turn on to 20%

4. **Double-click DOWN button**
   - Light should turn OFF

If it doesn't work:
- Check that panel device is online
- Check that button entity IDs are correct
- Check that light entity ID is correct
- Look at Home Assistant logs for errors

---

## 📝 Quick Checklist

- [ ] Panels are online (check ESPHome integration)
- [ ] Create automation #1 (Driveway)
- [ ] Test automation #1
- [ ] Create automation #2 (Front Walk)
- [ ] Test automation #2
- [ ] Create automation #3 (Front Walk Sconce)
- [ ] Test automation #3
- [ ] Create automation #4 (Garage Sconces)
- [ ] Test automation #4
- [ ] Create automation #5 (Guest Walkway)
- [ ] Test automation #5
- [ ] Create automation #6 (Service Walkway)
- [ ] Test automation #6
- [ ] Create automation #7 (South Landscape)
- [ ] Test automation #7
- [ ] Create automation #8 (Tree)
- [ ] Test automation #8
- [ ] Create automation #9 (Pool Lights)
- [ ] Test automation #9
- [ ] Create automation #10 (Planter By Pool)
- [ ] Test automation #10
- [ ] Create automation #11 (Banquette Spots) - optional
- [ ] Test automation #11

**Total**: 10-11 automations × ~2 minutes each = 20-25 minutes of work

---

## 💡 Tips

1. **Start with one** - Create and test the first automation completely before moving to the next
2. **Use clear names** - You'll thank yourself later when debugging
3. **Test immediately** - Don't create all 10 then test. Test each one as you go.
4. **If a button doesn't work** - The panel might still be offline. Wait a bit longer.
5. **Copy entity IDs** - You can copy/paste entity IDs from this guide into HA

---

**Ready to start?**
Check if panels are online, then create your first automation!
