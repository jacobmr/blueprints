#!/bin/bash
# ESPHome Config Downloader for Private GitHub Repository
# This script reads the GitHub token from a local file for security

# Configuration
GITHUB_USER="jacobmr"
GITHUB_REPO="blueprints"
GITHUB_BRANCH="main"
TOKEN_FILE="/config/.github_token"
ESPHOME_DIR="/config/esphome"

# Read token from file
if [ ! -f "$TOKEN_FILE" ]; then
    echo "ERROR: Token file not found at $TOKEN_FILE"
    echo "Create the file with: echo 'your_token_here' > $TOKEN_FILE"
    exit 1
fi

GITHUB_TOKEN=$(cat "$TOKEN_FILE" | tr -d '\n\r ')

# Function to download a file
download_file() {
    local filename=$1
    local output_path="${ESPHOME_DIR}/${2:-$filename}"
    local url="https://raw.githubusercontent.com/${GITHUB_USER}/${GITHUB_REPO}/${GITHUB_BRANCH}/${filename}"

    echo "Downloading ${filename}..."
    curl -H "Authorization: token ${GITHUB_TOKEN}" \
         -o "$output_path" \
         -f \
         -s \
         "$url"

    if [ $? -eq 0 ]; then
        echo "✓ Downloaded ${filename}"
    else
        echo "✗ Failed to download ${filename}"
        return 1
    fi
}

# Download specific file or all configs
case "${1:-all}" in
    "great-room")
        download_file "great-room-led-WORKING.yaml" "great-room-led.yaml"
        ;;
    "all")
        download_file "great-room-led-WORKING.yaml" "great-room-led.yaml"
        download_file "great-room-led-esp32.yaml"
        ;;
    *)
        echo "Usage: $0 [great-room|all]"
        exit 1
        ;;
esac

echo "Done!"
