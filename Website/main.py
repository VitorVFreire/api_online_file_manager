import requests
import json

def upload_file(api_url, file_path):
    upload_endpoint = api_url
    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(upload_endpoint, files=files)
            if response.status_code == 200:
                print('Upload do arquivo realizado com sucesso!')
                print(response)
            else:
                print('Erro ao fazer o upload do arquivo. Código de status:', response.status_code)
                print(response.json)
    except IOError as e:
        print('Erro ao abrir o arquivo:', str(e))
        
api_url = 'http://192.168.1.14:8585/upload'
file_path='file/HarryPotter.png'
#upload_file(api_url, file_path)
        
def remove_file(api_url, file_path):
    try:
        with open(file_path, 'rb') as file:
            response = requests.delete(api_url, files={'file': file})

            if response.status_code == 200:
                print('Remoção do arquivo realizada com sucesso!')
                print(response)
            else:
                print('Erro ao remover arquivo. Código de status:', response.status_code)
                print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo de vídeo:', str(e))
        
api_url_remove='http://192.168.1.14:8585/remove'
file_path = 'file/Drum_Island_Infobox.png'
#remove_file(api_url_remove, file_path)

def files(api_url, file_name):
    try:
        response = requests.post(api_url, json={'file':file_name})
        print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo:', str(e))
api_url_file = 'http://192.168.1.14:8585/files'
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

api_url_open_file = 'http://192.168.1.14:8585/openfile'
file_name_open = 'file/Drum_Island_Infobox'
#link_file(api_url_open_file, file_name_open)
