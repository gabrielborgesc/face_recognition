# face_recognition

## Instalação no Ubuntu

1. Instale os seguintes requerimentos:
```
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev 
sudo apt-get install libx11-dev libgtk-3-dev
sudo apt-get install python python-dev python-pip
sudo apt-get install python3 python3-dev python3-pip
```

2. Clone o projeto
```
git clone https://github.com/gabrielborgesc/face_recognition.git
```

3. Instale o gerenciador de dependências pipenv:
```
pip3 install pipenv
```

4. Instale as dependências no virtualenv do projeto pelo pipenv
```
pipenv update
```
5. Acesse o virtualenv para executar o projeto
```
pipenv shell
```
6. Testando:
```
python3 test.py
```
