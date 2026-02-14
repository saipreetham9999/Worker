#!/bin/bash
REPO_URL="https://github.com/saipreetham9999/Worker.git"
DIR_NAME="Worker"

echo "========================================"
echo "🚀 FORCE DEPLOYMENT: WIPING LOCAL CHANGES"
echo "========================================"

if [ -d "$DIR_NAME" ]; then
    cd "$DIR_NAME"

    # 🛑 THE DANGER ZONE: Reset everything to match GitHub
    echo "🔥 Hard Resetting to origin/main..."
    git fetch origin
    git reset --hard origin/main
    git pull origin main
else
    # Clone fresh if missing
    git clone "$REPO_URL"
    cd "$DIR_NAME"
fi

# Install dependencies quietly
if [ -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt > /dev/null 2>&1
fi

echo "✅ STARTING WORKER..."
python3 main.py
