def led_calibration_temp(threadname):
    import hmsysteme
    import time
    time.sleep(5)
    temp_init=hmsysteme.get_temp()
    print("init temp :"+str(temp_init))

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


    while True:
        time.sleep(10)
        temp=hmsysteme.get_temp()
        if temp != False:
            if temp != temp_init:
                print("temp :" + str(temp))
                a=200+3*(temp-temp_init)
                led_calib(a)







