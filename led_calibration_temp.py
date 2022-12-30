def led_calibration_temp(threadname):
    import hmsysteme
    import time
    import statistics
    import math


    def measuretemp():
        try:
            s = []
            for i in range(0, 20):
                time.sleep(1)
                temp = hmsysteme.get_temp()
                if temp != False:
                    s.append(temp)
            #print(s)
            s = statistics.median(s)
            s = int(round(s, 0))
            print("temp :" + str(s))
            return s
        except:
            pass


    def led_calib(value):
        try:
            path = '/home/pi/Downloads/HM01_v0.1/'
            import smbus2
            import time
            bus = smbus2.SMBus(1)
            address = 0x2c
            # value=200
            bus.write_byte_data(address, 0, value)
            print("LEDS set to: " + str(value))
            time.sleep(1)
        except Exception as e:
            print(e)


    time.sleep(5)
    temp_init=measuretemp()
    print("init temp :"+str(temp_init))
    while True:
        try:
            #time.sleep(10)
            s=measuretemp()
            a = 200 + 3 * (s - temp_init)
            led_calib(a)
        except:
            pass









