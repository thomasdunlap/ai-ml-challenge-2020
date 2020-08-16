import os
import glob
import docx
from flask import Flask, Response, render_template, request
from ocr_core import ocr_core, multi_doc_pipeline, docx_pipeline
from convert import convert_to_image

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])


app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    print("Running upload page")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file_path = os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            if file.filename[-3:] == 'pdf':
                print("PDF Pipeline")
                convert_to_image(file_path, file_path[:-4])
                print(file_path)
                extracted_text = multi_doc_pipeline(file_path)
            else:
                print("Docx Pipeline")
                extracted_text = docx_pipeline(file_path)
            
            return Response(stream_template('upload.html', extracted_text=extracted_text))
    
    elif request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run()
