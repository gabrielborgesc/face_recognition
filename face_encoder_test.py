import cv2
import dlib
from imutils import rotate as imutilsRotate
from scipy.ndimage.interpolation import rotate as scipyRotate
import numpy as np
from math import pi, cos, sin

# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("files/shape_predictor/shape_predictor_68_face_landmarks.dat")

# Instancia o objeto responsável pela codificação do rosto baseado no modelo de aprendizado
face_encoder = dlib.face_recognition_model_v1("files/shape_predictor/dlib_face_recognition_resnet_model_v1.dat")

# read the image
img = cv2.imread("files/images/antero.jpeg")
img = imutilsRotate(img, 0)

# Convert image into grayscale
# gray_image = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

img_np_array = np.array(img)
img_rgb = img_np_array[:, :, ::-1]

# Use detector to find rectangle
faces = detector(img_rgb, 0)
# faces = detector(img_rgb, 0)
for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point

    # Use predictor to find landmarks
    # landmarks = predictor(image=gray_image, box=face)
    landmarks = predictor(img_rgb, face)
    code = face_encoder.compute_face_descriptor(img_rgb, landmarks, 1)
    print(type(code))
    encodings = np.array(code)
    print('encodings', encodings[0])

    # x = firstPoint.x
    # y=firstPoint.y
    # angle = -7
    # radianAngle = angle*pi/180
    # xx = x*cos(radianAngle) - y*sin(radianAngle)
    # yy = x*sin(radianAngle) + y*cos(radianAngle)
    # rotatePoint = [xx, yy]
    # print('rotatePoint', rotatePoint)

    # Loop through all the points
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        # Draw a circle
        cv2.circle(img=img, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)

    # cv2.circle(img=img, center=(firstPoint.x, firstPoint.y), radius=5, color=(0, 255, 0), thickness=-1)
    # cv2.circle(img=img, center=(secondPoint.x, secondPoint.y), radius=5, color=(0, 255, 0), thickness=-1)

    # Draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)

    # cv2.line(img=img, pt1=(firstPoint.x, firstPoint.y), pt2=(secondPoint.x, secondPoint.y), color=(0, 255, 0))


    
    
# show the image
cv2.imshow(winname="Face", mat=img)

# img = cv2.imread("files/images/foto3.jpeg")
# gray_image = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# faces = detector(gray_image)
# for face in faces:
#     landmarks = predictor(image=gray_image, box=face)
#     secondPoint = landmarks.part(14)
#     # print(secondPoint)

#     for n in range(0, 68):
#         x = landmarks.part(n).x
#         y = landmarks.part(n).y
#         # Draw a circle
#         cv2.circle(img=img, center=(x, y), radius=5, color=(0, 255, 0), thickness=-1)

    # Draw a rectangle
    # cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)



# show the image
# cv2.imshow(winname="Face", mat=img)

# Wait for a key press to exit
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()
