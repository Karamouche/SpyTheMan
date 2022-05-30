"""
Created on Wed Feb  9 09:57:17 2022

@author: Karamouche

Small algorithme to get if a mask is wear or not
"""

import cv2
import serial 
channel = serial.Serial('COM4',9600) #Complete le port serial ls /dev/tty*
options = ['1','2','3','4', '5']
# shoot : 1 / up :2 / down : 3 / left : 4 / right : 5
"""
liste = ['2', '2', '2', '2', '2', '4', '4', '4', '4', '4']
for element in liste:
    channel.write(element.encode())
"""

def shoot(rec):
    """
    If a face is detect, and the mouth inside of it, there is no mask -> shoot
    """
    face = cv2.CascadeClassifier('cascades/frontalface_alt.xml')
    mouth = cv2.CascadeClassifier('cascades/mouth2.xml')
    grayRec = cv2.cvtColor(rec, cv2.COLOR_BGR2GRAY)
    center = (int(rec.shape[1]/2), int(rec.shape[0]/2))
    faces = face.detectMultiScale(grayRec, 1.1, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    mouths = mouth.detectMultiScale(grayRec, 3, 5, minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE)
    nbMask = 0
    nbNotMask = 0
    facesToShoot = []
    if len(faces) >= 1:
        for fac in faces:
            if(inside(fac, mouths)):
                nbNotMask += 1
                facesToShoot.append(fac)
            else:
                nbMask += 1
    points = [] #liste des points à viser
    for element in facesToShoot:
        points.append( (int(element[0]+element[2]/2), int(element[1]+element[3]/2)) )
    if len(points) >= 1:
        cv2.circle(rec, points[0], 10, (0, 0, 255), 4)
    cv2.circle(rec, center, 10, (255, 0, 255), 4)
    deplacement = None
    if len(points)>=1:
        deplacement = (points[0][0]-center[0], points[0][1]-center[1])
        print(deplacement)
    if deplacement != None:
        if(deplacement[0] < 30 and deplacement[0] > -30 and
           deplacement[1] < 30 and deplacement[1] > -30):
            print("shoot")
            channel.write('1'.encode()) #shoot
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
if not cam.isOpened():
    print("Error initializing camera")

while cam.isOpened():
    cv2.imshow("SpyTheMan", shoot(rec))
    succes, rec = cam.read()
    rec = cv2.flip(rec, 1)
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyWindow("SpyTheMan")
channel.close()
cam.release()
