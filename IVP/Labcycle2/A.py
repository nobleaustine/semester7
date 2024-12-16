# A. Image Transform 
#   1. Perform Discrete Fourier Transform, Z- transform  KL Transform on a gray scale image. 

# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# from scipy.linalg import eigh
# from matplotlib.gridspec import GridSpec

# def DFT(image):
#     """Compute the Discrete Fourier Transform and return its magnitude spectrum."""
#     dft = np.fft.fft2(image)
#     dft_shift = np.fft.fftshift(dft) 
#     magnitude_spectrum = 20 * np.log(np.abs(dft_shift))
#     return magnitude_spectrum

# def z_transform(image):
#     """Compute the Z-Transform (log scaling for visualization)."""
#     return np.log1p(np.abs(image))

# def KLT(image):
#     # Assume the input image is already grayscale
#     # Step 1: Flatten the image into a 2D array if needed
#     height, width = image.shape
#     flat_image = image.reshape(-1, width)
    
#     # Step 2: Subtract the mean from each column (center the data)
#     mean = np.mean(flat_image, axis=0)
#     centered_data = flat_image - mean
    
#     # Step 3: Compute the covariance matrix
#     covariance_matrix = np.cov(centered_data, rowvar=False)
    
#     # Step 4: Compute the eigenvalues and eigenvectors
#     eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
    
#     # Step 5: Sort eigenvalues and eigenvectors in descending order
#     sorted_indices = np.argsort(eigenvalues)[::-1]
#     eigenvalues = eigenvalues[sorted_indices]
#     eigenvectors = eigenvectors[:, sorted_indices]
    
#     # Step 6: Project the image onto the eigenvectors (new basis)
#     transformed_data = np.dot(centered_data, eigenvectors)
    
#     return transformed_data, eigenvalues, eigenvectors, mean

# def main():
    
#     image = cv2.imread('../images/default_image.png' , cv2.IMREAD_GRAYSCALE)
#     titles = ['Original Image', 'DFT', 'Z-Transform', 'KL Transform']
#     images = []
    
#     images.append(DFT(image))
#     images.append(z_transform(image))
#     images.append(KLT(image))

  
#     for i in range(1, 4):
#         plt.subplot(1, 4, i)
#         plt.imshow(images[i-1], cmap='gray')
#         plt.title(titles[i-1])
#         plt.axis('off')
#     plt.show()

# if __name__ == "__main__":
#     main()
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

print("Perform Discrete Fourier Transform, Z- transform KL Transform on a gray scale image.")

image             = cv2.imread('/home/jarvis/codebase_II/semester7/IVP/images/default_image.png', cv2.IMREAD_GRAYSCALE)
frequencyDomain   = np.fft.fft2(image)
shift             = np.fft.fftshift(frequencyDomain)
magnitudeSpectrum = 20 * np.log(np.abs(shift))
z_transform = np.log(np.abs(frequencyDomain))
flatten           = image.flatten().reshape(-1, 1)
pca               = PCA(n_components=1)
result            = pca.fit_transform(flatten)
result            = result.reshape(image.shape)
plt.figure(figsize=(8, 5))
plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.title('DFT Magnitude Spectrum')
plt.imshow(magnitudeSpectrum, cmap='gray')
plt.axis('off')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.title('KL Transformed Image')
plt.imshow(result, cmap='gray')
plt.axis('off')
plt.show()
