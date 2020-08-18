import io
import random
import base64
import os
from werkzeug import secure_filename
from flask import Flask, render_template, url_for, flash, redirect, request, Response, stream_with_context
from flaskMain import app, db, bcrypt
from flaskMain.Forms import *
from flaskMain.Models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
#from .ocr_core import ocr_core
import glob
import docx
#from flask import Flask, Response, render_template, request
from .ocr_core import ocr_core, multi_doc_pipeline, docx_pipeline
from .convert import convert_to_image

UPLOAD_FOLDER = '/flaskMain/static/uploads/'
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv

#pages
@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About Page')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegestrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created for {form.username.data}! You can now Log In', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Log In Failed! Please Check Email and Password', 'danger')
    return render_template('login.html', title='login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='account')

@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template('contact.html', title='Contact Us')



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

            return Response(stream_template('upload.html', extracted_text=stream_with_context(extracted_text)))

    elif request.method == 'GET':
        return render_template('upload.html')

@app.route('/tupload', methods=['GET', 'POST'])
def tupload_page():
    print("Running upload page")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('tupload.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('tupload.html', msg='No file selected')

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

            return Response(stream_template('tupload.html', extracted_text=extracted_text))

    elif request.method == 'GET':
        return render_template('tupload.html')
