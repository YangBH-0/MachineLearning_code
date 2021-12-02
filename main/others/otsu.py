import numpy as np
import cv2


def calc_histogram(image, histSzie, ranges=[0, 256]):
    hist = np.zeros((histSzie, 1), np.float32)
    gap = ranges[1] / histSzie

    for row in image:
        for pix in row:
            idx = int(pix / gap)
            hist[idx] += 1
    return hist


def histo_mean(histogram, ranges=[0, 256]):
    return np.sum([i * histogram[i] for i in range(ranges[0], ranges[1])]) / np.sum(
        [histogram[i] for i in range(ranges[0], ranges[1])])


def histo_variance(histogram, mean, w=1, ranges=[0, 256]):
    histoSum=sum(histogram)
    return sum([((i - mean) ** 2) * (histogram[i] / histoSum) for i in range(ranges[0], ranges[1])]) / w

def objectiveFun(histogram, ranges=[0, 256]):
    threshhold = -1
    minSum = 618429491
    histoSum=sum(histogram) # 픽셀의 모든 갯수(영상의 픽셀수 = 가로 * 세로)
    for t in range(1, ranges[1]): # 가정 변수 t
        left, right = histogram[:t], histogram[t:] # t를 기준으로 나눈 영역
        left_w, right_w = sum(left) / histoSum, sum(right) / histoSum # 각 영역별 가중치(확률)
        left_m, right_m = histo_mean(histogram, [0, t]), histo_mean(histogram, [t, ranges[1]]) # 각 영역별 픽셀 밝기의 평균
        left_d, right_d = histo_variance(histogram, left_m, left_w, [0, t]), histo_variance(histogram, right_m, right_w,
                                                                                  [t, ranges[1]]) # 각 영역별 분산
        total = left_w * left_d + right_w * right_d # 픽셀수 비율로 가중치를 준 각 클래스의 분산의 합산 최소 = 각각의 클래스에 속한 픽셀 값의 분포가 유사도가 높다.
        if minSum > total:
            threshhold = t
            minSum = total
    return threshhold


def threshFilter(image, threshhold):
    flat = image.flatten()
    img = np.zeros(flat.shape, np.uint8)
    print(threshhold)

    for i in range(flat.shape[0]):
        if threshhold <= flat[i]:
            img[i] = 255
    return img.reshape(image.shape)


img1 = cv2.imread('../images/final/ostu_test_image1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../images/final/ostu_test_image2.png', cv2.IMREAD_GRAYSCALE)
if img1 is None or img2 is None: raise Exception("영상파일 읽기 오류")

hist1 = calc_histogram(img1, 256)
hist2 = calc_histogram(img2, 256)
o1 = threshFilter(img1, objectiveFun(hist1))
o2 = threshFilter(img2, objectiveFun(hist2))

cv2.imshow("origin1", img1)
cv2.imshow("origin2", img2)
cv2.imshow("ostu1", o1)
cv2.imshow("ostu2", o2)
cv2.waitKey(0)
