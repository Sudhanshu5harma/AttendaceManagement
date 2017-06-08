import serial
ardunioData=serial.Serial('com6',9600)
while(1==1):
    mydata = (ardunioData.readline().strip())
    print (mydata.decode('utf-8'))
