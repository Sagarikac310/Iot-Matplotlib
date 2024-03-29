import RPi.GPIO as GPIO
import time
import datetime
import csv

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 17
ECHO = 27

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
while True:
    row = []
    GPIO.output(TRIG,False)
    print("---------------------------")
    print("Distance Measurements in progress")
    print("Waiting for sensor to settle")
    time.sleep(2)

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration*17150
    distance = round(distance,2)

    print("Distance:",distance," cm ")
    print("-------------------------------")

    row.append(distance)
    row.append(str(datetime.datetime.now()))

    with open('reading.csv','a')as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
csvFile.close()

    


    
