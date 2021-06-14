import dao
import face_recognition
from picamera import PiCamera
import serivce as service

camera = PiCamera()

camera.capture('tmp/image.jpg')
#print("capiturasse")
img = face_recognition.load_image_file("tmp/image.jpg")
print("lesse")
encodings = face_recognition.face_encodings(img)[0]
print("encodasse")
print(encodings)
dao.add_user("bernardo", service.npArrayToJson(encodings))
print("salvasse")
