import pytesseract
import cv2


def read_image(image):
    """
    param: image path
    return parsed string
    """
    # change tesseract destination
    pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    im = cv2.imread(image, 0)
    BLACK = [0, 0, 0]
    fixed = cv2.copyMakeBorder(im, top=30, bottom=30, left=30, right=30, borderType=cv2.BORDER_CONSTANT, value=BLACK)

    return pytesseract.image_to_string(fixed)


if __name__ is "__main__":
    pass


