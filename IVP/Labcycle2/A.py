# A. Image Transform 
#   1. Perform Discrete Fourier Transform, Z- transform  KL Transform on a gray scale image. 

import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from matplotlib.gridspec import GridSpec

def DFT(image):
    """Compute the Discrete Fourier Transform and return its magnitude spectrum."""
    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft) 
    magnitude_spectrum = 20 * np.log(np.abs(dft_shift))
    return magnitude_spectrum

def z_transform(image):
    """Compute the Z-Transform (log scaling for visualization)."""
    return np.log1p(np.abs(image))

def KLT(image):
    """Compute the KL Transform and return the transformed image."""
    
    image_reshaped = image.astype(float)
    image_cov = np.cov(image_reshaped, rowvar=False)  
    eigenvalues, eigenvectors = eigh(image_cov)
    
    # Sort eigenvalues and eigenvectors in descending order
    sorted_idx = np.argsort(-eigenvalues)
    eigenvalues = eigenvalues[sorted_idx]
    eigenvectors = eigenvectors[:, sorted_idx]
    
    # Reconstruct the image using the most significant eigenvector
    klt_image = np.dot(image_reshaped, eigenvectors[:, :1])  
    return klt_image.T


def display(title, image, position, cmap='gray'):
    """Utility function to plot a single image."""
    plt.subplot(1, 4, position)
    plt.title(title)
    plt.imshow(image, cmap=cmap)
    plt.axis('off')

def display(images, spans, titles, cmap='gray'):
    
    fig = plt.figure(figsize=(10, 8))
    grid = GridSpec(3, 3)

    for image, span, title in zip(images, spans, titles):
        ax = fig.add_subplot(grid[span[0]:span[0] + span[2], span[1]:span[1] + span[3]])
        ax.imshow(image, cmap=cmap)
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

def main():
    
    image = cv2.imread('../images/default_image.png' , cv2.IMREAD_GRAYSCALE)
    
   
    plt.figure(figsize=(15, 5))
    display("Original Image", image, position=1)

    # Compute and plot DFT
    dft_magnitude = DFT(image)
    display("DFT (Magnitude Spectrum)", dft_magnitude, position=2)

    # Compute and plot Z-Transform
    z_transform_image = z_transform(image)
    display("Z-Transform (log scaled)", z_transform_image, position=3)
    

    # Compute and plot KLT
    klt_image = KLT(image)
    display("Z-Transform (log scaled)", klt_image, position=4)
    # plt.figure(figsize=(5, 5))
    # plt.title("KLT Image (First Component)")
    # plt.imshow(klt_image, cmap='gray')
    # plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
