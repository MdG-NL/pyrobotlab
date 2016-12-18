# Starting the Servo Service
# Tested in MRL 1851, where Calamity has added a Acceleration option

arduino = Runtime.createAndStart("arduino","Arduino")
arduino.setBoardMega()
arduino.connect("/dev/tty.usbmodem411")

servo = Runtime.createAndStart("servo","Servo")
servo.attach(arduino,3)
sleep(1) #attaching procedure take a bit more time to do, wait a little before using it

# Setting the Velocity and the first Acceleration
servo.setVelocity(400)

servo.setAcceleration(4)
servo.moveTo(0)

sleep(4)
servo.setAcceleration(10)
servo.moveTo(180)

sleep(4)
servo.setAcceleration(20)
servo.moveTo(0)

sleep(4)
servo.setAcceleration(40)
servo.moveTo(180)