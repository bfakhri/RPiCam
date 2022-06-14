#!/bin/sh
# Encodes at 4k, 24fps, 56Mbit/s
#ffmpeg -pattern_type glob -i './fast/*.png' -c:v h264_nvenc -vf scale=1920:1080 -r 24 -b:v 10M output_fast_smaller.avi
ffmpeg -pattern_type glob -i './fast/*.png' -c:v h264_nvenc -r 24 -b:v 100M output_fast.mp4
