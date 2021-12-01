
import cv2

img = cv2.imread('./images/final_exam/BSDS_1.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise Exception("영상파일 읽기 에러")

#x,y,p= img.shape
#reshape_img=img.reshape(x*y,p)
#change_img=reshape_img.reshape(x,y,p)
print(([1,2,3,1,0]-2)**2)
print(img.shape)