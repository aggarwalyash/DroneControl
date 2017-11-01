from RPIO import PWM


roll = PWM.Servo(0,20000,5)
pitch = PWM.Servo(0,20000,5)
throttle = PWM.Servo(0,20000,5)
yaw = PWM.Servo(0,20000,5)
#aux = PWM.Servo()
# start PWM on servo specific GPIO no, this is not the pin no but it is the GPIO no 
roll.set_servo(5,1520)# pin 29
pitch.set_servo(6,1520)# pin 31
throttle.set_servo(13,1100)# pin 33
yaw.set_servo(19,1520)# pin 35

try: 
    while True:
       x = int(raw_input("CHECK THROTTLE: "))
       throttle.set_servo(13,x)
except:
    throttle.stop_servo(13)
    yaw.stop_servo(19)
    pitch.stop_servo(6)
    roll.stop_servo(5)
PWM.cleanup()       

