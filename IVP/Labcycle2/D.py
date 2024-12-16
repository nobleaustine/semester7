import cv2
import numpy as np
import matplotlib.pyplot as plt

# RGB to HSI Conversion
def rgb_to_hsi(image):
    image = image / 255.0
    R, G, B = image[..., 0], image[..., 1], image[..., 2]
    intensity = (R + G + B) / 3
    saturation = 1 - 3 * np.minimum(R, np.minimum(G, B)) / (R + G + B + 1e-5)
    hue = np.arccos((0.5 * ((R - G) + (R - B))) / (np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-5))
    hue[B > G] = 2 * np.pi - hue[B > G]
    return np.stack((hue / (2 * np.pi), saturation, intensity), axis=-1)

# HSI to RGB Conversion
def hsi_to_rgb(image):
    H, S, I = image[..., 0] * 2 * np.pi, image[..., 1], image[..., 2]
    R, G, B = np.zeros_like(H), np.zeros_like(H), np.zeros_like(H)
    sector = (H / (2 * np.pi / 3)).astype(int)
    f = H % (2 * np.pi / 3)
    p = I * (1 - S)
    q = I * (1 - S * f / (2 * np.pi / 3))
    t = I * (1 - S * (1 - f / (2 * np.pi / 3)))
    for i in range(3):
        mask = (sector == i)
        if i == 0:
            R[mask], G[mask], B[mask] = I[mask], t[mask], p[mask]
        elif i == 1:
            R[mask], G[mask], B[mask] = q[mask], I[mask], p[mask]
        else:
            R[mask], G[mask], B[mask] = p[mask], I[mask], t[mask]
    return np.clip(np.stack((R, G, B), axis=-1) * 255, 0, 255).astype(np.uint8)

# Color Histogram Equalization
def equalize_color_histogram(image):
    channels = cv2.split(image)
    equalized_channels = [cv2.equalizeHist(channel) for channel in channels]
    return cv2.merge(equalized_channels)

# Color Edge Detection
def color_edge_detection(image, method='sobel'):
    edges = []
    for i in range(3):  # Apply edge detection to each channel
        if method == 'sobel':
            dx = cv2.Sobel(image[..., i], cv2.CV_64F, 1, 0, ksize=3)
            dy = cv2.Sobel(image[..., i], cv2.CV_64F, 0, 1, ksize=3)
            edges.append(cv2.magnitude(dx, dy))
        elif method == 'canny':
            edges.append(cv2.Canny(image[..., i], 100, 200))
    return np.max(edges, axis=0)

# Input Image
image = cv2.cvtColor(cv2.imread('example.jpg'), cv2.COLOR_BGR2RGB)

# Conversions
hsi_image = rgb_to_hsi(image)
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)

# Equalization
equalized_image = equalize_color_histogram(cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb))
equalized_image = cv2.cvtColor(equalized_image, cv2.COLOR_YCrCb2RGB)

# Edge Detection
sobel_edges = color_edge_detection(image, method='sobel')
canny_edges = color_edge_detection(image, method='canny')

# Visualization
results = [image, hsi_image[..., 2], ycbcr_image[..., 0], equalized_image, sobel_edges, canny_edges]
titles = ['Original', 'HSI Intensity', 'YCbCr Luma', 'Histogram Equalized', 'Sobel Edges', 'Canny Edges']

plt.figure(figsize=(12, 8))
for i, (result, title) in enumerate(zip(results, titles)):
    plt.subplot(2, 3, i + 1)
    cmap = 'gray' if len(result.shape) == 2 else None
    plt.imshow(result, cmap=cmap)
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
# converted_image = cv2.cvtColor(src, code)
