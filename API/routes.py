from flask import Flask, request, url_for, send_from_directory,jsonify,send_file
from app import app
from helpers import file_class
import os

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "file wasn't uploaded", 400
    
    file = file_class(request.files['file'])

    if not file.save_file():
        return "file wasn't saved", 400

    return 'file saved', 200

@app.route('/remove', methods=['POST','DELETE'])
def remove():
    if 'file' not in request.files:
        return "file wasn't uploaded", 400
    
    file = file_class(request.files['file'])

    if not file.remove_file():
        return "file wans't removed", 400

    return 'file removed', 200

@app.route('/files', methods=['POST'])
def get_files():
    if 'file' not in request.json:
        return 'no file uploaded', 400
    
    file = file_class(request.json['file'])
    return jsonify(file.get_file_path())

@app.route('/openfile/<name_file>', methods=['GET'])
def open_file(name_file):    
    file = file_class(name_file)
    #file=file_class(request.json['file'])
    file_path = file.get_file_path()
    if not os.path.exists(file_path):
        return 'file not found', 404

    return send_file(file_path, mimetype=file.type_file())