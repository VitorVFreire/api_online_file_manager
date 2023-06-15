import requests
import json
base_api='http://192.168.1.105:8585/'
def upload_file(api_url, file_path):
    try:
        files = {'file': open(file_path, 'rb')}
        response = requests.post(api_url, files=files)

        if response.status_code == 200:
            print('Upload do arquivo realizado com sucesso!')
            print(response)
        else:
            print('Erro ao fazer o upload do arquivo. Código de status:', response.status_code)
            print(response.json)
    except IOError as e:
        print('Erro ao abrir o arquivo:', str(e))
        
api_url = base_api+'upload_file'
file_path='file/A Bola Rosada.mp4'
#upload_file(api_url, file_path)
        
def remove_file(api_url, file_path):
    try:
        json = {'file': file_path}
        response = requests.post(api_url, json=json)

        if response.status_code == 200:
            print('Remoção do arquivo realizada com sucesso!')
            print(response)
        else:
            print('Erro ao remover arquivo. Código de status:', response.status_code)
            print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo de vídeo:', str(e))
        
api_url_remove=base_api+'remove'
file_path = 'ABolaRosada.mp4'
remove_file(api_url_remove, file_path)

def files(api_url, file_name):
    try:
        response = requests.post(api_url, json={'file':file_name})
        print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo:', str(e))
api_url_file = base_api+'files'
file_name = 'file/Drum_Island_Infobox'
#files(api_url_file, file_name)

def link_file(api_url, file_name):
    try:
        response = requests.post(api_url, json={'file': file_name})
        if response.status_code == 200:
            link = response
            print('Link do arquivo:', link)
        else:
            print('Erro ao obter o link do arquivo. Código de status:', response.status_code)
            print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo:', str(e))

api_url_open_file = base_api+'openfile'
file_name_open = 'file/Drum_Island_Infobox'
#link_file(api_url_open_file, file_name_open)
