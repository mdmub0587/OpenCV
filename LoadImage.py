import cv2

img = cv2.imread("L-Mello-and-Near.jpg", 1)    # colored Image

img_1 = cv2.imread("L-Mello-and-Near.jpg", 0)    # Black and White Image

# Resizing image

resized_image = cv2.resize(img, (650, 500))
resized_image_1 = cv2.resize(img_1, (int(img_1.shape[1]/2), int(img_1.shape[0]/2)))


# cv2.imread() returns numpy array
print(type(img))
print(img)
print(img.shape)

# showing image
cv2.imshow("Death Note", img)
cv2.imshow("Death Note Resized", resized_image)

cv2.waitKey(0)

cv2.imshow("Death Note", img_1)
cv2.imshow("Death Note resized ", resized_image_1)

cv2.waitKey(0)
cv2.destroyAllWindows()



