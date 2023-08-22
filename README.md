현재 미완성, 작업 중입니다. 작동하지 않습니다.

# realEstateOCR
해당 리포지터리는 대한민국의 등기등본 문서에 적합한 OCR 기능을 목표로, Tesseract OCR의 pretrained된 모델의 등기부등본 형식을 Fine-tuning한 레포지토리이다. 표로 이루어진 문서 내용 구성과 한국 주소(한글, 숫자, 기호 등으로 구성)를 정확하게 인식하는 것에 특장점을 지닌다.
표 추출을 위해 OpenCV 라이브러리와 OCR을 위한 Tesseract 프레임워크를 활용하였다.

## Samples
##### 1. Clone this repo.
## Setup

## Inference
1. input 폴더에 등기부등본 파일을 넣는다. (PDF와 PNG 및 JPEG파일 지원)
2. 본 레포지토리의 루트에서 다음 코드를 실행시키면 된다.
````
python tools/infer.py [OPTIONS]
````
## Options
--s h|f|s
내용을 추출할 구역을 설정한다.
````
0 : default(전부)
h : headline(표제부)
f : first(갑구)
s : second(을구)
````
## Train
* 해당 레포지토리는 Tesseract OCR을 활용하여, 이하, 학습을 위해서는 Tesseract OCR의 tesstrain을 사용한다.
1. 
2. 

## How it works
본 레포지토리 내 main.ipynb 파일에서 해당 소프트웨어의 OCR과정을 시각적으로 확인이 가능하다.
## About OCR
