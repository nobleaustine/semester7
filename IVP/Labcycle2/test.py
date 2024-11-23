# import matplotlib.pyplot as plt
# from matplotlib.gridspec import GridSpec
# import numpy as np

# def plot_grid_with_spanning(images, spans, titles, cmap='gray'):
#     fig = plt.figure(figsize=(10, 8))
#     grid = GridSpec(3, 3)

#     for image, span, title in zip(images, spans, titles):
#         ax = fig.add_subplot(grid[span[0]:span[0] + span[2], span[1]:span[1] + span[3]])
#         ax.imshow(image, cmap=cmap)
#         ax.set_title(title)
#         ax.axis('off')

#     plt.tight_layout()
#     plt.show()

# # Example data
# image1 = np.random.rand(100, 100)
# image2 = np.random.rand(100, 100)
# image3 = np.random.rand(100, 100)
# image4 = np.random.rand(100, 100)

# spans = [
#     (0, 0, 1, 2), 
#     (0, 2, 1, 1), 
#     (1, 0, 2, 1), 
#     (1, 1, 2, 2)
# ]

# titles = ["Image 1", "Image 2", "Image 3", "Image 4"]


import cv2
import matplotlib.pyplot as plt

def extract_bit_planes(image):
    bit_planes = []
    
    for i in range(8):  
        # Shift the image by `i` positions and mask with `& 1` to extract the i-th bit
        bit_plane = (image >> i) & 1
        bit_planes.append(bit_plane)
    
    return bit_planes

image = cv2.imread('../images/dollar.png' , cv2.IMREAD_GRAYSCALE)

bit_planes = extract_bit_planes(image)

for i, bit_plane in enumerate(bit_planes):
    plt.subplot(2, 4, i+1)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {i+1}')
    plt.axis('off')

plt.tight_layout()
plt.show()