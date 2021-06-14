import cv2
import dlib
from imutils import rotate as imutilsRotate
from scipy.ndimage.interpolation import rotate as scipyRotate
import numpy as np

class EncodingsGenerator:

    def __init__(self):
        self.default='default'

    def generateEncoding(self, img):
        # Load the detector
        detector = dlib.get_frontal_face_detector()
        print("1")
        # Load the predictor
        predictor = dlib.shape_predictor("files/shape_predictor/shape_predictor_68_face_landmarks.dat")
        print("2")
        # Instancia o objeto responsável pela codificação do rosto baseado no modelo de aprendizado
        face_encoder = dlib.face_recognition_model_v1("files/shape_predictor/dlib_face_recognition_resnet_model_v1.dat")
        print("3")
        #change img to rbg
        img_np_array = np.array(img)
        img_rgb = img_np_array[:, :, ::-1]
        print("4")
        # Use detector to find rectangle
        faces = detector(img_rgb, 0)
        print("faces aaaa")
        print(faces)
        for face in faces:
            x1 = face.left() # left point
            y1 = face.top() # top point
            x2 = face.right() # right point
            y2 = face.bottom() # bottom point

            # Use predictor to find landmarks
            landmarks = predictor(img_rgb, face)

            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                # Draw a circle
                # cv2.circle(img=img, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)
                # print((x, y))

            
            # Draw a rectangle
            # cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)

            

            #generate encoding
            encodings = np.array(face_encoder.compute_face_descriptor(img_rgb, landmarks, 1))

        # show the image
        # cv2.imshow(winname="Face", mat=img)
        return encodings

        

