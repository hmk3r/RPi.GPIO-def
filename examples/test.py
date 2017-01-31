import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, True)

p = GPIO.PWM(11, 50)
p.start(6)
p.ChangeDutyCycle(4)
p.ChangeFrequency(60)
p.stop()
