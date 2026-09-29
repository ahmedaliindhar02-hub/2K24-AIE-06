from pathlib import Path

import cv2
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
input_path = SCRIPT_DIR / "input.jpg"

# Create a small demo image when no input file has been provided.
if not input_path.exists():
	demo_image = np.zeros((200, 300, 3), dtype=np.uint8)
	demo_image[:, :100] = (0, 0, 255)
	demo_image[:, 100:200] = (0, 255, 0)
	demo_image[:, 200:] = (255, 0, 0)
	cv2.imwrite(str(input_path), demo_image)

# 1. Load an image from disk.
image = cv2.imread(str(input_path))
if image is None:
	raise FileNotFoundError(f"Could not read image: {input_path}")

# 2. Convert the image to grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Apply thresholding (binary mask at cutoff 128).
_, binary_mask = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# 4. Apply a 5x5 blurring filter.
blurred = cv2.blur(gray, (5, 5))

# Save outputs beside this script.
cv2.imwrite(str(SCRIPT_DIR / "output_mask.jpg"), binary_mask)
cv2.imwrite(str(SCRIPT_DIR / "output_blurred.jpg"), blurred)
print(f"Processed image: {input_path}")
print(f"Saved output files in: {SCRIPT_DIR}")