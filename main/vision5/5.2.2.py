import cv2

image = cv2.imread("../images/ch5/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3: raise Exception("컬러영상 아님")

bgr = cv2.split(image)
# b,g,r =cv2.split(image)  3개의 변수에 각각 받기 가능
print("bgr 자료형:", type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소개수:", len(bgr))

cv2.imshow("image", image)
cv2.imshow("Blue Channel", bgr[0])
cv2.imshow("Green Channel", bgr[1])
cv2.imshow("Red Channel", bgr[2])
cv2.waitKey(0)
