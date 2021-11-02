## OCR-Tesseract-and-Text-Detection
OCR is undoubtedly a tremendous research field with its numerous applications. There has been extensive research on OCR, particularly the inclusion of deep learning because of its high success rate amongst other approaches. My intent is not to overwhelm you with very complex architectures nor introduce well-known libraries like OCR-Tesseract. But instead, I explained preprocessing stage and share the text recognition code for ID card detection from my post

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

### Binarization:
Before delving deeper into our OCR model, I’d like to point out that Jupyter notebook and OpenCV are used in this work. Let’s start with the binarization of the input image.

