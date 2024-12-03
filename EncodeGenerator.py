import os

import cv2
import face_recognition
import pickle

folderImgPath = "Images"
imgPathList = os.listdir(folderImgPath)
imgList = []
studentID = []
for path  in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderImgPath,path)))
    studentID.append(int(path[0:4]))

def findEncodings(imglist):
    encodeList = []

    for img in imglist:
        cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started")
encodelistKnown = findEncodings(imgList)
encodeListId = [encodelistKnown,studentID]
print("Encoding finished")


file = open("encode.p",'wb')
pickle.dump(encodeListId,file)
file.close()
print("file saved")



