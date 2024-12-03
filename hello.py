import pickle
import numpy
import cv2
import cvzone
import face_recognition
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackgroud = cv2.imread("Resources/background.png")

file = open('encode.p','rb')
encodelistknownids = pickle.load(file)
encodelistKnown,studentID = encodelistknownids


while True:
    sucess,img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)
    imgBackgroud[162:162+480,55:55+640] = img

    for encoFace,facloc in zip(encodeCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodelistKnown,encoFace)
        faceDis = face_recognition.face_distance(encodelistKnown,encoFace)
        matchid = np.argmin(faceDis)
        if(matches[matchid]):
            y1,x2,y2,x1 = facloc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            bbox = 55+x1,162+y1, x2-x1,y2-y1

            imgBackgroud = cvzone.cornerRect(imgBackgroud,bbox,rt=0)

    cv2.imshow("Image",imgBackgroud)
    cv2.waitKey(1)
