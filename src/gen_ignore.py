from os.path import join
import os
import json
from colorthief import ColorThief
import cv2

TIMESKIP = 1000

CURRENT_DIR = "src"
ASSETS = "assets"
VIDEO_NAME = "ignored.mp4"
BASE_NAME = VIDEO_NAME.split(".")[0]
OUTPUT_DIR = join(CURRENT_DIR, "output", BASE_NAME)
OUTPUT_IMG = join(OUTPUT_DIR, "img")
OUTPUT_DATA = join(OUTPUT_DIR, "ignored_palette.json")

unique_colors = set()

cap = cv2.VideoCapture(join(ASSETS, VIDEO_NAME))
os.makedirs(OUTPUT_IMG, exist_ok=True)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = int(frame_count / fps * 1000)

current_time = 0

while current_time < duration:
    try:
        file_name = join(OUTPUT_IMG, f"{current_time}.jpg")
        cap.set(cv2.CAP_PROP_POS_MSEC, current_time)

        ret, frame = cap.read()

        cv2.imwrite(file_name, frame)
        cv2.waitKey()
        ct = ColorThief(file_name)

        palette = ct.get_palette(color_count=5)

        for rgb in palette:
            hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
            unique_colors.add(hex_color)

        current_time += TIMESKIP

        print(f"Frame: {int(current_time / TIMESKIP)}")

    except Exception as e:
        print(e)
        break

unique_colors_list = list(unique_colors)

with open(OUTPUT_DATA, "w", encoding="utf-8") as f:
    json.dump(unique_colors_list, f, indent=2)

print("OK")
