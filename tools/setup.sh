#!/bin/bash
# Recreates the paths the builder expects. Run from repo root.
set -e
mkdir -p /home/claude/reels /home/claude/wf/brand /home/claude/wf/v3/img
cp tools/reel.html tools/tts.py tools/build.py tools/verify.py tools/scenes/*.js /home/claude/reels/
cp tools/*.woff2 /home/claude/wf/brand/
cp tools/icon.svg tools/3d-property-walkthrough.webp /home/claude/wf/v3/img/
pip install --break-system-packages kokoro-onnx soundfile espeakng_loader phonemizer numpy
cd /home/claude/reels
[ -f kokoro-v1.0.onnx ] || curl -L -o kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
[ -f voices-v1.0.bin ] || curl -L -o voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
