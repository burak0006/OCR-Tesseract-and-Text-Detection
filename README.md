## OCR-Tesseract-and-Text-Detection
OCR is undoubtedly a tremendous research field with its numerous applications. There has been extensive research on OCR, particularly the inclusion of deep learning because of its high success rate amongst other approaches. My intent is not to overwhelm you with very complex architectures nor introduce well-known libraries like OCR-Tesseract. But instead, I explained preprocessing stage and share the text recognition code for ID card detection from my [post](https://yldrmburak.medium.com/building-a-ocr-model-from-scratch-using-dl-opencv-for-id-cards-97bf1bd123f)

### Requirements

- MacOS X,Linux or Windows

## Preparation
### Library
- PIL
- OpenCV 2
- matplotlib
- scipy
- pytextractor
- pytesseract

Execute following commands for install library:
```sh
$ pip install opencv-python
$ pip install pytesseract
$ pip install matplotlib
```

### Binarization:
Before delving deeper into our OCR model, I’d like to point out that Jupyter notebook and OpenCV are used in this work. Let’s start with the binarization of the input image.

<img src="https://github.com/burak0006/OCR-Tesseract-and-Text-Detection/blob/2fd6cc405b61e80e11d8e8121d436f3d695eba83/image/index.png" width = "800" height = "300"/>

### Results
Important Note: You need to verify your path where the tesseract engine is installed.
```sh
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract
```

UK DRIVING LICENCE
1. MORGAN
2. SARAH
MEREDYTH
Ze 3. 11.03.1976 UNITED KINGDOM
, da. 04.01.2021 4c. DVLA Sy
) 4b. 31.12.2030
() .. 5 — MORGA753116SMalJ 35 "Aim
ae || *
ea Si AININA rl <<
31
8, 122 BURNS CRESCENT
EDINBURGH
EH1 9GP
9. AM/A/B1/B/BE/f/k/I/n/p/q



