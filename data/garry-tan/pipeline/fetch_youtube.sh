#!/bin/bash
# fetch_youtube.sh — Download Garry Tan YouTube transcripts/subtitles
#
# Usage:
#   ./fetch_youtube.sh [--count 20]
#
# Output: garry-tan/data/youtube/*.vtt
# Dependencies: python3, yt-dlp (pip install yt-dlp)
#
# Note: YouTube auto-captions require a PO token for some videos.
# If subtitles are missing, try: pip install yt-dlp --upgrade
# See: https://github.com/yt-dlp/yt-dlp/wiki/PO-Token-Guide

set -euo pipefail

CHANNEL="https://www.youtube.com/@garrytan/videos"
COUNT="${1:-20}"  # Default: first 20 videos
OUTPUT_DIR="$(dirname "$0")/../data/youtube"
mkdir -p "$OUTPUT_DIR"

# Check yt-dlp
if ! python3 -m yt_dlp --version &>/dev/null; then
    echo "Installing yt-dlp..."
    pip3 install yt-dlp -q
fi

echo "Fetching subtitles for first $COUNT videos from @garrytan..."
echo "Channel: $CHANNEL"
echo "Output: $OUTPUT_DIR"
echo ""

python3 -m yt_dlp \
    --write-auto-sub \
    --skip-download \
    --sub-langs "en" \
    --playlist-items "1-${COUNT}" \
    "$CHANNEL" \
    -o "$OUTPUT_DIR/%(title)s.%(ext)s" \
    2>&1

# Count downloaded files
VTT_COUNT=$(find "$OUTPUT_DIR" -name "*.vtt" 2>/dev/null | wc -l | tr -d ' ')
echo ""
echo "Done. VTT files downloaded: $VTT_COUNT"

# Convert VTT to plain text for easier processing
if [ "$VTT_COUNT" -gt 0 ]; then
    echo "Converting VTT to plain text..."
    python3 << 'PYEOF'
import re
from pathlib import Path

output_dir = Path(__file__).parent.parent / "data" / "youtube"
for vtt_file in output_dir.glob("*.vtt"):
    txt_file = vtt_file.with_suffix(".txt")
    with open(vtt_file) as f:
        content = f.read()

    # Strip VTT formatting
    lines = content.split('\n')
    text_lines = []
    for line in lines:
        # Skip timestamps, WEBVTT header, and empty lines
        if re.match(r'^\d{2}:\d{2}', line) or line.startswith('WEBVTT') or '-->' in line or line.strip() == '':
            continue
        # Strip HTML tags
        line = re.sub(r'<[^>]+>', '', line).strip()
        if line:
            text_lines.append(line)

    # Deduplicate consecutive identical lines (VTT has lots of these)
    deduped = []
    prev = None
    for line in text_lines:
        if line != prev:
            deduped.append(line)
            prev = line

    with open(txt_file, 'w') as f:
        f.write('\n'.join(deduped))
    print(f"  Converted: {vtt_file.name}")

print(f"Converted {len(list(output_dir.glob('*.vtt')))} VTT files to plain text")
PYEOF
fi
