import cv2
import numpy as np
import face_recognition
import os

def findClass():
    path = "./employ_img"
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cls in myList:
        curImg = cv2.imread(f"{path}/{cls}")
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
    return images,classNames


def findEncode(images):
    encodeList=[]
    print(len(images))
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        print("Done")
        encodeList.append(encode)
    return encodeList

def find_img(img_input):
    encodeKnowFace = findEncode(findClass()[0])
    print("Encoding Complite")
    classNames=findClass()[1]
    imgSmall = cv2.resize(img_input,(0,0),None,0.25,0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
    faceCurrFrame = face_recognition.face_locations(imgSmall)
    encodeCurrFrame = face_recognition.face_encodings(imgSmall, faceCurrFrame)
    print(len(encodeKnowFace))
    for en, loc in zip(encodeCurrFrame, faceCurrFrame):


        matches = face_recognition.compare_faces(encodeKnowFace, en)
        faceDis = face_recognition.face_distance(encodeKnowFace, en)
        print(len(matches))
        matchIndex = np.argmin(faceDis)
        name="Not found"
        if matches[matchIndex]:
            name = classNames[matchIndex]
            print(name)
            return name

