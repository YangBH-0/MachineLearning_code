import copy
import math, numpy as np
import random

import cv2


# x = [(18, 5), (20, 9), (20, 14), (20, 18), (5, 15), (9, 15), (6, 20)]  # 데이터
# k = 3  # 군집의 수
# C = [[] for i in range(k)]  # 군집
# z = [x[i] for i in range(k)]  # 군집의 중심
# print("초기 군집 중심:", z)


def euclidean(a, b):  # 유클리드 거리 구하는 함수
    if (len(a) == len(b)):  # 같은 차원만 가능
        sum = 0
        for i in range(len(a)):
            sum += ((a[i] - b[i]) ** 2)  # 각각의 차에 제곱
        return math.sqrt(sum)  # 유클리드 공식을 이용하여 계산 후 반환
    else:  # 아니면 -1으로 반환
        print(a.shape)
        print(b.shape)
        print("두 점이 서로 다른 차원입니다.")
        return -1


def k_means(k, data):
    result=[]
    x, y, p = data.shape
    data = data.reshape((x * y, p))
    for i in k:
        centers = np.zeros((i, p)) # 군집의 중심 크기 설정
        for j in range(i): # 군집의 중심 랜덤 픽셀로 초기화
            centers[j] = data[random.randrange(0, data.shape[0])]
        clusters = [[] for i in range(i)]  # 군집
        print(centers.shape)
        k_means_img = np.array(main(data, centers, clusters, i),np.uint8)
        result.append(k_means_img.reshape(x, y, p))
    return result

def main(data, centers, clusters, k):
    len, p = data.shape  # len = 데이터의 길이(len*y), p 해당 화소 값
    while True:
        print("각 군집의 중점 위치")
        for i in range(k):
            print("z", (i + 1), ":", centers[i])
        new_Cluster = [[] for i in range(k)]  # 새로 만든 군집
        for i in range(len): # 군집 생성
            dist=[]
            for j in range(k):
                dist.append(euclidean(centers[j],data[i])) # 군집의 중심과 점의 거리 구하기
            new_Cluster[dist.index(min(dist))].append(i) # 군집의 중심들과 점의 거리 중 가장 작은 군집의 중심을 가지고 있는 군집에 넣기

        if new_Cluster == clusters:
            result=copy.deepcopy(data)
            for i in range(k):
                for index in clusters[i]: # 군집에 있는 데이터 인덱스 번호 추출
                    result[index]=centers[i] # 해당 군집에 있는 데이터의 값을 군집의 중심으로 바꾸기
            print("군집의 변화가 없음")
            return result
        else:
            clusters = new_Cluster

        for i in range(k):  # 군집의 중심 좌표 갱신
            for j in range(p):
                temp = [data[index][j] for index in clusters[i]]
                scale = np.mean(temp)
                centers[i][j] = scale
            if centers[i][j] == np.nan: # 만약 중복된 픽셀 값 시 오류 처리
                centers[i]=data[random.randrange(0,len)]


# print("최종 군집 중심 좌표", z)

img = cv2.imread('../images/final/BSDS_1.png', cv2.IMREAD_COLOR)
#img2= cv2.imread('../images/final/BSDS_2.png', cv2.IMREAD_COLOR)
#img3 = cv2.imread('../images/final/BSDS3.png', cv2.IMREAD_COLOR)
if img is None:
    raise Exception("영상파일 읽기 에러")
k=[2,5,7]
r1 = k_means(k, img)
#k_means(k, img2)
#k_means(k, img3)
cv2.imshow("img",img)
for i in range(len(r1)):
    cv2.imshow("{0}".format(k[i]), r1[i])
#cv2.imshow(img2)
#cv2.imshow(img3)
cv2.waitKey(0)
