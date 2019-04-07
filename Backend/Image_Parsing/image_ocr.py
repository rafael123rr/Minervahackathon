import pytesseract
import cv2
import urllib.request
import numpy as np


def read_url(image_url):
    """
    param: image path
    return parsed string
    """

    resp = urllib.request.urlopen(image_url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    im = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

   # pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    BLACK = [0, 0, 0]
    fixed = cv2.copyMakeBorder(im, top=30, bottom=30, left=30, right=30, borderType=cv2.BORDER_CONSTANT, value=BLACK)

    return pytesseract.image_to_string(fixed)


def read_path(image_path):

    im = cv2.imread(image_path, 0)
    BLACK = [0, 0, 0]
    fixed = cv2.copyMakeBorder(im, top=30, bottom=30, left=30, right=30, borderType=cv2.BORDER_CONSTANT, value=BLACK)

    return pytesseract.image_to_string(fixed)

if __name__ is "__main__":
    pass


