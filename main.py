import pyzbar.pyzbar as pyzbar
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('barcode.png')

# plt.imshow(img)
# plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 3채널을 1채널로 변경

# plt.imshow(gray, cmap='gray')
# plt.show()

decoded = pyzbar.decode(gray)   # 바코드를 해석
print(decoded)

