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

def objectiveFun(histogram, histSize, ranges=[0, 256]):
    t = -1
    minSum = 618429491
    print([i * histogram[i] for i in range(histSize)])
    m = np.sum([i * histogram[i] for i in range(histSize)])/np.sum(histogram)
    for i in range(1,ranges[1]):
        left, right = histogram[:i], histogram[i:]
        left_w, right_w = sum(left), sum(right)
        left_m, right_m = sum([i*left[i] for i in range(left.shape[0])])/left_w, sum([(i+j)*right[j] for j in range(right.shape[0])])
        total = sum([left[i]*((i-left_m)**2) for i in range(left.shape[0])])+ sum([right[j]*(((i+j)-right_m)**2) for j in range(right.shape[0])])
        if minSum > total:
            t = i
            minSum = total
    return t

def threshFilter(image, threshhold):
    flat = image.flatten()
    img = np.zeros(flat.shape,np.uint8)
    print(threshhold)

    for i in range(flat.shape[0]):
        if threshhold <= flat[i]:
            img[i]=255
    return img.reshape(image.shape)

img1 = cv2.imread('../images/final_exam/ostu_test_image1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../images/final_exam/ostu_test_image2.png', cv2.IMREAD_GRAYSCALE)
if img1 is None or img2 is None: raise Exception("영상파일 읽기 오류")

hist1= calc_histogram(img1,256)
hist2= calc_histogram(img2,256)
o1 = threshFilter(img1,objectiveFun(hist1,256))
o2 = threshFilter(img2,objectiveFun(hist2,256))

cv2.imshow("origin1", img1)
cv2.imshow("origin2", img2)
cv2.imshow("ostu1",o1)
cv2.imshow("ostu2",o2)
cv2.waitKey(0)
