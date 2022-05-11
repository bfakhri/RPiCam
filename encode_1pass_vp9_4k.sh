#!/bin/sh
# Encodes at 4k, 24fps, 56Mbit/s
ffmpeg -pattern_type glob -i 'temper/*.png' -vf scale=3840:2160 -c:v libvpx-vp9 -r 24 -b:v 56M output.mp4
