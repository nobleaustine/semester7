# C. Power-Law Transformation 
# 1. Implement the power-law transformation function with different values of gamma. 
# 2. Apply the power-law transformation to enhance images with different contrast characteristics. 
# 3. Analyze the effect of gamma values on the image appearance, especially for values less than and greater than 1. 
# 4. Experiment with different image types (e.g., medical, satellite, natural) to observe the impact of transformations. 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# power law transformation
def power_law_transform(image, gamma,c=1):
    
    normalized_image = image / 255.0
    transformed_image = c*np.power(normalized_image, gamma)
    transformed_image = np.uint8(transformed_image * 255)
    return transformed_image

# different gamma values
def apply_power_law_transformation(image, gamma_values, title):

    plt.figure(figsize=(10, 10))
    plt.suptitle(title, fontsize=16)
    
    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    

    for i, gamma in enumerate(gamma_values):
        transformed_image = power_law_transform(image, gamma)
        
        plt.subplot(2, 3, i + 2)
        plt.imshow(transformed_image, cmap='gray')
        plt.title(f'Gamma = {gamma}')
        plt.axis('off')
    
    plt.show()

# different types of images
def experiment_with_images(image_paths, gamma_values):
    for i,image_path in enumerate(image_paths):
        
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        title = f"Power-law transformation for {(image_path.split('/')[-1]).split('.')[0]}"
        if i % 2 == 0:
            apply_power_law_transformation(image, gamma_values[0:5], title)
        else:
            apply_power_law_transformation(image, gamma_values[5:], title)


image_paths = [
    '../images/MRI_spine.png',
    '../images/low_contrast_landscape.png', 
    '../images/satellite_image.png',
    '../images/satellite_image.png',
    '../images/CT_brain.png',
    '../images/CT_brain.png'
]

gamma_values = [0.2, 0.3, 0.4, 0.6,1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

experiment_with_images(image_paths, gamma_values)
