def main():
    import time
    import pygame
    import math
    import random
    from pathlib import Path
    from threading import Thread
    import multiprocessing
    from queue import Queue
    import sys
    import os
    import platform
    import hardware_com
    import mobile_com
    import hotspot
    import background
    import hmsysteme
    import rgb_background
    import led_calibration_temp
    import arduino_reset
    hmsysteme.clear_all()
    print(platform.uname())
    def led_calib(value):
        if 'raspberrypi' in platform.uname():
            path = '/home/pi/Downloads/HM01_v0.1/'
            import smbus2
            import time
            bus=smbus2.SMBus(1)
            address=0x2c
            #value=200
            bus.write_byte_data(address, 0, value)
            print("LEDS set to: " + str(value))
            time.sleep(1)


    arduino_reset.arduino_reset()


    path=os.path.realpath(__file__)
    path=path.replace('thread_handler.py', '')
    sys.path.append(os.path.join(path, "games"))
    size=hmsysteme.get_size()

    def list_files(path='.'):
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                print(filename)
            else:
                list_files(os.path.join(path, filename))

    gamefiles=os.listdir(os.path.join(path, "games"))
    gamefiles.remove('__pycache__')
    gamefiles.remove('game_template.py')
    gamefiles.remove('pics')

    for x in range(len(gamefiles)):
        gamefiles[x]=gamefiles[x].replace('.py', '')

    modules=[]
    for x in gamefiles:
        try:
            modules.append(__import__(x))
            print("Successfully imported", x, '.')
        except ImportError:
            print("Error importing", x, '.')
    print(gamefiles)

    queue=multiprocessing.Queue()
    queue2=multiprocessing.Queue()
    queue3=multiprocessing.Queue(maxsize = 1)
    queue4=multiprocessing.Queue()
    queue5=multiprocessing.Queue(maxsize = 1)
    hwqueue=multiprocessing.Queue(maxsize = 1)
    queuegamename = []

    #if 'raspberrypi' in platform.uname():
    #    ths=multiprocessing.Process(target=hotspot.hotspot, args=("Mobile Hotspot",))
    #    ths.start()
    #    print("mobile hotspot started")
    t1 = multiprocessing.Process(target=hardware_com.hardware_com, args=("Hardware_com", path, queue, queue4, size))
    t1.start()
    print("harware_com started")     
    t3 = multiprocessing.Process(target=mobile_com.mobile_com, args=("Mobile_com", path, queuegamename, queue, queue2, queue3, queue4, queue5, size, gamefiles, hwqueue))
    t3.start()
    print("mobile_com started")
    t4 = multiprocessing.Process(target=rgb_background.rgb_background, args=("rgb_background",))
    t4.start()
    print("background process started")
    t5 = multiprocessing.Process(target=led_calibration_temp.led_calibration_temp, args=("led_calibration_temp",))
    t5.start()
    print("led calibration process started")


    while True:
        time.sleep(0.5)
        if str(hwqueue.get())=="off":
            t1.terminate()
            t1 = multiprocessing.Process(target=hardware_com.hardware_com, args=("Hardware_com", path, queue, queue4, size))
            time.sleep(0.5)
            t1.start()
		
    

if __name__ == '__main__':
    main()



