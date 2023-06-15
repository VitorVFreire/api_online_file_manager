from flask import Flask,render_template
import requests

def get_file_url(api_url, file_path):
    try:
        response = requests.post(api_url, json={'file': file_path})
        if response.status_code == 200:
            data = response.json()
            file_url = data.get('file_url')
            if file_url:
                return file_url
            else:
                print("URL not found in the response.")
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Request error:", str(e))
    
    return None

app = Flask(__name__)

from routes import *
@app.route('/')
def index():
    api_url_open_file = 'http://192.168.1.105:8585/files'
    file_name_open = 'A Bola Rosada'
    link=get_file_url(api_url_open_file, file_name_open)
    return render_template('index.html',titulo='teste',link_img=str(link))

app.run(port=8000, host='0.0.0.0',debug=True)