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

## 📚 Project Files

- `dimmer_two_button.yaml` - Main dimmer blueprint with double-click
- `two_button_onoff.yaml` - Simple on/off control
- `spst_switch_light.yaml` - Toggle switch control
- `kitchen_dimmer_automation.yaml` - Example automation instance
- `CLAUDE.md` - Development instructions for AI assistants
- `ESP32_COMPLETE_DOCUMENTATION.md` - Full ESP32 system documentation
- `monitor_kitchen_buttons.py` - Development tool for testing buttons

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
