# Object Detection(객체인식)

### 환경
- Ubuntu 18.04
- yolov3 - tiny? 
    - jetson 보드에 yolov3 너무 무거우니까 tiny 써볼까?

### class
- 사람(kaggle)  ; 1200 = 9 : 1
- 자동차  ; 1200 = 9 : 1
- 나무  ;  학교나무 동영상 프레임별로 잘라보자
- 1공학관  ; 50여장
- 고운관  ; 50여장
~~-본관? ; 생각좀~~

### 데이터 증강 : 1공학관, 고운관
- mean_blur
- brightness +30 -30
- gray_scale
- noise 0.02
- rotation 10 20 350 340 줄일까...?
- 확대? 자르기?


음....증강 후 train/val? 아니면 나눈 후 증강?? 뭘까.....

