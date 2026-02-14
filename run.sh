#!/bin/bash
REPO_URL="https://github.com/saipreetham9999/Worker.git"
DIR_NAME="Worker"

git fetch origin
git reset --hard origin/main


# Install dependencies quietly
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt

echo "✅ STARTING WORKER..."
python3 main.py

