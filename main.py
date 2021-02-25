import cv2
import numpy as np
import face_recognition
from encodingsGenerator import EncodingsGenerator

encoder = EncodingsGenerator()

img = cv2.imread("files/images/empe.jpeg")
# img = face_recognition.load_image_file("files/images/foto1.jpeg")
# print('encondings1')
encodings1 = encoder.generateEncoding(img)
# encodings1 = face_recognition.face_encodings(img)[0]

# print('\n\n\n\n')

img = cv2.imread("files/images/foto1.jpeg")
# img = face_recognition.load_image_file("files/images/antero.jpeg")
# print('encondings2')
encodings2 = encoder.generateEncoding(img)
# encodings2 = face_recognition.face_encodings(img)[0]

# print('encodings1', encodings1)
# print('encodings2', encodings2)
# print('dif', encodings1 - encodings2)
# print('norm1', np.linalg.norm(encodings1))
dif = encodings1 - encodings2
# print('dif', dif)
# print('dif size', dif.size)
print(np.linalg.norm(encodings1-encodings2))