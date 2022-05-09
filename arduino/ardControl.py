import serial 
channel = serial.Serial('dev/ttyACM0',9600) #Complete le port serial ls /dev/tty*
options = ['0','1','2','3','4']
while True:
    message = input("shoot : 0/up : 1/down : 2/right : 3/left : 4")
    for i in options:
        if message == i:
            channel.write(message)
            print('Message send :',message)
