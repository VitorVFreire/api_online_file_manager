import time
import os
import pathlib
from flask import send_from_directory
class file_class:
    def __init__(self, file):
        self.file = file
        self.directory=pathlib.Path('Files')
    
    def save_file(self):
        try:
            filename = self.file.filename
            time_now = int(time.time())
            name = f'{self.directory}{time_now}{filename}'           
            self.file.save(name)
            return True
        except Exception as e:
            print("**ERRO::", e)
            return False
        
    def remove_file(self):
        try:
            name = f'{self.file.filename}'
            arquivo = list(self.directory.glob(f'*{name}*'))
            os.remove(arquivo[0])
            return True
        except Exception as e:
            print("**ERRO::", e)
            return False
    
    def get_file_path(self):
        name = f'{self.file}'
        arquivo = list(self.directory.glob(f'*{name}*'))
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