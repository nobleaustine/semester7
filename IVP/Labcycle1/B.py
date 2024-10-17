# B. Log Transformation 
# 1. Implement the log transformation function and apply it to an image with a narrow range of low gray-level values. 
# 2. Analyze the effect of the log transformation on enhancing details in dark regions of an image. 
# 3. Experiment with different values of the constant 'c' in the log transformation equation and observe the changes in output image. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# load image
def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# log transformation
def log_transform(image, c=1):

    image_float = image.astype(np.float32) # for precision
    log_image = c * np.log(1 + image_float) # log transformation
    log_image_normalized = cv2.normalize(log_image, None, 0, 255, cv2.NORM_MINMAX) # normalize the image

    return np.uint8(log_image_normalized)

def calculate_c_from_image(image):
    max_intensity = np.max(image)
    c = 255 / np.log(1 + max_intensity)
    return c

def plot_images(original, transformed,title):

    plt.figure(figsize=(10, 5))
    plt.suptitle(title, fontsize=16)

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Transformed image
    plt.subplot(1, 2, 2)
    plt.imshow(transformed, cmap='gray')
    plt.title("Log Transformed Image")
    plt.axis('off')

    plt.show()

# compare with different 'c' values
def experiment_with_c(image, c_values,title):

    total_plots = len(c_values) + 1
    
    plt.figure(figsize=(10, 10))
    plt.suptitle(title, fontsize=16)
    
    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')
    
    for i, c in enumerate(c_values):
        transformed_image = log_transform(image, c)
        
        plt.subplot(2, 3, i + 2)
        plt.imshow(transformed_image, cmap='gray')
        plt.title(f"c = {c}")
        plt.axis('off')

    plt.show()

def process_image(image_path):
    original_image = load_image(image_path)
    
    transformed_image = log_transform(original_image, c=1)
    plot_images(original_image, transformed_image, 'Log Transformation')

    c_calc=calculate_c_from_image(original_image)

    c_values = [0.5,1.75,18,50,c_calc]
    experiment_with_c(original_image, c_values,"Different c values")

image_path = '../images/low_contrast_img.jpeg'  
process_image(image_path)
