from flask import Flask, request
from app import app
from helpers import file_class

@app.post('/upload')
def upload():
    if 'file' not in request.files:
        return 'Nenhum vídeo enviado', 400
    
    file=file_class(request.files['video'])

    if file.save_file:
        return "file wasn't saved"

    return 'file saved'