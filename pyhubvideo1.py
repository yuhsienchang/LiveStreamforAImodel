

import cv2
import torch
from PIL import Image
import numpy as np

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # for file/URI/PIL/cv2/np inputs and NMS
model.conf = 0.40  # confidence threshold (0-1)
model.iou = 0.45  # NMS IoU threshold (0-1)

# 讀取攝像頭
cap = cv2.VideoCapture("http://192.168.43.181:8080/?action=stream")
# cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    #cv2.namedWindow('img', cv2.WINDOW_NORMAL)  #正常視窗大小
    
    # Inference 
    results = model(img, size=320)  # includes NMS
    
    # Results
    results = np.array(results.xyxy[0]) # 每幀辨識資訊 ， 如果沒有物件會是[]

    # font style
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    # print(results)
    for i in results:
        (x, y, w, h, cf, nc) = i 
        print(cf)
        nc = int(nc)
        text = str(nc)+": {:.1f}%".format(cf * 100)
        cv2.rectangle(img, (x, y),(w, h), (0, 255, 0), 4)
        cv2.putText(img, text, (x, y), font, 5, (0, 255, 0  ),cv2.LINE_AA, 4)
        
        


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    cv2.imshow('img', img) 


    #print('\n', results.xyxy[0][2][5])  # print img1 predictions 第0張圖, 第二個物件, 第五個值
    #print(len(results.xyxy)) # 一張圖
    #print(len(results.xyxy[0])) # 找到三個物件
    #print(len(results.xyxy[0][0])) # 一個物件有六個值

    #          x1 (pixels)  y1 (pixels)  x2 (pixels)  y2 (pixels)   confidence        class
    # tensor([[7.47613e+02, 4.01168e+01, 1.14978e+03, 7.12016e+02, 8.71210e-01, 0.00000e+00],
    #         [1.17464e+02, 1.96875e+02, 1.00145e+03, 7.11802e+02, 8.08795e-01, 0.00000e+00],
    #         [4.23969e+02, 4.30401e+02, 5.16833e+02, 7.20000e+02, 7.77376e-01, 2.70000e+01],
    #         [9.81310e+02, 3.10712e+02, 1.03111e+03, 4.19273e+02, 2.86850e-01, 2.70000e+01]])
cap.release()
cv2.destroyAllWindows()