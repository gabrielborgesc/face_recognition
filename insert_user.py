import dao
from encodingsGenerator import EncodingsGenerator
from picamera import PiCamera
import cv2

#camera = PiCamera()
encoder = EncodingsGenerator()

#camera.capture('tmp/image.jpg')
#print("capiturasse")
img = cv2.imread("files/teste.jpg")
print("lesse")
encodings = encoder.generateEncoding(img)
print("encodasse")
print(encodings)
dao.add_user("Bernardo", encodings)
print("salvasse")
