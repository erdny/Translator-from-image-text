from PIL import Image
import pytesseract
import argparse
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


class Reader:
    
    def __init__(self):
        
        self.filePath = ''
        self.content = ''

    def setFilePath(self,file_path):
        
        self.filePath = file_path
        

    def extractText(self):
        
        image = cv2.imread(self.filePath)
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        image_gray = cv2.medianBlur(image_gray, 3)
        filename = "{}.png".format(os.getpid())
        folder = 'C:\\Users\\Erdenay\\Desktop\\translatorProject\\'
        path = folder + filename
        cv2.imwrite(path, image_gray)
        text = pytesseract.image_to_string(Image.open(path), lang = 'eng')
        self.content = text
        print(self.content)




    def getText(self):
        self.extractText()
        return self.content
    
