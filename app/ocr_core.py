import cv2
import glob
import pytesseract
import time
from transformers import pipeline
from transformers import PretrainedConfig, TFBertForSequenceClassification, BertTokenizer


MODEL_FOLDER = './static/models/'
UPLOAD_PATH = './static/uploads/'

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True, add_special_tokens=True,
                                                max_length=512, pad_to_max_length=True)
config = PretrainedConfig.from_json_file(MODEL_FOLDER + 'config.json')
model = TFBertForSequenceClassification.from_pretrained(MODEL_FOLDER)


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    print(filename)
    im = cv2.imread(filename)
    img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img_rgb, config='-c preserve_interword_spaces=1') 
    return text  # Then we will print the text in the images

def multi_doc_pipeline(filename):
    print(filename)
    for im_path in sorted(glob.glob(filename[:-4] + '*.jpg')):
        # call the OCR function on it
        print(f'extracting text from {im_path}')
        extracted_text = ocr_core(im_path)
        print('text extracted')
        for clause in extracted_text.split('\n\n'):
            prediction = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, config=config)(clause)
            print(prediction)
            yield clause
            time.sleep(1)                                    

if __name__ == '__main__':
    print(ocr_core('test'))
