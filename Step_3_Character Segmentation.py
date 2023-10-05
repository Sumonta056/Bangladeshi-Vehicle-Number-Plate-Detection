import cv2
import numpy as np
import os  # Import os to create the directory if it doesn't exist

# Load the image
image = cv2.imread('./Step_2_Extraction_Result/Binary Character_5.jpg')  # Replace with your image file

# Create a directory for saving intermediate images
output_directory = "Step_3_CharacterSegmentation_Result"
os.makedirs(output_directory, exist_ok=True)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join(output_directory, '1_gray.jpg'), gray)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite(os.path.join(output_directory, '2_blur.jpg'), blur)

# Apply Canny edge detection
canny = cv2.Canny(blur, 120, 255, 1)
cv2.imwrite(os.path.join(output_directory, '3_canny.jpg'), canny)

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
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)

    # Filter out small noise contours
    if area > min_char_area:
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a bounding box around the character or word
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract the region of interest (ROI) for the character or word
        roi = gray[y:y + h, x:x + w]

        # Determine if it's a character or word based on size
        if w > 2 * h:
            words.append(roi)
        else:
            characters.append(roi)

# Display the result image with contours
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)

# Save the result image with contours
cv2.imwrite(os.path.join(output_directory, '4_result_with_contours.jpg'), result_image)
cv2.destroyAllWindows()

# Save segmented characters and words
for i, word in enumerate(words):
    cv2.imwrite(os.path.join(output_directory, f'word_{i}.png'), word)

for i, char in enumerate(characters):
    cv2.imwrite(os.path.join(output_directory, f'char_{i}.png'), char)
