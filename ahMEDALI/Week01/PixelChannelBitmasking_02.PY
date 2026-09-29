import numpy as np
#Create a dummy 2x2 RGB Image Matrix
img_rgb = np.array([[[255, 0, 0], [0, 255, 0]],
                   [[0, 0,  255], [255, 255, 0]]], dtype=np.uint8)
# Extract Red Channel Only ( Zero in gout G and B)
red_mask = img_rgb.copy()
red_mask[:, :, 1] = 0 # Clear Green
red_mask[:, :, 2] = 0 # Clear Blue

print("Original RGB image:")
print(img_rgb)
print("Red channel mask:")
print(red_mask)
