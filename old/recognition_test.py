import numpy as np
import cv2
from encodingsGenerator import EncodingsGenerator

encoder = EncodingsGenerator()

img1 = cv2.imread("files/images/fp1.jpeg") 
encodings1 = encoder.generateEncoding(img1)
img2 = cv2.imread("files/images/fp2.jpeg") 
encodings2 = encoder.generateEncoding(img2)
dif = np.linalg.norm(encodings1-encodings2)
print(dif)