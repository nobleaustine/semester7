import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram_matching(source_image, reference_image):
    """
    Perform histogram matching.
    """
    src_hist, src_bins = np.histogram(source_image.flatten(), bins=256, range=[0, 256])
    ref_hist, ref_bins = np.histogram(reference_image.flatten(), bins=256, range=[0, 256])
    
    src_cdf = src_hist.cumsum()
    ref_cdf = ref_hist.cumsum()
    
    src_cdf_normalized = src_cdf / src_cdf[-1]  
    ref_cdf_normalized = ref_cdf / ref_cdf[-1]  
    
   
    lookup_table = np.zeros(256, dtype=np.uint8)
    for src_val in range(256):
        closest_ref_val = np.argmin(np.abs(ref_cdf_normalized - src_cdf_normalized[src_val]))
        lookup_table[src_val] = closest_ref_val
    
    matched_image = lookup_table[source_image]
    
    return matched_image

def histogram_equalization(image):
    """
    Perform histogram equalization.
    """
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    print(bins)
    cdf = histogram.cumsum()
    height, width = image.shape
    cdf_normalized = 255* (cdf/(height * width))
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized).reshape(image.shape)
    
    return np.uint8(equalized_image)

image = cv2.imread("/home/jarvis/codebase_II/semester7/default_image.png", cv2.IMREAD_GRAYSCALE)
equalized_image = histogram_equalization(image)
matched_image = histogram_matching(equalized_image,image)


plt.figure(figsize=(12, 6))
plt.subplot(2,3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis("off")

plt.subplot(2,3, 2)
plt.title("Histogram Equalized Image")
plt.imshow(equalized_image, cmap='gray')
plt.axis("off")

plt.subplot(2,3, 3)
plt.title("Histogram Matched Image")
plt.imshow(matched_image, cmap='gray')
plt.axis("off")

plt.subplot(2,3, 4)
plt.hist(image.ravel(), bins=256, range=(0, 256))
plt.title('Histogram of Original Image')
plt.axis("off")

plt.subplot(2,3, 5)
plt.hist(equalized_image.ravel(), bins=256, range=(0, 256))
plt.title('Histogram of Equalised Image')
plt.axis("off")

plt.subplot(2,3, 6)
plt.hist(matched_image.ravel(), bins=256, range=(0, 256))
plt.title('Histogram of Equalised Image')
plt.axis("off")

plt.tight_layout()
plt.show()
