import numpy as np, cv2

m = np.random.randint(0, 100, 15).reshape(3, 5)

m_sort1 = cv2.sortIdx(m, cv2.SORT_EVERY_ROW)  # 행 단위 오름 차순 인덱스 반환
m_sort2 = cv2.sortIdx(m, cv2.SORT_EVERY_COLUMN)  # 열 단위 오름 차순 인덱스 반환
m_sort3 = np.argsort(m, axis=0)  # y축 방향 (열 단위) 인덱스 반환

print("[m1] = \n%s\n" % m)
print("[m_sort1] = \n%s\n" % m_sort1)
print("[m_sort2] = \n%s\n" % m_sort2)
print("[m_sort3] = \n%s\n" % m_sort3)
