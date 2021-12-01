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
    x, y, p = data.shape
    data = data.reshape((x * y, p))
    for i in k:

        z = [data[j] for j in range(i)]  # 군집의 중심
        z = np.zeros((i, p))
        for j in range(i):
            z[j] = data[random.randrange(1, data.shape[0])]
        c = [[] for i in range(i)]  # 군집
        print(z.shape)
        k_means_img = np.array(main(data, z, c, i),np.uint8)
        cv2.imshow("{0}".format(i), k_means_img.reshape(x, y, p))
    return c


def main(data, centers, clusters, k):
    x, p = data.shape  # x = 데이터의 길이(x*y), p 해당 화소 값
    while True:
        new_Cluster = [[] for i in range(k)]  # 새로 만든 군집
        dist = [[] for i in range(x)]  # 군집의 중심과 각 점의 거리
        for i in range(k):  # 군집의 중심과 각 픽셀의 거리 구하기
            for j in range(x):
                dist[j].append(euclidean(centers[i], data[j]))
        for i in range(x):  # 군집의 중심들과 점의 거리 중 가장 작은 군집의 중심을 가지고 있는 군집에 넣기
            new_Cluster[dist[i].index(min(dist[i]))].append(data[i].tolist())
        try:
            print(new_Cluster == clusters)
        except:
            print(new_Cluster)
            print(clusters)
        if np.all(new_Cluster == clusters):
            result = []
            for i in range(x):  # 군집의 중심들과 점의 거리 중 가장 작은 군집의 중심을 가지고 있는 군집에 넣기
                result.append(centers[dist[i].index(min(dist[i]))])
            print("군집의 변화가 없음")
            return result
        else:
            clusters = new_Cluster

        for i in range(k):  # 군집의 중심 좌표 갱신
            for j in range(p):
                temp = [i[j] for i in clusters[i]]
                scale = np.mean(temp)
                centers[i][j] = scale

        print("각 군집의 중점 위치")
        for i in range(len(centers)):
            print("z", (i + 1), ":", centers[i])


# print("최종 군집 중심 좌표", z)

img = cv2.imread('../images/final_exam/BSDS_1.png', cv2.IMREAD_COLOR)
if img is None:
    raise Exception("영상파일 읽기 에러")
k_means([2,5,7], img)
cv2.waitKey(0)
