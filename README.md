# Home Assistant Blueprint Collection

Custom Home Assistant blueprints for controlling lights with ESPHome binary sensors (buttons and switches).

## 📦 Available Blueprints

### 1. Dimmer Two Button (Click Only)
**File**: `dimmer_two_button.yaml`
**Import URL**: `https://raw.githubusercontent.com/jacobmr/blueprints/main/dimmer_two_button.yaml`

**Features**:
- Full dimming control with two momentary buttons (UP/DOWN)
- Single-click UP: Turn on to 50% (if off) or increase brightness by step
- Double-click UP: Set to 100% brightness
- Single-click DOWN: Turn on to 20% (if off) or decrease brightness by step
- Double-click DOWN: Turn light OFF
- Configurable brightness step (5-50%, default 20%)
- Configurable double-click window (200-600ms, default 400ms)

**Best For**: Kitchen panels, bedside controls, anywhere you want fine-grained dimming control

---

### 2. Two Button On/Off
**File**: `two_button_onoff.yaml`
**Import URL**: `https://raw.githubusercontent.com/jacobmr/blueprints/main/two_button_onoff.yaml`

**Features**:
- Simple on/off control with two momentary buttons
- UP button: Turn light ON
- DOWN button: Turn light OFF
- No dimming, no double-click detection

**Best For**: Simple on/off control where dimming isn't needed, garage lights, closets

---

### 3. SPST Switch Light Control
**File**: `spst_switch_light.yaml`
**Import URL**: `https://raw.githubusercontent.com/jacobmr/blueprints/main/spst_switch_light.yaml`

