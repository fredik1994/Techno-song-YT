#!/bin/bash
# Usage: put Suno v1 audio as audio/01.mp3 ... audio/08.mp3 (mp3/m4a/wav ok), then run ./build_videos.sh
cd "$(dirname "$0")"
for cover in [0-9][0-9]_*.cover.png; do
  slug=${cover%.cover.png}; n=${slug:0:2}
  a=$(ls audio/$n.* 2>/dev/null | head -1)
  [ -z "$a" ] && { echo "$slug: MISSING audio/$n.*"; continue; }
  ffmpeg -y -v error -loop 1 -framerate 1 -i "$cover" -i "$a" -c:v libx264 -tune stillimage -preset medium -crf 18 -pix_fmt yuv420p -r 1 \
    -c:a aac -b:a 320k -ar 48000 -shortest -movflags +faststart "$slug.mp4" && \
  printf "%s  %s\n" "$slug.mp4" "$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$slug.mp4" | awk '{printf "%d:%02d", $1/60, $1%60}')"
done
