# API Online File Manager

A API Online File Manager é um projeto em Python com Flask que permite o envio e o acesso a arquivos de vídeo, imagem e áudio de forma online. Com essa API, é possível fazer upload de arquivos e obter URLs para visualizá-los e reproduzi-los diretamente no navegador.
 
## Recursos
Suporte a arquivos de vídeo (formatos comuns como MP4, AVI, MOV, etc.)
Suporte a arquivos de imagem (formatos comuns como JPG, PNG, GIF, etc.)
Suporte a arquivos de áudio (formatos comuns como MP3, WAV, FLAC, etc.)
Geração de URLs para visualizar e reproduzir os arquivos online

## Pré-requisitos
Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados em sua máquina:

Python 3.11.4: https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe<br>

## Como Usar
Clone o repositório para sua máquina local:
```
git clone https://github.com/VIVF0/api_online_file_manager.git
```
Navegue até o diretório do projeto:
```
cd api_online_file_manager
```
Instale as dependências do projeto:
```
pip install -r api/requirements.txt
```
Execute o arquivo app.py:
```
python api/app.py
```
## Endpoints
A API possui os seguintes endpoints:

POST /upload: Recebe um arquivo como entrada e retorna a URL do arquivo online.

GET /file/<filename>: Retorna a URL de um arquivo específico para visualização ou reprodução online.
```
curl -F "file=@/caminho/do/arquivo/video.mp4" http://localhost:5000/upload
```
A API retornará um JSON com a URL do arquivo online. Por exemplo:
```
{
  "url": "http://localhost:5000/file/video.mp4"
}
```
Acesse a URL fornecida para visualizar ou reproduzir o arquivo online.

## Licença
Este projeto está licenciado sob a licença MIT. <br>Sinta-se à vontade para usá-lo de acordo com os termos da licença.

Esse projeto foi desenvolvido por Vitor Freire.
