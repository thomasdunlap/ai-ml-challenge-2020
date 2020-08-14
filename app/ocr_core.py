try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from convert import convert_to_image, run_cpp

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    #image = convert_from_path(filename)
    print(filename)
    image = convert_to_image('./static/uploads/' + filename, './static/uploads/' + filename[:-4])
    text = pytesseract.image_to_string(Image.open('static/uploads/' + filename[:-4] + '.png')) 
    #text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image

if __name__ == '__main__':
    print(ocr_core('test'))
