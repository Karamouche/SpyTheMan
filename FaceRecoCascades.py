"""
Created on Wed Feb  9 09:57:17 2022

@author: Karamouche

Small algorithme to get if a mask is wear or not
"""

import cv2
import serial 
import time
channel = serial.Serial('COM4',9600) #Complete le port serial ls /dev/tty*
options = ['1','2','3','4', '5']
hasShoot = False

def shoot(rec):
    """
    If a face is detect, and the mouth inside of it, there is no mask -> shoot
    """
    face = cv2.CascadeClassifier('cascades/frontalface_alt.xml')
    mouth = cv2.CascadeClassifier('cascades/mouth2.xml')
    global hasShoot
    APROX = 20 #Valeur d'environ autour du centre de la cam
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
        #print(deplacement)
    if deplacement != None and not hasShoot:
        if(deplacement[0] < APROX and deplacement[0] > -APROX and
           deplacement[1] < APROX and deplacement[1] > -APROX):
            channel.write('1'.encode()) #shoot
            time.sleep(0.3)
            hasShoot = True
        if(deplacement[0] > APROX):
            channel.write('4'.encode())
        if(deplacement[0] < -APROX):
            channel.write('5'.encode())
        if(deplacement[1] > APROX):
            channel.write('3'.encode())
        if(deplacement[1] < -APROX):
            channel.write('2'.encode())
    else:
        channel.write('0'.encode())
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
    if hasShoot:
        time.sleep(1)
        hasShoot = False
    cv2.imshow("SpyTheMan", shoot(rec))
    #shoot(rec)
    succes, rec = cam.read()
    rec = cv2.flip(rec, 1)
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyWindow("SpyTheMan")
channel.close()
cam.release()
