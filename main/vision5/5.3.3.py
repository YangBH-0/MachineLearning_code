import numpy as np, cv2

x = np.array([1, 2, 3, 5, 10], np.float32)
y = np.array([2, 5, 7, 2, 9]).astype("float32")

mag = cv2.magnitude(x, y)  # 크기 계산
ang = cv2.phase(x, y)  # 각도(방향) 계산
p_mag, p_ang = cv2.cartToPolar(x, y)  # 크기와 각도 계산
x2, y2 = cv2.polarToCart(p_mag, p_ang)  # 크기와 각도로 좌표 계산

print("[x] 형태: %s 원소: %s" % (x.shape, x))
print("[y] 형태: %s 원소: %s" % (y.shape, y))
print("[mag] 형태: %s 원소: %s" % (mag.shape, mag))

print("[m_mag] =%s" % mag.T)  # 행렬 전치
print("[p_mag] =%s" % np.ravel(p_mag))
print("[p_ang] =%s" % np.ravel(p_ang))
print("[x_mat2] =%s" % x2.flatten())
print("[y_mat2] =%s" % y2.flatten())
