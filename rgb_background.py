def rgb_background(threadname):
    import hmsysteme
    import time
    import smbus2
    bus=smbus2.SMBus(1)
    addrnano=0x1E

    while True:
        time.sleep(0.5)       
        a=hmsysteme.get_rgbcolor()     
        if a != False:
            try:
                bus.write_byte_data(addrnano,0, int(a[2]))#blue
                bus.write_byte_data(addrnano, 1, int(a[1]))#green
                bus.write_byte_data(addrnano, 2, int(a[0]))#red
                print("colors set")

            except Exception as e:
                print(e)
                print("only usable on HM01")
                print("color :" +str(a))


        hmsysteme.put_temp(bus.read_byte(addrnano))




