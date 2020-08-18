import cv2
import glob
import pytesseract
import time
import docx
from transformers import pipeline
from transformers import PretrainedConfig, TFBertForSequenceClassification, BertTokenizer

UPLOAD_FOLDER = './flaskMain/static/uploads/'
MODEL_FOLDER = './flaskMain/static/models/'
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])
label_converter = {'LABEL_0': 'ACCEPTABLE', 'LABEL_1': 'UNACCEPTABLE'}
config = PretrainedConfig.from_json_file(MODEL_FOLDER + 'config.json')
model = TFBertForSequenceClassification.from_pretrained(MODEL_FOLDER)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                                        do_lower_case=True,
                                        add_special_tokens=True,
                                        max_length=512,
                                        pad_to_max_length=True)



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
            if len(clause) < 4:
                continue

            prediction = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, config=config)(clause)
            print(prediction)
            accept = label_converter[prediction[0]['label']]
            prob = prediction[0]['score']

            yield clause, accept, prob
            time.sleep(1)

def docx_pipeline(docx_path):
    document = docx.Document(docx_path)
    for paragraph in document.paragraphs:
        if len(paragraph.text) < 4:
            continue
        prediction = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, config=config)(paragraph.text)
        print(prediction)
        accept = label_converter[prediction[0]['label']]
        prob = prediction[0]['score']
        yield paragraph.text, accept, prob
        time.sleep(1)

if __name__ == '__main__':
    print(ocr_core('test'))
