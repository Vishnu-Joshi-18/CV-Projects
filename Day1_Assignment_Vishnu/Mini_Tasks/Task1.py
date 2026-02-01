import cv2

image_path = "/Users/vishnu/Downloads/learning_opencv.png"

image = cv2.imread(image_path)
corrected_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Gaussian Blur
blur_gaussian = cv2.GaussianBlur(image, (9, 9), 0)
blur_gaussian_converted_to_rgb = cv2.cvtColor(blur_gaussian, cv2.COLOR_BGR2RGB)

#Canny Edge detection 
#First will convert to grayscale, blur , and then Canny

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)


#Binary Thresholding
#not the same as Grayscale
#either white or black

returned_value , binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


#To Display results 

import matplotlib.pyplot as plt

images = [corrected_img, blur_gaussian_converted_to_rgb, edges, binary_img ]
titles = ['Original', 'Gaussian Blur', 'Canny Edge', 'Binary Thresholding']

fig, axes = plt.subplots(2, 2, figsize=(10, 7))

for img, title, ax in zip(images, titles, axes.ravel() ):
    ax.imshow(img , cmap ="gray")
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()

plt.savefig("Task1_img.png", dpi=300, bbox_inches="tight")
plt.show()

