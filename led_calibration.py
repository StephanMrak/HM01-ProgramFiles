def led_calibration(threadname):
    import smbus2
    import time
    bus=smbus2.SMBus(1)
    address=0x2c
    bus.write_byte_data(address,0,0)
    
if __name__ == '__main__':
    led_calibration('thread')