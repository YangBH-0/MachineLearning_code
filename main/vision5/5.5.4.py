import numpy as np, cv2


def print_rects(rects):
    print("-" * 46)
    print("사각형 원소\t\t랜덤 사각형 정보\t 크기")
    print("-" * 46)
    for i, (x, y, w, h, a) in enumerate(rects):
        print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" % (i, x, y, w, h, a))

rands = np.zeros((5, 5), np.uint16)
starts = cv2.randn(rands[:, :2], 100, 50)
ends = cv2.randn(rands[:, 2:-1], 300, 50)

sizes = cv2.absdiff(starts, ends)  # 가로, 세로 길이 구하기
areas = sizes[:, 0] * sizes[:, 1]  # 넓이
rects = rands.copy()  # 결과 넣을 곳에 사각형 정보 넣기
rects[:, 2:-1] = sizes  # 2,3 열에 가로, 세로 길이 저장
rects[:, -1] = areas  # 마지막 열에 넓이 저장

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()  # 정렬 인덱스

print_rects(rects)  # 원본 사각형 정보
print_rects(rects[idx.astype('int')])  # 정렬 된 사각형 정보
