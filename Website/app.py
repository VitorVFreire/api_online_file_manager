import requests
import json

def upload_video(api_url, video_path):
    # Definir o endpoint da API para upload de vídeo
    upload_endpoint = api_url

    try:
        # Abrir o arquivo de vídeo em modo de leitura binária
        with open(video_path, 'rb') as file:
            # Criar o payload do arquivo para o upload
            files = {'file': file}

            # Enviar a requisição POST para fazer o upload do vídeo
            response = requests.post(upload_endpoint, files=files)

            # Verificar se a requisição foi bem-sucedida
            if response.status_code == 200:
                print('Upload do vídeo realizado com sucesso!')
                print(response)
            else:
                print('Erro ao fazer o upload do vídeo. Código de status:', response.status_code)
                print(response.json)
    except IOError as e:
        print('Erro ao abrir o arquivo de vídeo:', str(e))
        
api_url = 'http://192.168.1.14:8585/upload'
video_path = 'Drum_Island_Infobox.png'
#upload_video(api_url, video_path)
        
def remove_video(api_url, video_path):
    try:
        with open(video_path, 'rb') as file:
            response = requests.delete(api_url, files={'file': file})

            if response.status_code == 200:
                print('Remoção do vídeo realizada com sucesso!')
                print(response)
            else:
                print('Erro ao remover o vídeo. Código de status:', response.status_code)
                print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo de vídeo:', str(e))
        
file='Drum_Island_Infobox.png'
api_url_remove='http://192.168.1.14:8585/remove'
remove_video(api_url_remove, file)

def files(api_url, file_name):
    try:
        response = requests.post(api_url, json={'file':file_name})
        print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo de vídeo:', str(e))
api_url_file = 'http://192.168.1.14:8585/files'
file_name = 'Drum_Island_Infobox'
files(api_url_file, file_name)