from matplotlib.pyplot import imshow
import cv2
import matplotlib.pyplot as plt
from pytextractor import pytextractor
import pytesseract


class OCR:
    '''OCR using Tesseract Engine
    Parameters
    ------------------------------
    path          : image path
    threshed_image: binarized image
    '''

    @staticmethod
    def contour_extraction(threshed_image,img):
        '''Finding text character contours'''
        # contour extraction 
        contours, hierarchy = cv2.findContours(threshed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        ind = 0
        min_char_width = 1 
        max_char_width = 30
        min_char_height = 5 
        max_char_height = 80
        # finding x,y,w,h coordinates
        for cont in contours: 
            x,y,w,h = cv2.boundingRect(cont)

            if min_char_width<w<max_char_width and min_char_height<h<max_char_height:

                newimg = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)
                # to save characters for further processing 
                # letterimage = img[y-2:y+h+2,x-2:x+w+2]
                # kernel = np.ones((2,2),np.uint8)
                # image_name = 'characters'+str(ind)+'.jpg'
                # cv2.imwrite(image_name,letterimage)
                # ind+=1         
        plt.imshow(newimg)

    @staticmethod
    def detect_and_extract_text(path):
        '''Image read and processing'''
        # Image read and conversion to gray
        img = cv2.imread(path)
        img_org = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Binarization of gray scaled image
        r,threshed = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)   
        kernel = np.ones((1,1),np.uint8)
        final_th= cv2.dilate(threshed,kernel,iterations = 1)

        plt.figure(figsize=(16, 6))
        plt.subplot(121),plt.imshow(img_org)
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(final_th,cmap = 'gray')
        plt.title('Binarized Image'), plt.xticks([]), plt.yticks([])
        
        # text extraction using pytesseract
        extractor = pytextractor.PyTextractor()
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
        #extractor.get_image_text(path,width=320,height=320, display=True, numbers=True,
        #                     confidence=0.5, percentage=2.0, 
        #                     min_boxes=1, max_iterations=20)
        custom_config = r'--oem 3 --psm 6'
        return pytesseract.image_to_string(path, config=custom_config)
    
if __name__ == '__main__':
    path = 'sarah.jpg'
    print(OCR.detect_and_extract_text(path))