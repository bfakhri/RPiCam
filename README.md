# Timelapse Utilities for the RPi

These scripts can be used with an RaspberryPi to capture a timelapse with an attached webcam. The script ``` capture_timelapse.py ``` saves images into an ``` images/ ``` directory and the ``` generate*.py ``` scripts compile those images into a video file (avi). 

## Installation
```
python3 -m venv virtualenv

source virtualenv/bin/activate

pip install -r requirements.txt
```

## Gather images

Before collecting the timelapse, ensure the default parameters are sufficient for your use case (capture period, focus distance (only works on some webcams), jpg quality, etc). 

Then ensure that a directory exists to store the images ``` mkdir images/ ```. Then you can run the capture script: 

```
python capture_timelapse.py
```

This will capture images indefinitely (or, more practically, until you run out of storage space). 

## Compile captured images into a video

Once you are finished capturing the image, use the ``` generate_slider_video.py ```. 

[![Timelapse of a Portulaca](https://raw.githubusercontent.com/bfakhri/Poker/master/portulaca.png)](https://youtu.be/m5NLu9jh1go "Timelapse of a Portulaca")

