# C. Frequency Domain Processing 
# 1. Implement the 2D Discrete Fourier Transform (DFT) and its inverse. 
# 2. Design low-pass, high-pass, and band-pass filters in the frequency domain. Apply them to an 
# image and analyze the results. 
# 3. Implement homomorphic filtering and apply it to an image with uneven illumination. 
# '../images/default_image.png'

import numpy as np
import cv2
import matplotlib.pyplot as plt

def dft_2d(image):
    return np.fft.fftshift(np.fft.fft2(image))

def idft_2d(frequency_image):
    return np.abs(np.fft.ifft2(np.fft.ifftshift(frequency_image)))

def apply_filter(image, filter_mask):
    dft = dft_2d(image)
    filtered_dft = dft * filter_mask
    return idft_2d(filtered_dft)

def low_pass_filter(shape, cutoff):
    center = (shape[0] // 2, shape[1] // 2)
    mask = np.zeros(shape, dtype=np.float32)
    for u in range(shape[0]):
        for v in range(shape[1]):
            if np.sqrt((u - center[0])**2 + (v - center[1])**2) <= cutoff:
                mask[u, v] = 1
    return mask

def high_pass_filter(shape, cutoff):
    return 1 - low_pass_filter(shape, cutoff)

def band_pass_filter(shape, low_cutoff, high_cutoff):
    return low_pass_filter(shape, high_cutoff) - low_pass_filter(shape, low_cutoff)

def homomorphic_filter(image, low_gamma, high_gamma, cutoff, c=1):
    image_log = np.log1p(image)
    dft = dft_2d(image_log)
    shape = image.shape
    center = (shape[0] // 2, shape[1] // 2)
    mask = np.zeros(shape, dtype=np.float32)
    for u in range(shape[0]):
        for v in range(shape[1]):
            d = np.sqrt((u - center[0])**2 + (v - center[1])**2)
            mask[u, v] = (high_gamma - low_gamma) * (1 - np.exp(-c * (d**2 / cutoff**2))) + low_gamma
    filtered_dft = dft * mask
    result = np.exp(idft_2d(filtered_dft)) - 1
    return np.clip(result, 0, 1)

def decompose_image(image, cutoff):
    shape = image.shape
    low_pass = apply_filter(image, low_pass_filter(shape, cutoff))
    reflectance = np.clip(image / (low_pass + 1e-5), 0, 1)
    illumination = np.clip(low_pass, 0, 1)
    return reflectance, illumination

image = cv2.imread('../images/default_image.png', cv2.IMREAD_GRAYSCALE) / 255.0
shape = image.shape
cutoff_low, cutoff_high = 30, 60
low_pass = apply_filter(image, low_pass_filter(shape, cutoff_low))
high_pass = apply_filter(image, high_pass_filter(shape, cutoff_low))
band_pass = apply_filter(image, band_pass_filter(shape, cutoff_low, cutoff_high))
homomorphic = homomorphic_filter(image, 0.5, 2, 30)

reflectance, illumination = decompose_image(image, 30)

results = [image, low_pass, high_pass, band_pass, homomorphic, reflectance, illumination]
titles = ["Original", "Low-Pass", "High-Pass", "Band-Pass", "Homomorphic", "Reflectance", "Illumination"]

plt.figure(figsize=(12, 8))
for i, (result, title) in enumerate(zip(results, titles)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(result, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()