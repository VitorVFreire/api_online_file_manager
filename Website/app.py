from flask import Flask,render_template
import requests

def link_file(api_url, file_name):
    try:
        response = requests.post(api_url, json={'file': file_name})
        print(response.content)
        print(response.json())
        if response.status_code == 200:
            link = response.content
            print(link)
            return link['link']
        else:
            print('Erro ao obter o link do arquivo. Código de status:', response.status_code)
            print(response.json())
    except IOError as e:
        print('Erro ao abrir o arquivo:', str(e))

api_url_open_file = 'http://192.168.1.14:8585/oepnfile'
file_name_open = 'Drum_Island_Infobox'

app = Flask(__name__)

from routes import *
@app.route('/')
def index():
    link=link_file(api_url_open_file, file_name_open)
    return render_template('index.html',titulo='teste',link_img=link)

app.run(port=8000, host='0.0.0.0',debug=True)