**Features**:
- Direct mapping of physical SPST (toggle) switch to light state
- Switch ON → Light ON
- Switch OFF → Light OFF
- No hold or double-click logic (because it's a toggle switch, not a button)

**Best For**: Traditional toggle switches that stay in position, basement switches, utility areas

---

## 🏠 How to Use in Home Assistant

### Import a Blueprint

1. Open Home Assistant
2. Go to **Settings** → **Automations & Scenes** → **Blueprints**
3. Click **Import Blueprint** (blue button, bottom right)
4. Paste the Import URL from above
5. Click **Preview Blueprint**
6. Click **Import Blueprint**

### Create an Automation from a Blueprint

1. Go to **Settings** → **Automations & Scenes**
2. Click **Create Automation** → **Create new automation**
3. Select one of the imported blueprints
4. Fill in the configuration:
   - Select your button/switch entities (binary sensors)
   - Select your target light
   - Adjust settings (brightness step, double-click timing, etc.)
5. Give it a meaningful name (e.g., "Kitchen Dimmer Control")
6. Click **Save**

---

## 🤖 Modifying Blueprints with AI (Claude Code or ChatGPT)

Matt, here's how you can modify these blueprints yourself using AI tools without needing to become a Home Assistant expert.

### Option 1: Using Claude Code (Recommended)

**Setup** (one-time):
1. Install Claude Code: https://claude.ai/download
2. Clone this repository:
   ```bash
   git clone https://github.com/jacobmr/blueprints.git
   cd blueprints
   ```
3. Open Claude Code in this directory:
   ```bash
   claude
   ```

**Making Changes**:

Just describe what you want in plain English. Here are some examples:

```
"Change the dimmer blueprint so single-click UP increases by 30% instead of 20%"

"Add a triple-click feature to the dimmer that sets the light to 75%"

"Create a new blueprint that uses 4 buttons - two for dimming, two for color temperature"

"Make the SPST switch toggle instead of direct mapping - if the light is on and I flip the switch, turn it off regardless of switch position"

"Add a timer to the two-button on/off blueprint - if I hold the UP button for 2 seconds, turn on for 30 minutes then automatically turn off"
```

Claude Code will:
1. Read the relevant blueprint file
2. Make the changes
3. Test the YAML syntax
4. Commit to git
5. Show you exactly what changed

**Push to GitHub**:
After Claude makes changes, tell it:
```
"Commit these changes and push to GitHub"
```

Then re-import the blueprint in Home Assistant to get the updates.

---

### Option 2: Using ChatGPT

**Setup**:
1. Go to https://chat.openai.com
2. Copy the entire blueprint file content you want to modify

**Making Changes**:

Start a new conversation with:
```
I have a Home Assistant blueprint that controls lights with buttons.
Here's the current blueprint:

[paste the entire YAML file here]

I want to modify it to [describe your change].
Can you update the blueprint and show me the complete new YAML file?
```

**Example Requests**:
```
"Change the double-click timeout from 400ms to 300ms"

"Add a long-press feature - if I hold UP for 1 second, set to 100%"

"Make single-click only change brightness by 10% instead of 20%"

"Add a fourth action - triple-click UP to set the light to a specific color"
```

ChatGPT will give you the complete updated YAML. Then:
1. Copy the new YAML
2. Save it to the blueprint file
3. Commit to git:
   ```bash
   git add [filename].yaml
   git commit -m "Updated blueprint: [describe change]"
   git push
   ```
4. Re-import in Home Assistant

---

## 🔧 Common Modification Examples

### Change Brightness Step
**Tell the AI**: "Change the default brightness step from 20% to 15%"

**What gets modified**: The `default: 20` value under `brightness_step` input

---

### Adjust Double-Click Timing
**Tell the AI**: "Make the double-click window 500ms instead of 400ms"

**What gets modified**: The `default: 400` value under `double_click_window` input

---

### Add Triple-Click Feature
**Tell the AI**: "Add triple-click detection. Triple-click UP should set brightness to 75%"

**What happens**: AI will add another `wait_for_trigger` after the double-click detection and add a new action

---

### Change Single-Click Behavior
**Tell the AI**: "When light is off, single-click UP should turn it on to 100% instead of 50%"

**What gets modified**: The `50` in the template under "SINGLE CLICK UP"

---

### Add Color Temperature Control
**Tell the AI**: "Add color temperature control - long press UP to make warmer, long press DOWN to make cooler"

**What happens**: AI will add duration detection and new color temperature service calls

---

## 📝 Blueprint Modification Workflow

1. **Describe your change** to Claude Code or ChatGPT in plain English
2. **Review the changes** - the AI will show you what's different
3. **Test in Home Assistant**:
   - Go to Developer Tools → YAML
   - Click "Check Configuration" to validate
   - Reload automations
4. **If it works**: Commit and push to GitHub
5. **If it doesn't**: Tell the AI what went wrong and ask for a fix

---

## 🔀 Contributing Back: Submitting Pull Requests

If you create a useful blueprint modification that others might benefit from, you can contribute it back to the main repository!

### Option 1: Ask Claude Code to Create a PR (Easiest)

**Step 1**: Make your changes and test them in Home Assistant

**Step 2**: Ask Claude Code to submit a PR:
```
"I've modified the dimmer blueprint to add triple-click support.
Please create a pull request to submit this back to the main repository.

Use this PR description:
- Added triple-click detection
- Triple-click UP sets brightness to 75%
- Triple-click DOWN sets brightness to 25%"
```

**Step 3**: Claude Code will:
1. Create a new branch
2. Commit your changes
3. Push to GitHub
4. Open a pull request with your description
5. Give you the PR URL

**Step 4**: Share the PR URL with JMR so he can review and merge it!

---

### Option 2: Manual Pull Request (Traditional Git)

If you prefer to do it manually:

```bash
# 1. Create a new branch for your feature
git checkout -b add-triple-click-feature

# 2. Make your changes to the blueprint file
# (edit dimmer_two_button.yaml)

# 3. Commit your changes
git add dimmer_two_button.yaml
git commit -m "Add triple-click feature to dimmer blueprint"

# 4. Push to GitHub
git push origin add-triple-click-feature

# 5. Go to GitHub and create Pull Request
# https://github.com/jacobmr/blueprints/pulls
```

---

## 🍴 Forking: Creating Your Own Version

Want to maintain your own customized version of the blueprints? Fork the repository!

### Why Fork?

- Create custom blueprints without affecting the main repo
- Experiment freely with different features
- Maintain blueprints specific to your home setup
- Share your custom blueprints with others

### How to Fork

**Step 1**: Go to the repository on GitHub:
```
https://github.com/jacobmr/blueprints
```

**Step 2**: Click the **Fork** button (top right)

**Step 3**: This creates a copy at:
```
https://github.com/YOUR-USERNAME/blueprints
```

**Step 4**: Clone YOUR fork to your computer:
```bash
cd ~/dev
git clone https://github.com/YOUR-USERNAME/blueprints.git my-blueprints
cd my-blueprints
```

**Step 5**: Make changes and push to YOUR fork:
```bash
# Make your changes
git add .
git commit -m "My custom dimmer with triple-click"
git push origin main
```

**Step 6**: Import from YOUR fork in Home Assistant:
```
https://raw.githubusercontent.com/YOUR-USERNAME/blueprints/main/dimmer_two_button.yaml
```

### Asking Claude Code to Work with Your Fork

Tell Claude Code which fork to use:
```
"I've forked the blueprints repo to my-username/blueprints.
Please make changes to MY fork, not the original.
Add a feature that..."
```

Claude will:
1. Work with your forked repository
2. Push changes to your fork
3. Keep your custom version separate from the main repo

### Syncing Your Fork with Updates

If the main repository gets updates you want:

```bash
# Add the original repo as a remote (one-time setup)
git remote add upstream https://github.com/jacobmr/blueprints.git

# Get the latest from the main repo
git fetch upstream

# Merge updates into your fork
git merge upstream/main

# Push to your fork
git push origin main
```

**Or ask Claude Code**:
```
"Sync my fork with the latest changes from jacobmr/blueprints"
```

---

## 🐛 Troubleshooting

### Blueprint doesn't show up in Home Assistant
- Make sure you imported from the correct raw GitHub URL
- Check that the YAML syntax is valid (use Developer Tools → YAML → Check Configuration)
- Try re-importing the blueprint

### Automation doesn't trigger
- Check that your button entities are `binary_sensor` domain
- Monitor button presses: Developer Tools → States → find your binary sensor → watch it change
- Check Home Assistant logs: Settings → System → Logs

### Double-click not working
- Increase the `double_click_window` timeout (try 500ms or 600ms)
- Make sure you're clicking fast enough
- Some ESPHome configurations may need debounce adjustments

### Changes not appearing after push to GitHub
- Wait 1-2 minutes for GitHub CDN to update
- Clear Home Assistant cache: Developer Tools → YAML → Reload Automations
- Re-import the blueprint (delete old one first)

---

## 🔗 Useful Resources

- **Home Assistant Blueprints Documentation**: https://www.home-assistant.io/docs/automation/using_blueprints/
- **ESPHome Binary Sensor**: https://esphome.io/components/binary_sensor/
- **Home Assistant Light Service**: https://www.home-assistant.io/integrations/light/
- **Claude Code**: https://claude.ai/code
- **ChatGPT**: https://chat.openai.com

---

## 🔌 ESP32 Dimmer Hardware

This project uses custom ESP32-C3 dimmer hardware based on the [krida0electronics HASS dimmer](https://github.com/krida0electronics/hass).

### Hardware Specs
- **Board**: ESP32-C3-DevKitM-1
- **Output**: GPIO3 (LEDC PWM at 1220Hz)
- **Max Load**: ~3A @ 120V (360W)
- **Use Case**: High-amperage LED fixtures

### Configuration File
**File**: `great-room-led-esp32.yaml`

This is the ESPHome configuration for the Great Room LED dimmer.

### Critical Fix: `zero_means_zero: true`

**IMPORTANT**: The default krida0electronics config has a bug where lights won't turn completely off (stay at ~20%).

**The Fix** (already applied in our config):
```yaml
output:
  - platform: ledc
    pin: GPIO03
    id: gpio_03
    frequency: "1220Hz"
    zero_means_zero: true  # ← This line forces true OFF at 0%
```

Without this line, the dimmer maintains a minimum brightness and won't fully turn off, which prevents sleep!

### Web Interface Access

The dimmer has a built-in web interface:
- **URL**: `http://[device-ip-address]` (find IP in Home Assistant)
- **Username**: `admin`
- **Password**: `admin`

Use this to:
- Control the light directly
- View device logs
- Check WiFi status
- Monitor device health

### Flashing/Updating Firmware

**Via ESPHome CLI** (USB connected):
```bash
cd /Users/jmr/dev/hass
python3 -m esphome run hass.yaml --device /dev/cu.usbmodem101
```

**Via ESPHome Dashboard** (OTA over WiFi):
1. Install ESPHome add-on in Home Assistant
2. Open ESPHome Dashboard
3. Upload `great-room-led-esp32.yaml`
4. Click "Install" → "Wirelessly"

### WiFi Configuration

Current settings (hardcoded in YAML):
- **SSID**: Casa Aperture
- **Password**: rosie1234
- **Fallback Hotspot**: "Light-Dimmer Fallback Hotspot" (activates if WiFi fails)

### Troubleshooting

**Light won't turn completely off**:
- Check that `zero_means_zero: true` is in the output config
- Reflash firmware if missing

**Device offline**:
- Check WiFi credentials
- Look for fallback hotspot
- Power cycle the device

**Can't access web interface**:
- Find device IP in Home Assistant (Settings → Devices → great-room-led)
- Make sure you're on the same network
- Try `http://great-room-led.local` (mDNS)

---

## 📚 Project Files

**Blueprints:**
- `dimmer_two_button.yaml` - Main dimmer blueprint with double-click
- `two_button_onoff.yaml` - Simple on/off control
- `spst_switch_light.yaml` - Toggle switch control
- `kitchen_dimmer_automation.yaml` - Example automation instance

**ESP32 Hardware:**
- `great-room-led-esp32.yaml` - ESP32-C3 dimmer configuration with `zero_means_zero` fix

**Documentation:**
- `README.md` - This file! Complete guide for Matt
- `CLAUDE.md` - Development instructions for AI assistants
- `ESP32_COMPLETE_DOCUMENTATION.md` - Full ESP32 system documentation

**Development Tools:**
- `monitor_kitchen_buttons.py` - Real-time button event monitor
- `monitor_light_debug.py` - Light debugging tool (service calls + state changes)

---

## 💡 Tips for Matt

1. **Start Small**: Try modifying just one parameter (like brightness step) before attempting complex changes
2. **Keep Backups**: Git automatically keeps history, but you can always revert: `git checkout [filename]`
3. **Test Before Committing**: Try the blueprint in HA first, make sure it works, then commit
4. **Ask Specific Questions**: The more specific your request to the AI, the better the result
5. **Check the Logs**: If something doesn't work, Home Assistant logs usually tell you why

---

## 🙋 Questions?

If you run into issues or want to add features:
1. Ask Claude Code or ChatGPT - describe the problem in detail
2. Check Home Assistant logs for error messages
3. Review the Home Assistant blueprint documentation

Remember: These blueprints are just YAML files. You can't break Home Assistant by modifying them - worst case, the automation just won't work and you can revert the changes.

Happy automating! 🎉
