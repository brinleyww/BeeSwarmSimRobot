import cv2

sample_image = cv2.imread("sample.png")
print(sample_image[6,1558])  # 99 106 107
print(sample_image[6,1996])  # 99 106 107

sample_image2 = cv2.imread("sample2.png")
print(sample_image2[6,1558])  # 37  13 244]
print(sample_image2[6,1996])  # 37  13 244]
print(sample_image2[6,1558][2])