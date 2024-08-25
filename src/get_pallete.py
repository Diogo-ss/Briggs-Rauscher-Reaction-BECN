import argparse
import json
import os
from os.path import join
from colorthief import ColorThief
import cv2
from tqdm import tqdm

# Command line argument configuration
parser = argparse.ArgumentParser(
    description="Extract predominant colors from video frames."
)
parser.add_argument("--video-name", required=True, help="Path to the video file.")
args = parser.parse_args()

# Set the time interval constant between frame extractions
TIMESKIP = 1000

CURRENT_DIR = "src"
ASSETS = "assets"
VIDEO_NAME = args.video_name
BASE_NAME = VIDEO_NAME.split(".")[0]
OUTPUT_DIR = join(CURRENT_DIR, "output", BASE_NAME)
OUTPUT_IMG = join(OUTPUT_DIR, "img")
OUTPUT_DATA = join(OUTPUT_DIR, BASE_NAME + ".json")
IGNORED_COLORS_PATH = join(ASSETS, "ignored_colors.json")
IGNORED_COLORS = {}

# Dictionary to store extracted data (timestamp -> color in hexadecimal)
DATA = {}

# Attempt to load the JSON file with ignored colors
try:
    with open(IGNORED_COLORS_PATH, "r", encoding="utf-8") as f:
        IGNORED_COLORS = json.load(f)
except Exception as e:
    print("Ignored colors didn't load.")

cap = cv2.VideoCapture(join(ASSETS, VIDEO_NAME))
os.makedirs(OUTPUT_IMG, exist_ok=True)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = int(frame_count / fps * 1000)

current_time = 0

total_frames = int(duration / TIMESKIP)

with tqdm(total=total_frames, desc="Processing frames") as pbar:
    # Loop through the video frames, extracting frames at specified intervals
    while current_time < duration:
        try:
            file_name = join(OUTPUT_IMG, f"{current_time}.jpg")
            cap.set(cv2.CAP_PROP_POS_MSEC, current_time)

            ret, frame = cap.read()

            if not ret:
                print("Failed to read frame.")
                break

            cv2.imwrite(file_name, frame)
            cv2.waitKey()
            ct = ColorThief(file_name)

            # Extract the predominant color from the image
            rgb = ct.get_color(quality=1)

            hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

            # Check if the extracted color is in the ignored colors list
            if hex_color in IGNORED_COLORS:
                print("Ignored color:", hex_color)
                hex_color = "#ffffff"

            DATA[current_time] = hex_color

            current_time += TIMESKIP

            pbar.update(1)

        except Exception as e:
            print(e)
            break

# Save the extracted data to the output JSON file
with open(OUTPUT_DATA, "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=2)

print("OK")
