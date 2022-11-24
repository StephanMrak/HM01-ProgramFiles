def rgb_background(threadname):
	import hmsysteme
	import time
	try:
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(17, GPIO.OUT)
            GPIO.setup(22, GPIO.OUT)
            GPIO.setup(27, GPIO.OUT)
            r = GPIO.PWM(22, 2500)  # Rot; 25kHz
            r.start(0)
            g = GPIO.PWM(17, 2500)  # Grün; 25kHz
            g.start(0)
            b = GPIO.PWM(27, 2500)  # Blau; 25kHz
            b.start(0)
	except:
            pass
	while True:
            time.sleep(0.5)
            a=hmsysteme.get_rgbcolor()
            if a != False:
                try:        
                    r.ChangeDutyCycle(a[0]/255*100)
                    g.ChangeDutyCycle(a[1]/255*100)
                    b.ChangeDutyCycle(a[2]/255*100)
                    
                except:
                    print("only usable on HM01")
                    print("color :" +str(a))

			

	r.stop()
	g.stop()
	b.stop()
	GPIO.cleanup()
