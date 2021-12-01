import cv2
import numpy as np

# 두 영상의 차분 영상을 구하는 예
# 차분 계산 시  음수면 0으로 나오게 됨 -> 원하는 결과 x
# 넘파이의 absolute()함수로 해결
# 행렬 절대값 및 차분 연산
image1 = cv2.imread("../images/ch5/abs_test1.jpg", cv2.IMREAD_GRAYSCALE)  # 명암도 영상 읽기
image2 = cv2.imread("../images/ch5/abs_test2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

dif_img1 = cv2.subtract(image1, image2)  # 차분 연산
dif_img2 = cv2.subtract(np.int16(image1), np.int16(image2))  # 음수 보전 위해
abs_dif1 = np.absolute(dif_img2).astype('uint8')
abs_dif2 = cv2.absdiff(image1, image2)  # 차분 절댓값 계산

x, y, w, h = 100, 100, 7, 3

print("[image1 = \n%s\n" % image1[y:y + h, x:x + w])
print("[image2  = \n%s\n" % image2[y:y + h, x:x + w])
print("[dif_img1(roi) uint8] = \n%s\n" % dif_img1[y:y + h, x:x + w])
print("[dif_img2(roi) int16]  = \n%s\n" % dif_img2[y:y + h, x:x + w])
print("[abs_dif1(roi)] = \n%s\n" % abs_dif1[y:y + h, x:x + w])
print("[abs_dif2(roi)] = \n%s\n" % abs_dif2[y:y + h, x:x + w])

titles = ['image1', 'image2', 'dif_img1', 'abs_dif1', 'abs_dif2']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.imshow("dif_img2", dif_img2)
cv2.waitKey(0)
