import numpy as np, cv2

## 행렬 축소 연산
m = np.random.rand(3, 5) * 1000 / 10  # 0~99 실수

reduce_sum = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_SUM)  # dim=0 열방향으로 합 축소 -> 행벡터
reduce_avg = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG)  # dim=1 행방향으로 평균 축소 -> 열벡터
reduce_max = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_MAX)  # dim=0 열방향으로 최대값 축소 -> 행벡터
reduce_min = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_MIN)  # dim=1 행방향으로 최소값 축소 -> 열벡터

print("[m] = \n%s\n" % m)
print("m_reduce_sum] =", reduce_sum.flatten())
print("m_reduce_avg] =", reduce_avg.flatten())
print("m_reduce_max] =", reduce_max.flatten())
print("m_reduce_min] =", reduce_min.flatten())
