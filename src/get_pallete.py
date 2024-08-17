from os.path import join
import os
import json
from colorthief import ColorThief
import cv2

TIMESKIP = 1000

CURRENT_DIR = "src"
ASSETS = "assets"
VIDEO_NAME = "gradient.mp4"
BASE_NAME = VIDEO_NAME.split(".")[0]
OUTPUT_DIR = join(CURRENT_DIR, "output", BASE_NAME)
OUTPUT_IMG = join(OUTPUT_DIR, "img")
OUTPUT_DATA = join(OUTPUT_DIR, BASE_NAME + ".json")
IGNORED_COLORS_PATH = join(ASSETS, "ignored_colors.json")
IGNORED_COLORS = {}

DATA = {}

with open(IGNORED_COLORS_PATH, "r", encoding="utf-8") as f:
    if f:
        try:
            IGNORED_COLORS = json.load(f)
        except Exception as e:
            print("Ignored colors don't load.")

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

        rgb = ct.get_color(quality=1)

        hex = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

        if hex in IGNORED_COLORS:
            print("Ignored color:", hex)
            hex = "#ffffff"

        DATA[current_time] = hex

        current_time += TIMESKIP

        print(f"Frame: {int(current_time / TIMESKIP)}")

    except Exception as e:
        print(e)
        break

with open(OUTPUT_DATA, "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=2)

print("OK")
