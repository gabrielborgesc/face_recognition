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
sudo pip3 install pipenv
```
4. Crie o virtualenv
```
pipenv shell
```
5. Instale as dependências no virtualenv do projeto pelo pipenv
```
pipenv update --python python3
```

6. Testando: 
Repare que o arquivo test.py há referência para os arquivos files/shape_predictor/shape_predictor_68_face_landmarks.dat, files/shape_predictor/dlib_face_recognition_resnet_model_v1.dat e files/images/teste.jpeg.

Os arquivos shape_predictor_68_face_landmarks.dat e dlib_face_recognition_resnet_model_v1.dat são de treinamento para o algoritmo de Inteligência Artificial e não sobrem para o git devido seu tamanho. Eles podem ser baixados na raiz de https://github.com/davisking/dlib-models.

Após realizar o download de ambos, vá com o terminal à pasta em que foram baixados e descompacte-os:

```
bunzip2 shape_predictor_68_face_landmarks.dat.bz2
bunzip2 dlib_face_recognition_resnet_model_v1.dat.bz2
```
Após isso, coloque-os na pasta files/shape_predictor a partir da raiz do projeto.

Por fim, utilize qualquer, nomeando-a como test.jpeg (ou troque o nome do arquivo no código) e coloque-a na pasta files/images

```
python3 test.py
```
