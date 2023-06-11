from flask import Flask, request, url_for, send_from_directory,jsonify
from app import app
from helpers import file_class

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "file wans't posted", 400
    
    file = file_class(request.files['file'])

    if not file.save_file():
        return "file wans't saved", 400

    return 'file saved', 200

@app.route('/remove', methods=['POST','DELETE'])
def remove():
    if 'file' not in request.files:
        return "file wans't posted", 400
    
    file = file_class(request.files['file'])

    if not file.remove_file():
        return "file wans't removed", 400

    return 'file removed', 200

@app.route('/files', methods=['POST'])
def get_files():
    if 'file' not in request.json:
        return 'Nenhum arquivo enviado', 400
    
    file = file_class(request.json['file'])
    return jsonify(file.get_file_path())
    #return send_from_directory(file.get_file_path()) 