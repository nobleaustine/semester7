
# A. Image Negative 
# 1. Implement the image negative transformation function and apply it to a grayscale image. 
# 2. Analyze the effect of image negative on different types of images (e.g., low contrast, high contrast). 
# 3. Compare the histogram of an original image with its negative.Explain the observed differences. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# load image
def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# negative transformation function
def negative_transform(image):
    return 255 - image

# display images and histograms
def plot_images(original, negative,title):


    plt.figure(figsize=(10, 10))
    plt.suptitle(title, fontsize=16)

    # Original Image
    plt.subplot(2, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Negative Image
    plt.subplot(2, 2, 2)
    plt.imshow(negative, cmap='gray')
    plt.title("Negative Image")
    plt.axis('off')

    # Histogram of Original Image
    plt.subplot(2, 2, 3)
    plt.hist(original.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
    plt.title('Histogram of Original Image')

    # Histogram of Negative Image
    plt.subplot(2, 2, 4)
    plt.hist(negative.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
    plt.title('Histogram of Negative Image')

    plt.tight_layout()
    plt.show()

def process_image(image_path, title):

    original_image = load_image(image_path)
    negative_image = negative_transform(original_image)
    
    plot_images(original_image, negative_image,title)
    

image_path1 = '../images/high_contrast_img.jpg' 
image_path2 = '../images/low_contrast_img.jpeg'   
process_image(image_path1,"High Contrast Image")
process_image(image_path2,"Low Contrast Image")