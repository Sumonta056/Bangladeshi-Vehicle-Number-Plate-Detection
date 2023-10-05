import cv2
import numpy as np

# Load the image
image = cv2.imread('./Step_2_Extraction_Result/Binary Character_5.jpg')  # Replace with your image file

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)

# Step 1: Apply Sobel operator to detect edges
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the magnitude of gradients
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_magnitude = np.uint8(255 * gradient_magnitude / gradient_magnitude.max())

cv2.imshow('Edge Detection (Sobel)', gradient_magnitude)
cv2.waitKey(0)

# Step 2: Apply Morphological Operations (Filling, Dilation, Filling Again, and Erosion)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Filling (Closing)
closing = cv2.morphologyEx(gradient_magnitude, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Filling (Closing)', closing)
cv2.waitKey(0)

# Dilation
dilated = cv2.dilate(closing, kernel, iterations=7)
cv2.imshow('Dilation', dilated)
cv2.waitKey(0)

# Filling Again (Closing)
closing2 = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Filling Again (Closing)', closing2)
cv2.waitKey(0)

# Erosion
eroded = cv2.erode(closing2, kernel, iterations=1)
cv2.imshow('Erosion', eroded)
cv2.waitKey(0)

# Step 3: Apply Bounding Box Technique for Localization
contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a copy of the original image to draw contours on
result_image = image.copy()

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Bounding Box Localization', result_image)
cv2.waitKey(0)

# Step 4: Extract the Plate Using 'imcrop'
extracted_plate = gray[y:y + h, x:x + w]
cv2.imshow('Extracted Plate', extracted_plate)
cv2.waitKey(0)

# Step 5: Convert to Binary Image using Otsu's Method
_, binary_plate = cv2.threshold(extracted_plate, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Binary Plate", binary_plate)
cv2.waitKey(0)

# Step 6: Resize the License Plate
resized_plate = cv2.resize(binary_plate, (240, int(240 * h / w)))
cv2.imshow("Resized Plate", resized_plate)
cv2.waitKey(0)

# Step 7: Removal of Dust and Unnecessary Objects (Optional)

cv2.destroyAllWindows()
