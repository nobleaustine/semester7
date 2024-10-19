# E. Image Enhancement: Arithmetic/Logic Operations 
#  1. Implement image subtraction to detect changes between two images (e.g., before and after an event). 
#  2. Create a simple image watermarking system using image addition and subtraction. 
#  3. Experiment with image averaging to reduce noise in a sequence of images.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_images(images, titles, suptitle=""):
    n = len(images)
    
    if n == 2:
        rows, cols = 1, 2
        fig, axes = plt.subplots(rows, cols, figsize=(10, 5))
        plt.suptitle(suptitle, fontsize=16)
        
        for i, (image, title) in enumerate(zip(images, titles)):
            axes[i].imshow(image, cmap='gray')
            axes[i].set_title(title)
            axes[i].axis('off')
    
    else:
        rows = (n // 3) + (1 if n % 3 != 0 else 0)
        cols = 3

        plt.figure(figsize=(15, 10))
        plt.suptitle(suptitle, fontsize=16)

        for i, (image, title) in enumerate(zip(images, titles)):
            plt.subplot(rows, cols, i+1)
            plt.imshow(image, cmap='gray')
            plt.title(title)
            plt.axis('off')

    plt.show()

def image_subtraction(image1, image2):
    return cv2.absdiff(image1, image2)

def watermark_image(image, watermark, alpha=0.5, apply=False):
    # Resize watermark to match the image dimensions
    watermark_resized = cv2.resize(watermark, (image.shape[1], image.shape[0]))

    if apply:
        # Embed the watermark into the image
        watermarked_image = cv2.addWeighted(image, 1, watermark_resized, alpha, -6)
        return watermarked_image
    else:
        # Remove the watermark from the watermarked image
        # Assuming you have the watermarked image, you'll need to provide it here
        original_image = cv2.addWeighted(image, 1, watermark_resized, -alpha, 6)
        return original_image

def average_images(images):
    
    stacked_images = np.stack(images, axis=0)
    averaged_image = np.mean(stacked_images, axis=0).astype(np.uint8)
    return averaged_image

image_before = cv2.imread('../images/default_image.png', cv2.IMREAD_GRAYSCALE)
image_after = cv2.imread('../images/noisy_default_image.png', cv2.IMREAD_GRAYSCALE)

change_image = image_subtraction(image_before, image_after)

watermark = cv2.imread('../images/water_mark.png', cv2.IMREAD_GRAYSCALE)
watermarked_image = watermark_image(image_before, watermark,apply=True)
extracted_image = watermark_image(watermarked_image, watermark)

image_1= cv2.imread('../images/noisy_default_image010.png', cv2.IMREAD_GRAYSCALE)
image_2= cv2.imread('../images/noisy_default_image050.png', cv2.IMREAD_GRAYSCALE)
image_3= cv2.imread('../images/noisy_default_image075.png', cv2.IMREAD_GRAYSCALE)
image_4= cv2.imread('../images/noisy_default_image100.png', cv2.IMREAD_GRAYSCALE)

image_sequence = [image_1,image_2,image_3,image_4] 
average_image = average_images(image_sequence)

show_images([image_before, image_after, change_image], ["Before", "After", "Change"], "Image Subtraction")
show_images([image_before,watermarked_image, extracted_image], ["Actual Image","Watermarked Image", "Extracted Image"], "Watermarking System")
show_images([image_before,average_image,image_1,image_2,image_3,image_4], ["Actual Image","Averaged Image","Sequence 1","Sequence 2","Sequence 3","Sequence 4"], "Image Averaging")

