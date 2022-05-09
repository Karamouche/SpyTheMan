import serial 
channel = serial.Serial('dev/ttyACM0',9600) #Complete le port serial ls /dev/tty*
options = ['shoot','up','down','right','left']
while True:
    message = input("Choose between : shoot/up/down/right/left")
    for i in options:
        if message == i:
            channel.write(message)
            print('Message send :',message)
            
