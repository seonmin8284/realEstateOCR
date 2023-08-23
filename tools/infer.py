tessdata_dir_config = '--tessdata-dir "src"'
pytesseract.image_to_string(front,lang='kor',config=tessdata_dir_config)