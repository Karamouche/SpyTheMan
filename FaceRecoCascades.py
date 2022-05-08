"""
Created on Wed Feb  9 09:57:17 2022

@author: Karamouche

Small algorithme to get if a mask is wear or not
"""

import cv2

def hasMask(rec):
    """
    If a face is detect, and the mouth inside of it, there is no mask -> shoot
    If a face is detect, possibility to wear a mask
    else, nothing
    """
    face = cv2.CascadeClassifier('cascades/frontalface_alt.xml')
    mouth = cv2.CascadeClassifier('cascades/mouth2.xml')
    grayRec = cv2.cvtColor(rec, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(grayRec, 1.1, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    mouths = mouth.detectMultiScale(grayRec, 3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(rec, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x, y, w, h) in mouths:
        cv2.rectangle(rec, (x, y), (x+w, y+h), (0, 255, 0), 2)
    nbMask = 0
    nbNotMask = 0
    if len(faces) >= 1:
        for fac in faces:
            if(inside(fac, mouths)):
                nbNotMask += 1
            else:
                nbMask += 1
    cv2.putText(rec, "Nb mask : "+str(nbMask), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(rec, "Nb pas mask : "+str(nbNotMask), (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return rec
    
def inside(face, mouths):
    fx = face[0]
    fy = face[1]
    fw = face[2]
    fh = face[3]
    for mouth in mouths:
        Mx = mouth[0]
        My = mouth[1]
        if Mx < fx + fw and My < fy + fh:
            return True
    return False

cam = cv2.VideoCapture(0)
succes, rec = cam.read()
rec = cv2.flip(rec, 1)
rec = cv2.resize(rec, (1280, 720))
if not cam.isOpened():
    print("Error initializing camera")

while cam.isOpened():
    cv2.imshow("SpyTheMan", hasMask(rec))
    succes, rec = cam.read()
    rec = cv2.flip(rec, 1)
    rec = cv2.resize(rec, (1280, 720))
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyWindow("SpyTheMan")
cam.release()
