import cv2
import numpy as np
title1, title2 = 'originalPicture', 'bayerPicture' # titles

originalPicture = cv2.imread("images/ch5/read_color.jpg", cv2.IMREAD_COLOR) # 원본 영상 불러오기

if originalPicture is None:
    raise Exception("picture loading error")

b, g, r = cv2.split(originalPicture) # B, G ,R 나누기
blankLayer = np.zeros(b.shape, np.uint8) # 검은색 영역 생성

red_mask = np.zeros(r.shape, np.uint8) # R 마스킹 영역 생성
red_mask[0::2, 1::2] = 1
green_mask = np.zeros(g.shape, np.uint8) # G 마스킹 영역 생성
green_mask[1::2, 1::2] = 1
green_mask[0::2, 0::2] = 1
blue_mask = np.zeros(b.shape, np.uint8) # B 마스킹 영역 생성
blue_mask[1::2, 0::2] = 1

b = cv2.add(b, blankLayer, mask=blue_mask) # blue color plane 을 생성
r = cv2.add(r, blankLayer, mask=red_mask) # red color plane 을 생성
g = cv2.add(g, blankLayer, mask=green_mask) # green color plane 을 생성

planeTile = ["redPlane", "greenPlane", "bluePlane"] # plane titles
cv2.imshow(planeTile[0], cv2.merge([blankLayer, blankLayer, r])) # Red color plane 출력
cv2.imshow(planeTile[1], cv2.merge([blankLayer, g, blankLayer])) # Green color plane 출력
cv2.imshow(planeTile[2], cv2.merge([b, blankLayer, blankLayer])) # Blue color plane 출력
bayerPicture = cv2.merge([b, g, r]) # 3개의 plane 을 합쳐 bayer RGB pattern 을 가지는 영상 생성

cv2.imshow(title1, originalPicture) # 원본 영상 출력
cv2.imshow(title2, bayerPicture) # bayer 패턴 영상 출력
cv2.waitKey(0)
