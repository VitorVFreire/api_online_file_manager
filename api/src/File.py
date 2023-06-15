import time
import os
import pathlib
from flask import send_from_directory

from database import mydb
from .User import User

'''
status:
0-private
1-public
'''

class File(User):
    def __init__(self,name_file,id_user,file=None):
        self.file = file
        self.name_file=name_file.replace(" ","")
        super().__init__(id=id_user)
        self.directory=pathlib.Path('Files')
    
    def save_file(self):
        try:
            time_now = int(time.time())
            name = f'{time_now}{self.name_file}'  
            route= f'{self.directory}/{name}'   
            self.file.save(route)
            self.insert_file_base(name)
            return True
        except Exception as e:
            print("**ERRO::", e)
            return False
        
    def insert_file_base(self,name):
        try:
            if self.name_file and self.id:
                mycursor = mydb.cursor()
                mycursor.execute('INSERT INTO files (name_file,id_user,status) values(%s,%s,%s)',(name,self.id,0))
                mydb.commit()
                return True
        except EOFError as e:
                print(e)
                return False
        return False
        
    def remove_file(self):
        try:
            arquivo = list(self.directory.glob(f'*{self.name_file}*'))
            os.remove(arquivo[0])
            self.delete_file()
            return True
        except Exception as e:
            print("**ERRO::", e)
            return False

    def delete_file(self):
        try:
            if self.name_file:
                mycursor = mydb.cursor()
                mycursor.execute("DELETE from files WHERE name_file LIKE %s", (f'%{self.name_file}%',))
                mydb.commit()
                return True
        except EOFError as e:
            print(e)
            return False
        return False
    
    def update_status(self,status):
        try:
            if self.name_file and self.id:
                mycursor = mydb.cursor()
                mycursor.execute('UPDATE files SET status=%s WHERE id_file=%s',(status,self.id))
                mydb.commit()
                return True
        except EOFError as e:
                print(e)
                return False
        return False
    
    def get_file_path(self):
        arquivo = list(self.directory.glob(f'*{self.name_file}*'))
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