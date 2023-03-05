#Nama : Agym Mahaputra Romy Barlianta
#NIM  : F55121076
import cv2
import matplotlib.pyplot as plt

#picture low contrast equalization
img_low_contrast = cv2.imread('low.png', 0)
equalized_low_contrast = cv2.equalizeHist(img_low_contrast)
histogram_low = cv2.calcHist([img_low_contrast], [0], None, [256], [0, 256])
equalized_histogram_low = cv2.calcHist([equalized_low_contrast], [0], None, [256], [0, 256])
plt.subplot(2, 2, 1)
plt.imshow(img_low_contrast, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.imshow(equalized_low_contrast, cmap='gray')
plt.title('Gambar Equalization')
plt.subplot(2, 2, 3)
plt.plot(histogram_low, color='gray')
plt.title("Histogram Gambar Asli")
plt.xlabel('Intensitas Piexels')
plt.ylabel('Jumlah pixels')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram_low, color='gray')
plt.title('Histogram Gambar Equalization')
plt.xlabel('Intensitas Pixels')
plt.ylabel('Jumlah Pixels')

#picture normal contrast equalization
img_normal_contrast = cv2.imread('normal.png', 0)
equalized_normal_contrast = cv2.equalizeHist(img_normal_contrast)
histogram_normal = cv2.calcHist([img_normal_contrast], [0], None, [256], [0, 256])
equalized_histogram_normal = cv2.calcHist([equalized_normal_contrast], [0], None, [256], [0, 256])
plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img_normal_contrast, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.imshow(equalized_normal_contrast, cmap='gray')
plt.title('Gambar Equalization')
plt.subplot(2, 2, 3)
plt.plot(histogram_normal, color='gray')
plt.title("Histogram Gambar Asli")
plt.xlabel('Intensitas Piexels')
plt.ylabel('Jumlah pixels')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram_normal, color='gray')
plt.title('Histogram Gambar Equalization')
plt.xlabel('Intensitas Pixels')
plt.ylabel('Jumlah Pixels')

#picture high contrast equalization
img_high_contrast = cv2.imread('high.png', 0)
equalized_high_contrast = cv2.equalizeHist(img_high_contrast)
histogram_high = cv2.calcHist([img_high_contrast], [0], None, [256], [0, 256])
equalized_histogram_high = cv2.calcHist([equalized_high_contrast], [0], None, [256], [0, 256])
plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img_high_contrast, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.imshow(equalized_high_contrast, cmap='gray')
plt.title('Gambar Equalization')
plt.subplot(2, 2, 3)
plt.plot(histogram_high, color='gray')
plt.title("Histogram Gambar Asli")
plt.xlabel('Intensitas Piexels')
plt.ylabel('Jumlah pixels')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram_high, color='gray')
plt.title('Histogram Gambar Equalization')
plt.xlabel('Intensitas Pixels')
plt.ylabel('Jumlah Pixels')


plt.show()