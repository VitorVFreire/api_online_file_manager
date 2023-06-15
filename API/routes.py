from flask import Flask, request, url_for, send_from_directory,jsonify,send_file
from app import app
from src import User,File
import os

@app.route('/')
def index():
    return 'API ON'

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "file wasn't uploaded", 400
    file_upload = request.files['file']
    print(file_upload)
    print(file_upload.filename)
    file = File(file=file_upload, name_file=file_upload.filename,id_user=1)

    if file.save_file()==False:
        return "file wasn't saved", 400

    return 'file saved', 200

import os

@app.route('/remove', methods=['POST','DELETE'])
def remove():
    if 'file' not in request.files:
        return "file wasn't uploaded", 400
    
    file_path = request.files['file']
    file_name = os.path.basename(file_path)  # Extrai o nome do arquivo do caminho
    
    file = File(name_file=file_name, id_user=1)
    
    if file.remove_file() == False:
        return "file wasn't removed", 400

    return 'file removed', 200


@app.route('/files', methods=['POST'])
def get_files():
    if 'file' not in request.json:
        return 'no file uploaded', 400
    
    file_upload=request.files['file']
    file = File(file_upload,file_upload.filename)
    
    return jsonify(file.get_file_path())

@app.route('/openfile/<name_file>', methods=['GET'])
def open_file(name_file):    
    #file=File(request.json['file'])
    file = File(name_file=name_file)
    file_path = file.get_file_path()
    if not os.path.exists(file_path):
        return 'file not found', 404

    return send_file(file_path, mimetype=file.type_file())