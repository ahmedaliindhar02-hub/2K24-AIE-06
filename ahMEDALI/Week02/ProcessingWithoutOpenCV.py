import numpy as np
def adjust_brightness_contrast (image, alpha=1.0, beta=0):
    """Applies O = alpha * I + beta, then clips tovalid pixel range."""
    adjusted = image.astype(np.float32) * alpha + beta
    return np.clip(adjusted, 0, 255).astype(np.uint8)
#Example : increase contrast and reduce brightness slightly
gray = np.array([[100, 150], [200, 50]], dtype = np.uint8)
result =adjust_brightness_contrast(gray, alpha=1.5, beta=-20)
print(result)