import time

class file_class:
    def __init__(self,file):
        self.file=file
    
    def save_file(self):
        try:
            type_file=type(self.file)
            time_now=time.timezone()
            if type_file=='png':
                name=f'img{self.file}{time_now}'
                path=f'file/img/png/{name}'
            elif type_file=='mp4':
                name=f'video{self.file}{time_now}'
                path=f'file/video/mp4/{name}'
            else:
                return False
            self.file.save(path)
        except:
            return False
    