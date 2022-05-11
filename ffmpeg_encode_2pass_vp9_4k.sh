#!/bin/sh
# Encodes at 4k, 24fps, 56Mbit/s
# Reference: https://trac.ffmpeg.org/wiki/Encode/VP9
ffmpeg -pattern_type glob -i 'temper/*.png' -c:v libvpx-vp9 -r 24 -vf scale=3840:2160 -b:v 56M -pass 1 -an -f null /dev/null && \
ffmpeg -pattern_type glob -i 'temper/*.png' -c:v libvpx-vp9 -r 24 -vf scale=3840:2160 -b:v 56M -pass 2 -c:a libopus 4k_2pass_output.mp4
