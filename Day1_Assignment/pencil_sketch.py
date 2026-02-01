import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def is_valid_image(image_path):
    #to check if file exists 
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return False
        
    #to check for extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    if not image_path.lower().endswith(valid_extensions):
        print(f"Error: Invalid image format. Please use {valid_extensions}")
        return False

    #checks if cv2 had a problem reading the image
    image = cv2.imread(image_path)
    if image is None:
        return False

    return True

def pencil_sketch(file_path, blur_kernel=21):
    """
    Convert an image to pencil sketch effect. 
    Returns:
        tuple: (original_rgb, sketch) or (None, None) if error
    """
    # Todo: Implement the algorithm
    # Step 1: Load image
    image = cv2.imread(file_path)
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Step 2: Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Invert grayscale
    inverted_img = 255 - gray
    
    # Step 4: Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_img, (blur_kernel, blur_kernel ), 0)

    # Step 5: Invert blurred image
    inverted_blurred = 255 - blurred
    # Step 6: Divide and scale

    #it gave me error the first time i ran this without converting gray and inverted blurred to np.float32
    gray_f = gray.astype(np.float32)
    inverted_blurred_f = inverted_blurred.astype(np.float32)
    sketch = np.clip( (gray_f * 256) / ( inverted_blurred_f + 1e-6) , 0, 255).astype(np.uint8)
    #1e-6 is added in the denominator so that it is not divided by 0

    return original_rgb, sketch


def display_result(original, sketch, save_path=None):
    """
    Display original and sketch side-by-side.
    
    Args:
        original: Original image (RGB)
        sketch: Sketch image (grayscale)
        save_path: Optional path to save the sketch
    """
    #Todo: Create matplotlib figure with 1 row, 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display original on left, sketch on right

    axes[0].imshow(original)
    # Add titles and remove axes
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(sketch, cmap="gray")
    axes[1].set_title("Pencil Sketch")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()

    # If save_path provided, save the sketch
    if save_path:
        cv2.imwrite(save_path, sketch)
        print(f"Sketch saved at: {save_path}")

def main():
    """Main function to run the pencil sketch converter."""
    # Todo: Get image path from user or command line
    filepath = input("Enter full path of file : ")
    
    # Perform file checking
    if is_valid_image(filepath):

        # Call pencil sketch function
        original, sketch = pencil_sketch(filepath)
        
        if original is not None:
            # Call display_result function
            display_result(original, sketch, save_path="/Users/vishnu/Documents/Vishnu/Programming/College_now/iBot_Learning/CV-sessions/CV-Projects/Day1_Assignment/output_sketch.png")
        else:
            print("Processing error occurred.") 

if __name__ == '__main__':
    main()