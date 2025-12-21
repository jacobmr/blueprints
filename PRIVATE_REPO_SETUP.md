# Private GitHub Repository Setup Guide

This guide explains how to configure Home Assistant to download ESPHome configs from a **private** GitHub repository securely.

## Why Private?

- Your WiFi passwords are in the YAML files
- Your API encryption keys are in the YAML files
- Better security for remote locations

## One-Time Setup

### Step 1: Generate GitHub Personal Access Token

1. Go to: https://github.com/settings/tokens?type=beta
2. Click **"Generate new token"**
3. Configure the token:
   - **Token name**: `HA-ESPHome-Reader`
   - **Expiration**: 1 year (or your preference)
   - **Repository access**: **Only select repositories**
   - Select: **blueprints**
   - **Permissions** → **Repository permissions**:
     - **Contents**: **Read-only** ✅
4. Click **Generate token**
5. **COPY THE TOKEN** immediately (you won't see it again!)
   - Format: `github_pat_11ABC123...XYZ`

### Step 2: Make Repository Private

1. Go to: https://github.com/jacobmr/blueprints/settings
2. Scroll to **Danger Zone** section
3. Click **Change visibility** → **Make private**
4. Type the repository name to confirm
5. Click **I understand, make this repository private**

### Step 3: Install Download Script in Home Assistant

**In Home Assistant Terminal:**

```bash
# Create scripts directory
mkdir -p /config/scripts

# Download the script
curl -o /config/scripts/download_esphome_config.sh https://raw.githubusercontent.com/jacobmr/blueprints/main/download_esphome_config.sh

# Make it executable
chmod +x /config/scripts/download_esphome_config.sh

# Create token file (replace YOUR_TOKEN with actual token from Step 1)
echo "github_pat_YOUR_TOKEN_HERE" > /config/.github_token

# Verify it was created
ls -la /config/.github_token
```

**IMPORTANT**: Replace `YOUR_TOKEN_HERE` with your actual token from Step 1!

### Step 4: Update Home Assistant Configuration

1. **File Editor** → `/config/configuration.yaml`
2. Find the `shell_command:` section
3. It should already have:
   ```yaml
   shell_command:
     download_great_room_yaml: '/config/scripts/download_esphome_config.sh great-room'
     download_all_esphome_yamls: '/config/scripts/download_esphome_config.sh all'
   ```
4. Save and restart Home Assistant

### Step 5: Test the Download

1. Go to your dashboard
2. Click the **"DOWNLOAD"** button on your ESPHome updater card
3. You should get a notification: "ESPHome Config Updated"
4. Check ESPHome dashboard - the YAML should be there!

## How It Works

**Single Token, Multiple Files:**
- Token stored **once** in `/config/.github_token`
- Script reads token and downloads any file from the repo
- No token duplication in configuration files

**Security:**
- Token file is in `/config/` (not accessible via web)
- Token has **read-only** access
- Token only works for the `blueprints` repository
- Can revoke token anytime at GitHub

## Troubleshooting

### "ERROR: Token file not found"
```bash
# Check if file exists
ls -la /config/.github_token

# Recreate it
echo "your_token_here" > /config/.github_token
```

### "Failed to download"
- Check that repo is accessible at: https://github.com/jacobmr/blueprints
- Verify token hasn't expired: https://github.com/settings/tokens
- Test manually:
  ```bash
  /config/scripts/download_esphome_config.sh great-room
  ```

### "Permission denied"
```bash
# Make script executable
chmod +x /config/scripts/download_esphome_config.sh
```

## Token Expiration

Tokens expire after 1 year (or custom duration). When expired:

1. Generate a new token (same steps as above)
2. Update `/config/.github_token`:
   ```bash
   echo "new_token_here" > /config/.github_token
   ```
3. Done! No config changes needed.

## Security Notes

- ✅ Token is read-only (can't modify repo)
- ✅ Token is scoped to one repo only
- ✅ Token is stored locally, not in YAML
- ✅ `.github_token` file should be added to `.gitignore`
- ✅ Can revoke token anytime without breaking HA

## For Matt

Once setup is complete, you just:
1. Click the **DOWNLOAD** button on your dashboard
2. Open **ESPHome** from sidebar
3. Click **INSTALL** → **Wirelessly**

The token is managed automatically - no need to think about it! 🎯
