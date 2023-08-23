#0) 라이브러리 선언
import pytesseract

# tessdata_dir_config = '--tessdata-dir "src"'
# pytesseract.image_to_string(front,lang='kor',config=tessdata_dir_config)

# 1) pdf이면 이렇게 하기, 아니면 바로 진행
import pdf2image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


# def ocr_core(file):
#     text = pytesseract.image_to_string(file)
#     return text


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        img.save('page_{}.jpg'.format(pg))


print_pages('sample_input/testPdf.pdf')






import pandas as pd

frame = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(frame)