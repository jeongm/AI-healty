# Object Detection(객체인식)

### 환경
- Ubuntu 18.04
- yolov3 - tiny? 
    - jetson 보드에 yolov3 너무 무거우니까 tiny 써볼까?

### class
- 사람(kaggle)  
- 자동차  
- 나무  
- 1공학관  
- 고운관  
~~-본관?~~

### 데이터 증강 : 1공학관, 고운관
- mean_blur
- brightness +30 -30
- gray_scale
- noise 0.02
- rotation 10 20 350 340
