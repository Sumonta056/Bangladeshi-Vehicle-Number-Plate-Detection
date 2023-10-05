import cv2
import os  # Import os to create the directory if it doesn't exist

def save_image_with_prefix(image, prefix, output_directory):
    filename = os.path.join(output_directory, f'{prefix}.png')
    cv2.imwrite(filename, image)

def segment_characters(image_path, output_directory):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    save_image_with_prefix(image, '0_original', output_directory)

    # Get the size of the image
    m, n = image.shape

    # Segment the upper portion of the image
    Image1 = image[0:m // 2 + 14, :]
    save_image_with_prefix(Image1, '1_upper_segmented', output_directory)

    # Segment the lower portion of the image
    Image2 = image[(m // 2) + 18:2 * (m // 2), :]
    save_image_with_prefix(Image2, '2_lower_segmented', output_directory)

    # Initialize a list to store segmented characters
    segmented_characters = []

    for img in [Image1, Image2]:
        # Apply connected component labeling
        _, labels = cv2.connectedComponents(img)

        # Get bounding boxes of connected components
        regions = cv2.connectedComponentsWithStats(img)

        # Loop through each connected component
        for label in range(1, regions[0]):
            x, y, w, h, _ = regions[2][label]

            # Draw bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

            # Extract and resize the character
            char = img[y:y + h, x:x + w]
            char = cv2.resize(char, (24, 42))

            segmented_characters.append(char)

    save_image_with_prefix(image, '3_with_bounding_boxes', output_directory)

    return segmented_characters

def display_segmented_characters(segmented_characters):
    for i, char in enumerate(segmented_characters):
        cv2.imshow(f'Segmented Character {i}', char)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Example usage:
image_path = './Step_2_Extraction_Result/Binary Character_5.jpg'  # Replace with your image file path
output_directory = "Step_3_CharacterSegmentation_UpperLower_Result"
os.makedirs(output_directory, exist_ok=True)

segmented_chars = segment_characters(image_path, output_directory)

# Display segmented characters
display_segmented_characters(segmented_chars)
