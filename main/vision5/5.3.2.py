import numpy as np, cv2

v1 = np.array([1, 2, 3], np.float32)  # 1차원 리스트 행렬 생성
v2 = np.array([[1], [2], [3]], np.float32)  # 2차원 리스트 행렬(3행,1열) 생성 - 열 벡터
v3 = np.array([[1, 2, 3, ]], np.float32)  # 2차원 리스트 행렬(1행, 3열) 생성 - 행 벡터

v1_exp = cv2.exp(v1)  # 지수 계산
v2_exp = cv2.exp(v2)
v3_exp = cv2.exp(v3)
v_log = cv2.log(v1)  # 로그 계산
m_sqrt = cv2.sqrt(v2)  # 제곱근 계산
m_pow = cv2.pow(v3, 3)  # 3의 거듭 제곱 [1^3,2^3,3^3]

print("[v1] 형태: %s 원소: %s" % (v1.shape, v1))
print("[v2] 형태: %s 원소: %s" % (v2.shape, v2))
print("[v3] 형태: %s 원소: %s" % (v3.shape, v3))
print()

print("[v1_exp] 형태: %s 원소: %s" % (v1_exp.shape, v1_exp))
print("[v2_exp] 형태: %s 원소: %s" % (v2_exp.shape, v2_exp))
print("[v3_exp] 형태: %s 원소: %s" % (v3_exp.shape, v3_exp))
print()

print("[log] =", v_log.T)
print("[sqrt] =", np.ravel(m_sqrt))
print("[pow] =", m_pow.flatten())
