


# import cv2
# import matplotlib.pyplot as plt

# def extract_bit_planes(image):
#     bit_planes = []
    
#     for i in range(8):  
#         # Shift the image by `i` positions and mask with `& 1` to extract the i-th bit
#         bit_plane = (image >> i) & 1
#         bit_planes.append(bit_plane)
    
#     return bit_planes

# image = cv2.imread('../images/dollar.png' , cv2.IMREAD_GRAYSCALE)

# bit_planes = extract_bit_planes(image)

# for i, bit_plane in enumerate(bit_planes):
#     plt.subplot(2, 4, i+1)
#     plt.imshow(bit_plane, cmap='gray')
#     plt.title(f'Bit Plane {i+1}')
#     plt.axis('off')

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import cv2

import numpy as np
import cv2
import matplotlib.pyplot as plt

def z_transform_2d_matrix(image, z1, z2):
    """
    Compute the 2D Z-transform of an image and return a matrix of contributions.
    Parameters:
        image: ndarray
            Input 2D discrete signal (grayscale image).
        z1: complex
            Z-domain value for the first dimension.
        z2: complex
            Z-domain value for the second dimension.
    Returns:
        z_matrix: ndarray
            A matrix where each element is the contribution to the Z-transform, rescaled for visualization.
        Z_transform: complex
            The Z-transform of the 2D signal at (z1, z2) (sum of all elements in z_matrix).
    """
    M1, M2 = image.shape
    z_matrix = np.zeros((M1, M2), dtype=complex)

    for z1 in range(M1):
        for z2 in range(M2):
            z_matrix[z1, z2] = np.sum([image[n1, n2] * (z1 ** -n1) * (z2 ** -n2) for n1 in range(M1) for n2 in range(M2)])
    
    Z_transform = np.sum(z_matrix)  # Sum all elements to get the Z-transform

    # Rescale the magnitude for visualization
    magnitude = np.abs(z_matrix)
    magnitude_log = np.log1p(magnitude)  # Apply log transformation
    magnitude_rescaled = 255 * (magnitude_log - magnitude_log.min()) / (magnitude_log.max() - magnitude_log.min())
    
    return magnitude_rescaled.astype(np.uint8), Z_transform

# Load the image
image = cv2.imread('../images/default_image.png', cv2.IMREAD_GRAYSCALE)

# Ensure the image is loaded correctly
if image is None:
    raise FileNotFoundError("The image file was not found. Check the path.")

# Normalize the image for numerical stability
image = image.astype(np.float64) / 255.0

# Define Z-domain values
z1 = 0.9 + 0.1j  # Example complex value for z1
z2 = 0.8 + 0.2j  # Example complex value for z2

# Compute the 2D Z-transform contributions matrix and the final Z-transform
z_matrix_rescaled, Z_value = z_transform_2d_matrix(image, z1, z2)

# Print the final Z-transform value
print(f"The 2D Z-transform of the image at (z1={z1}, z2={z2}) is: {Z_value}")

# Visualize the rescaled Z-transform contributions matrix
plt.figure(figsize=(8, 6))
plt.title("Rescaled Log-Magnitude of Z-transform Contributions Matrix")
plt.imshow(z_matrix_rescaled, cmap='gray')
plt.colorbar(label='Intensity')
plt.xlabel("n2 (Columns)")
plt.ylabel("n1 (Rows)")
plt.show()
