#!/bin/bash

set -e  # fail ngay nếu có lỗi

echo "🚀 Start deploy..."

# 1. Add + commit
echo "📦 Commit source..."
git add .

# Nếu không có thay đổi thì skip commit
if git diff --cached --quiet; then
  echo "⚠️ No changes to commit"
else
  git commit -m "update docs $(date '+%Y-%m-%d %H:%M:%S')"
fi

# 2. Push source
echo "☁️ Push to main..."
git push origin main

# 3. Build + deploy
echo "🏗 Build & deploy..."
USE_SSH=true npm run deploy

echo "✅ Done!"
echo "🌐 https://tuninh99.github.io/cpp-notes/"
