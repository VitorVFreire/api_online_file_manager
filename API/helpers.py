import time
import os
import pathlib
from flask import send_from_directory

import base64
from hashlib import sha256

def criptografar(senha):
    hash_senha = sha256(senha.encode())
    senha_digest = hash_senha.digest()
    senha_base64 = base64.b64encode(senha_digest).decode('utf-8')
    return senha_base64

class file_class:
    def __init__(self, file):
        self.file = file
    
    def save_file(self):
        try:
            filename = self.file.filename
            time_now = int(time.time())
            name = f'files/{time_now}{filename}'           
            self.file.save(name)
            return True
        except Exception as e:
            print("**ERRO::", e)
            return False
        
    def remove_file(self):
        try:
            diretorio = pathlib.Path('files')
            name = f'{self.file.filename}'
            arquivo = list(diretorio.glob(f'*{name}*'))
            os.remove(arquivo[0])
            return True
        except Exception as e:
            print("**ERRO::", e)
            return False
    
    def get_file_path(self):
        diretorio = pathlib.Path('files')
        name = f'{self.file}'
        arquivo = list(diretorio.glob(f'*{name}*'))
        if arquivo:
            return str(arquivo[0])
        else:
            return 'Arquivo não encontrado'
    
    def type_file(self):
        if self.file.endswith('.jpg') or self.file.endswith('.jpeg'):
            return 'image/jpeg'
        elif self.file.endswith('.png'):
            return 'image/png'
        elif self.file.endswith('.mp4'):
            return 'video/mp4'
        elif self.file.endswith('.mp3'):
            return 'audio/mp3'
        else:
            return 'application/octet-stream'