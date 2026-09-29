import numpy as np
def calculate_framebuffer_size(width,height,bpp):
    total_pixels = width*height
    bytes_per_pixel = bpp/8.0
    memory_bytes = total_pixels * bytes_per_pixel
    return memory_bytes / (1024 ** 2) #ConverttoMB
#Calculate1080p24-bitTrueColor
mb = calculate_framebuffer_size(1920, 1080, 24)
print(f"Frame Buffer Size: {mb:.2f} MB")