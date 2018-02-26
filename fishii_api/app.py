from flask import Flask, request, jsonify, g, send_from_directory, url_for, render_template, redirect, flash, abort
from werkzeug.utils import secure_filename
import sys
import os
import sqlite3 
from PIL import Image
import numpy as np
# add parent to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fishii_model.keras_model.model as modelPkg

# load model 
model = modelPkg.Model().model


UPLOAD_FOLDER = "./images"
ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png"]

app = app = Flask(__name__, static_folder='public')  


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({"error": "file not found, field name should be 'file'"})
            # return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return jsonify({"error": "file name empty"})

            # return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = app.config['UPLOAD_FOLDER']
            fullpath = os.path.join(filepath, filename)
            file.save(fullpath)

            # f = Image.open(fullpath)

            # img_as_arr = np.array(f.resize((256,256)))

            # img_as_arr = img_as_arr.reshape(1, 256, 256, 3)
            
            # preds = model.predict(img_as_arr)
            # use filepath and filename to get file, run model and return prediction
            preds = {
                'Alligator Gar': '20%',
                'Rainbow Trout': '13%',
                'Catfish': '6%'
            }
            return jsonify({'predictions': preds})

    return send_from_directory(app.static_folder, 'index.html')

@app.route("/")
def index():
    return redirect('/predict')
