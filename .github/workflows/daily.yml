
import math
import os
import imageio.v2 as imageio
from PIL import Image, ImageDraw, ImageFont

W, H = 720, 1280
FPS, SECONDS = 20, 10
OUT = "videos/daily_workout.mp4"

os.makedirs("videos", exist_ok=True)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 42)
small = ImageFont.truetype(font_path, 28)

writer = imageio.get_writer(
    OUT, fps=FPS, codec="libx264",
    quality=7, macro_block_size=16
)

try:
    for i in range(FPS * SECONDS):
        img = Image.new("RGB", (W, H), (15, 22, 38))
        d = ImageDraw.Draw(img)

        d.text((45, 65), "IRON BOT", font=font, fill=(65, 220, 150))
        d.text((45, 125), "PUSH-UP WORKOUT", font=small, fill="white")
        d.rounded_rectangle((45, 205, 675, 212), radius=3,
                            fill=(65, 220, 150))

        # Animated push-up figure
        phase = (i / FPS) * 2 * math.pi / 2.5
        dip = (1 - math.cos(phase)) / 2
        sy = int(650 + 55 * dip)

        # Head and body
        d.ellipse((165, sy - 28, 215, sy + 22),
                  outline=(255, 205, 150), width=10)
        d.line((215, sy, 440, sy + 12),
               fill=(65, 220, 150), width=20)
        d.line((440, sy + 12, 570, sy + 28),
               fill=(65, 220, 150), width=16)

        # Bent arms
        elbow_x = 300
        elbow_y = sy + 85
        d.line((250, sy + 4, elbow_x, elbow_y),
               fill=(255, 205, 150), width=15)
        d.line((elbow_x, elbow_y, 355, 800),
               fill=(255, 205, 150), width=15)

        # Legs and feet
        d.line((520, sy + 25, 590, 790),
               fill=(255, 205, 150), width=15)
        d.line((590, 790, 635, 790),
               fill=(255, 205, 150), width=15)

        # Floor
        d.line((90, 810, 650, 810),
               fill=(100, 120, 145), width=5)

        d.text((45, 900), "KEEP YOUR BODY STRAIGHT",
               font=small, fill="white")
        d.text((45, 970), "3 SETS  |  CONTROLLED REPS",
               font=small, fill=(65, 220, 150))

        progress = int(620 * (i + 1) / (FPS * SECONDS))
        d.rounded_rectangle((45, 1080, 675, 1095), radius=7,
                            fill=(55, 65, 80))
        d.rounded_rectangle((45, 1080, 45 + progress, 1095),
                            radius=7, fill=(65, 220, 150))
        d.text((45, 1140), "TRAIN SMART. GET STRONGER.",
               font=small, fill="white")

        writer.append_data(img)

finally:
    writer.close()

print(f"Video created: {OUT}")
