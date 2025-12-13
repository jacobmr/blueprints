# ESP32 System Setup - Action Checklist

**Goal**: Get all 7 panel devices online and apply dimmer blueprint to 26 button pairs

---

## ✅ Phase 1: GET DEVICES ONLINE (Do This First!)

### Step 1: Power Cycle All Panel Devices
- [ ] Locate and power cycle all 7 ESP32 panel devices
  - Dining Room Panel
  - Kitchen Panel (UP)
  - Kitchen Panel (DOWN)
  - Master Panel
  - Nine Panel
  - Other Nine Panel
  - Terrace Panel
- [ ] Wait 3 minutes for devices to reconnect to WiFi "24"

### Step 2: Verify Devices Online in Home Assistant
- [ ] Open http://192.168.0.22:8123
- [ ] Navigate to: **Settings → Devices & Services → ESPHome**
- [ ] Check which panels show as "Online"
- [ ] Note: If any still unavailable after 5 min, troubleshoot that device

---

## 📥 Phase 2: BACKUP PANEL CONFIGS

### Step 3: Access ESPHome Dashboard
- [ ] In Home Assistant, go to **Settings → Add-ons → ESPHome**
- [ ] Click "Open Web UI" or find ESPHome in sidebar
- [ ] You should see all 7 panel devices listed

### Step 4: Download Configurations
- [ ] For EACH panel device, click the device card
- [ ] Look for "Edit" or download option
- [ ] Save the `.yaml` file to this folder
- [ ] Create subdirectory: `mkdir panel_configs`
- [ ] Name files clearly:
  - `dining_room_light_panel.yaml`
  - `kitchen_panel_up.yaml`
  - `kitchen_panel_dn.yaml`
  - `master_panel.yaml`
  - `nine_panel.yaml`
  - `other_nine_panel.yaml`
  - `terrace_panel.yaml`

### Step 5: Document Device Info
- [ ] Take screenshot of ESPHome dashboard
- [ ] Note IP address for each device
- [ ] Note firmware version (ESPHome version)
- [ ] Save screenshot to this folder

---

## 🎯 Phase 3: APPLY BLUEPRINT TO ALL PANELS

### Step 6: Update Monitoring Scripts (Optional but Recommended)
The scripts in this folder have the old IP (172.28.133.210). Update them:
```bash
# Find and replace in all Python scripts
find . -name "*.py" -exec sed -i '' 's/172.28.133.210/192.168.0.22/g' {} \;
```

### Step 7: Test Current Automation
- [ ] Verify `kitchen_dimmer_automation.yaml` is loaded in HA
- [ ] Test the UP button (KPU3) - should control Isla light
- [ ] Test single-click (brightness change)
- [ ] Test double-click (100% or off)
- [ ] If not working, check that devices are online first!

### Step 8: Create Automation Files for All Panels

You have 26 button pairs to automate. Options:

**Option A: Manual in HA UI**
- Go to Settings → Automations → Create Automation
- Select "Dimmer with Two Buttons" blueprint
- Fill in UP button, DOWN button, and target light
- Repeat 26 times (tedious but straightforward)

**Option B: YAML File (Recommended)**
- Create a single YAML file with all 26 automations
- Import into HA
- I can help generate this file

### Step 9: Priority Order for Automation Creation

**High Priority** (Create these first):
1. [ ] Kitchen Panel UP - KPU1/KPUD1 (Kitchen Cans)
2. [ ] Kitchen Panel UP - KPU2/KPUD2 (Main Hallway)
3. [ ] Kitchen Panel UP - KPU4/KPUD4 (Kitchen Box Lights)
4. [ ] Kitchen Panel DN - KPL2/KPLD2 (Great Room LED)
5. [ ] Dining Room - All 4 pairs (DR1-4)

**Medium Priority**:
6. [ ] Master Panel - All 4 pairs (MSTR1-4)

**Low Priority** (Outdoor/Terrace):
7. [ ] Nine Panel - 2 pairs
8. [ ] Terrace Panel - 4 pairs
9. [ ] Other Nine Panel - Review and configure

### Step 10: Testing Each Automation
For each automation created:
- [ ] Test UP button single-click (should increase brightness)
- [ ] Test UP button double-click (should go to 100%)
- [ ] Test DOWN button single-click (should decrease brightness)
- [ ] Test DOWN button double-click (should turn off)
- [ ] Adjust brightness_step and double_click_window if needed
- [ ] Document any issues

---

## 📝 Phase 4: FINAL DOCUMENTATION

### Step 11: Update Documentation
- [ ] Update `ESP32_COMPLETE_DOCUMENTATION.md` with:
  - Device IP addresses
  - Firmware versions
  - Any configuration changes made
  - List of all active automations
- [ ] Create automation map (which buttons control which lights)
- [ ] Take screenshots of working system

### Step 12: Backup Everything
- [ ] Backup all panel configs to this folder
- [ ] Export Home Assistant automations
- [ ] Commit everything to git:
  ```bash
  git add .
  git commit -m "Complete ESP32 panel setup and documentation"
  git push
  ```

---

## 🔧 Troubleshooting Quick Reference

### Device Won't Come Online After Power Cycle
1. Check power LED on ESP32
2. Look for fallback WiFi network: `<devicename>_fallback`
3. Connect to fallback network (password: `RNaWqpHp6lz1`)
4. Reconfigure WiFi through captive portal
5. Reboot device

### Automation Not Working
1. Verify devices (panels and lights) are online
2. Check entity IDs match exactly (case-sensitive)
3. Test buttons manually in Home Assistant Developer Tools
4. Check Home Assistant logs for errors
5. Reload automation after changes

### Can't Access ESPHome Dashboard
1. Verify ESPHome addon is installed and running
2. Try accessing directly: http://192.168.0.22:6052
3. Check addon logs if issues persist
4. Restart ESPHome addon if needed

---

## 📊 Progress Tracking

### Devices Online Status
- [ ] Dining Room Panel - ❌ Offline → ⏳ Pending → ✅ Online
- [ ] Kitchen Panel UP - ❌ Offline → ⏳ Pending → ✅ Online
- [ ] Kitchen Panel DN - ❌ Offline → ⏳ Pending → ✅ Online
- [ ] Master Panel - ❌ Offline → ⏳ Pending → ✅ Online
- [ ] Nine Panel - ❌ Offline → ⏳ Pending → ✅ Online
- [ ] Other Nine Panel - ❌ Offline → ⏳ Pending → ✅ Online
- [ ] Terrace Panel - ❌ Offline → ⏳ Pending → ✅ Online

### Automations Created
**Kitchen Panels**: 0/6 ⏳
**Dining Room**: 0/4 ⏳
**Master Bedroom**: 0/4 ⏳
**Outdoor/Terrace**: 0/10 ⏳

**Total**: 0/26 automations

---

## 🎯 SUCCESS CRITERIA

System is complete when:
- ✅ All 7 panel devices show as "Online" in Home Assistant
- ✅ All panel configs backed up to local folder
- ✅ 26 automations created using dimmer blueprint
- ✅ All automations tested and working
- ✅ Documentation updated with current state
- ✅ Everything committed to git

---

**Created**: 2025-12-12
**Last Updated**: 2025-12-12
**Status**: Ready to begin Phase 1
