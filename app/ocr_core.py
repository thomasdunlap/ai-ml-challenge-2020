from PIL import Image, ImageEnhance, ImageFilter
import cv2
import glob
import pytesseract
import time
UPLOAD_PATH = './static/uploads/'

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    #image = convert_from_path(filename)
    print(filename)
    #image = convert_to_image(UPLOAD_PATH + filename, UPLOAD_PATH + filename[:-4])
    im = cv2.imread(filename)
    img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb, config='-c preserve_interword_spaces=1') 
    #text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the images

def multi_doc_pipeline(filename):
    print(filename)
    for im_path in sorted(glob.glob(filename[:-4] + '*.jpg')):
        # call the OCR function on it
        print(f'extracting text from {im_path}')
        extracted_text = ocr_core(im_path)
        print('text extracted')
        
        yield extracted_text
        time.sleep(1)                                    

if __name__ == '__main__':
    print(ocr_core('test'))
