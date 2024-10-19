# D. Spatial Filtering 
#  1. Implement mean, median, and Gaussian filters. Apply them to images with different noise types (salt-and-pepper, Gaussian) and compare the results. 
#  2. Design a custom filter for sharpening edges while preserving image details. Apply it to a natural image and evaluate its performance. 
#  3. Experiment with different Laplacian operators (4-connected, 8-connected) and compare their edge detection capabilities. 


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
            plt.subplot(rows, cols, i + 1)
            plt.imshow(image, cmap='gray')
            plt.title(title)
            plt.axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Mean Filter
def apply_mean_filter(image, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    return cv2.filter2D(image, -1, kernel)

# Median Filter
def apply_median_filter(image, kernel_size=3):
    padded_image = np.pad(image, kernel_size // 2, mode='constant')
    output_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_image[i:i + kernel_size, j:j + kernel_size]
            output_image[i, j] = np.median(window)
    
    return output_image

# Gaussian Filter
def apply_gaussian_filter(image, kernel_size=3, sigma=1):
    ax = np.linspace(-(kernel_size // 2), kernel_size // 2, kernel_size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
    kernel = kernel / np.sum(kernel)
    
    return cv2.filter2D(image, -1, kernel)

# Salt and Pepper Noise
def add_salt_and_pepper_noise(image, amount=0.01):
    noisy_image = image.copy()
    num_salt = np.ceil(amount * image.size * 0.5)
    num_pepper = np.ceil(amount * image.size * 0.5)

    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

# Gaussian Noise
def add_gaussian_noise(image, mean=0, sigma=25):
    gaussian_noise = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + gaussian_noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# Sharpening Filter
def sharpen_filter(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

# Laplacian Edge Detection
def apply_laplacian(image, connected_type='4-connected'):
    if connected_type == '4-connected':
        laplacian_kernel = np.array([[0, -1, 0],
                                     [-1, 4, -1],
                                     [0, -1, 0]])
    else:  
        laplacian_kernel = np.array([[-1, -1, -1],
                                     [-1, 8, -1],
                                     [-1, -1, -1]])
    return cv2.filter2D(image, -1, laplacian_kernel)

image = cv2.imread('../images/default_image.png', cv2.IMREAD_GRAYSCALE)

# Add Noise
sp_noise_img = add_salt_and_pepper_noise(image)
gaussian_noise_img = add_gaussian_noise(image)

# Apply Filters
mean_filtered_sp = apply_mean_filter(sp_noise_img)
median_filtered_sp = apply_median_filter(sp_noise_img)
gaussian_filtered_sp = apply_gaussian_filter(sp_noise_img)

mean_filtered_g = apply_mean_filter(gaussian_noise_img)
median_filtered_g = apply_median_filter(gaussian_noise_img)
gaussian_filtered_g = apply_gaussian_filter(gaussian_noise_img)

# Sharpening Filter
sharpened_image = sharpen_filter(image)

# Laplacian Edge Detection
laplacian_4 = apply_laplacian(image, connected_type='4-connected')
laplacian_8 = apply_laplacian(image, connected_type='8-connected')

# Display the Results
show_images([image, sp_noise_img, gaussian_noise_img], ["Original", "Salt & Pepper Noise", "Gaussian Noise"], "Image and Noises")
show_images([mean_filtered_sp, median_filtered_sp, gaussian_filtered_sp, mean_filtered_g, median_filtered_g, gaussian_filtered_g],
            ["Mean Filter", "Median Filter", "Gaussian Filter", "Mean Filter", "Median Filter", "Gaussian Filter"], "Filtered Images")
show_images([image, sharpened_image], ["Original", "Sharpened Image"], "Sharpened Image Comparison")
show_images([laplacian_4, laplacian_8], ["Laplacian (4-connected)", "Laplacian (8-connected)"], "Laplacian Edge Detection")

