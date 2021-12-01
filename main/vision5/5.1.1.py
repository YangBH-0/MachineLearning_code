import cv2


image = cv2.imread("../images/ch5/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류 발생")

x_axis = cv2.flip(image, 0)  # x 축 기준 뒤집기 (상하 뒤집기)
y_axis = cv2.flip(image, 1)  # y 축 기준 뒤집기 (좌우 뒤집기)
xy_axis = cv2.flip(image, -1)  # 양축 기준 뒤집기 (상하좌우 뒤집기)
rep_image = cv2.repeat(image, 1, 2)  # 반복 복사
trans_image = cv2.transpose(image)  # 행렬 전치

## 각 행렬을 영상으로 표시
titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_image', 'trans_image']
for tile in titles:
    cv2.imshow(tile, eval(tile))
cv2.waitKey(0)
