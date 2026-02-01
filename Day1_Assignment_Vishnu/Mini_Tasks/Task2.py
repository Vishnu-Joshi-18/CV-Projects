import cv2
import matplotlib.pyplot as plt

filepath = "/Users/vishnu/Downloads/learning_opencv.png"

#I have a doubt - do we read img as grayscale or as BGR and then convert to grayscale ?

gray = cv2.imread(filepath , cv2.IMREAD_GRAYSCALE)
#or 

#gray = cv2.imread(filepath , 0)

# or 
#image = cv2.imread(filepath)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title("Grayscale Image")
axes[0].axis('off')

# Show histogram
axes[1].plot(hist)
axes[1].set_title("Pixel Intensity Histogram")
axes[1].set_xlabel("Intensity Value (0–255)")
axes[1].set_ylabel("Pixel Count")

plt.tight_layout()

plt.savefig("Task2_img.png", dpi=300, bbox_inches="tight")
plt.show()
