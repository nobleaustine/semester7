import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob: float, pepper_prob: float):
    noisy_image = np.copy(image)
    total_pixels = image.size
    
    # Add salt noise
    num_salt = np.ceil(salt_prob * total_pixels)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255  # Salt noise

    # Add pepper noise
    num_pepper = np.ceil(pepper_prob * total_pixels)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0  # Pepper noise

    return noisy_image

# Load the image
image_path = '../images/default_image.png' # Replace with your image path
image = cv2.imread(image_path)

# Convert to grayscale (optional)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Add salt and pepper noise
salt_prob = 0.0075  # 5% of the image pixels will be salt
pepper_prob = 0.0075 # 5% of the image pixels will be pepper
noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

# Save the noisy image as PNG
output_path = '../images/noisy_default_image075.png'  # Output path for the noisy image
cv2.imwrite(output_path, noisy_image)


