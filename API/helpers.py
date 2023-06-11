import time
import os
import pathlib
from flask import send_from_directory

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
            return str(arquivo)
        else:
            return 'Arquivo não encontrado'
    