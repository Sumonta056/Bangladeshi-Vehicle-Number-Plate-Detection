import cv2
import numpy as np

# Load the image
image = cv2.imread('result_5.png')
original = image.copy()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Canny edge detection
canny = cv2.Canny(blur, 120, 255, 1)

# Apply dilation to connect nearby contours
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilate = cv2.dilate(canny, kernel, iterations=3)

# Find contours in the dilated image
contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small noise contours
min_area = 5000
filtered_contours = [c for c in contours if cv2.contourArea(c) > min_area]

# Create a copy of the original image to draw contours
result_image = original.copy()

# Draw contours around words
cv2.drawContours(result_image, filtered_contours, -1, (36, 255, 12), 2)

# Save segmented words and display the result
image_number = 0
for c in filtered_contours:
    x, y, w, h = cv2.boundingRect(c)
    ROI = original[y:y+h, x:x+w]
    cv2.imwrite("Word_{}.png".format(image_number), ROI)
    image_number += 1

cv2.imshow('blur', blur)
cv2.imshow('dilate', dilate)
cv2.imshow('canny', canny)
cv2.imshow('image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
