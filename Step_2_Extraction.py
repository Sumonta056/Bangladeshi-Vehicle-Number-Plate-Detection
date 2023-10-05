import cv2
import numpy as np
import os  # Import the os module for working with file paths

# Load the image
image = cv2.imread('./Step_1_Rotation_Result/step_rotated.jpg')  # Replace with your image file

# Create a directory to save the images
output_dir = 'Step_2_Extraction_Result'
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Function to save an image with a unique name in the output directory
def save_image(image, step_name, index):
    filename = os.path.join(output_dir, f"{step_name}_{index}.jpg")
    cv2.imwrite(filename, image)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
save_image(gray, 'grayscale', 1)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)

# Step 1: Apply Sobel operator to detect edges
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the magnitude of gradients
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_magnitude = np.uint8(255 * gradient_magnitude / gradient_magnitude.max())

save_image(gradient_magnitude, 'edge_detection_sobel', 2)
cv2.imshow('Edge Detection (Sobel)', gradient_magnitude)
cv2.waitKey(0)

# Step 2: Apply Morphological Operations (Filling, Dilation, Filling Again, and Erosion)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Filling (Closing)
closing = cv2.morphologyEx(gradient_magnitude, cv2.MORPH_CLOSE, kernel)
save_image(closing, 'filling_closing', 3)
cv2.imshow('Filling (Closing)', closing)
cv2.waitKey(0)

# Dilation
dilated = cv2.dilate(closing, kernel, iterations=7)
save_image(dilated, 'dilation', 4)
cv2.imshow('Dilation', dilated)
cv2.waitKey(0)

# Filling Again (Closing)
closing2 = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
save_image(closing2, 'filling_again_closing', 5)
cv2.imshow('Filling Again (Closing)', closing2)
cv2.waitKey(0)

# Erosion
eroded = cv2.erode(closing2, kernel, iterations=1)
save_image(eroded, 'erosion', 6)
cv2.imshow('Erosion', eroded)
cv2.waitKey(0)

# Convert the image to grayscale again
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)
save_image(blur, 'gaussian_blur', 7)

# Apply Canny edge detection
canny = cv2.Canny(blur, 120, 255, 1)
save_image(canny, 'canny_edge', 8)

# Find contours in the canny edge-detected image
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image to draw contours on
result_image = image.copy()

# Create lists to store words and characters
words = []
characters = []

# Set a minimum area threshold for character segmentation
min_char_area = 100

# Loop through the detected contours
for i, contour in enumerate(contours):
    # Calculate the area of the contour
    area = cv2.contourArea(contour)

    # Filter out small noise contours
    if area > min_char_area:
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a bounding box around the character or word
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract the region of interest (ROI) for the character or word
        extracted_character = image[y:y + h, x:x + w]

        # Determine if it's a character or word based on size
        if w > 2 * h:
            words.append(extracted_character)
        else:
            characters.append(extracted_character)

        cv2.imshow('Result Image', extracted_character)
        save_image(extracted_character, 'Result Image', 5)
        cv2.waitKey(0)

        # Convert the extracted character to grayscale
        extracted_character_gray = cv2.cvtColor(extracted_character, cv2.COLOR_BGR2GRAY)

        # Apply Binary Threshold using Otsu's Method
        _, binary_plate = cv2.threshold(extracted_character_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow(f"Binary Character {i}", binary_plate)
        save_image(binary_plate, 'Binary Character', 5)
        cv2.waitKey(0)

        # Resize the License Plate
        resized_character = cv2.resize(binary_plate, (240, int(240 * h / w)))
        cv2.imshow(f"Resized Character {i}", resized_character)
        cv2.waitKey(0)

        filename = os.path.join(output_dir, f"result_{i + 1}.jpg")
        cv2.imwrite(filename, resized_character)

# Display the result image with contours

# Step 8: Removal of Dust and Unnecessary Objects (Optional)

cv2.destroyAllWindows()
