import numpy as np
import cv2

from skimage.transform import radon


filename = 'ggbaka.png'
# Load file, converting to grayscale
img = cv2.imread(filename)
I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = I.shape
# If the resolution is high, resize the image to reduce processing time.
if (w > 640):
    I = cv2.resize(I, (640, int((h / w) * 640)))
I = I - np.mean(I)  # Demean; make the brightness extend above and below zero
# Do the radon transform
sinogram = radon(I)
# Find the RMS value of each row and find "busiest" rotation,
# where the transform is lined up perfectly with the alternating dark
# text and white lines
r = np.array([np.sqrt(np.mean(np.abs(line) ** 2)) for line in sinogram.transpose()])
rotation = np.argmax(r)
print('Rotation: {:.2f} degrees'.format(90 - rotation))

# Rotate and save with the original resolution
M = cv2.getRotationMatrix2D((w/2, h/2), 90 - rotation, 1)
dst = cv2.warpAffine(img, M, (w, h))
cv2.imshow("rotated.jpg" , dst)
cv2.waitKey(0)


# Convert the image to grayscale
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)

cv2.imwrite('rotated.jpg', gray)