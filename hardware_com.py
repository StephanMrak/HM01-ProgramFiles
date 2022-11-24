def hardware_com(threadname, path, q, q4, size):
    import serial
    import time
    import multiprocessing
    from queue import Queue
    import hmsysteme
    import platform
    import matplotlib.pyplot as plt
    import numpy as np
    thislist = []
    ser = []
    riegel = [0, 0, 0, 0]
    data = [[], [], [], []]
    counter = 0
    start = 0
    foto_list = []
    count_list = []
    values = []
    blaval = []
    thresh = 1
    ind = []
    ind_val = []
    lengths = []
    mittelwert = [0, 0]
    pos_led1 = 0.13
    pos_led2 = 0.27
    d_lenght = 0.341
    d_height = 0.193
    d_offset = -0.01
    diode_length = 196 / 64 / 1000
    pixelw = d_lenght / size[0]
    pixelh = d_height / size[1]
    laenge = 0.4
    hoehe = 0.255
    l = 0.195
    x = [0, 0]
    y = [0, 0]
    coordinates = [0, 0]

    # try:
    #     import smbus2
    #     import time
    #     bus=smbus2.SMBus(1)
    #     address=0x2c
    #     bus.write_byte_data(address,0,105)
    # except:
    #     print("only usable on HM01")

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

    led_calib(200)

    def ardreset():
        try:
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(14, GPIO.OUT)
            GPIO.output(14, 0)
            time.sleep(0.1)
            GPIO.output(14, 1)
            time.sleep(1)
            print("arduino reset")
        except Exception as e:
            print(e)

    def ardwatcher(seri):
        print(seri.readline().decode("ascii"), "started")
        return

    # ardreset()

    for com in range(0, 10):
        try:
            # PORT = '/dev/ttyCOM' + str(com)
            # PORT = '/dev/ttyACM3'
            PORT = '/dev/ttyUSB' + str(com)  # raspi
            # PORT = 'COM'+ str(com) #Windows
            counter = counter + 1
            BAUD = 115200
            board = serial.Serial(PORT, BAUD)
            thislist.insert(counter, PORT)
            print("Arduino found at ", PORT)

            # board.close()

        except Exception as e:
            # print(e)
            print("Arduino not found")
    # gefundenen Port öffnen

    # for i in range(0,len(thislist)):
    #    DEVICE = str(thislist[i])
    #    ser.insert(i, serial.Serial(DEVICE, BAUD))
    i = 0
    while i < len(thislist):
        try:
            DEVICE = str(thislist[i])
            ser.insert(i, serial.Serial(DEVICE, BAUD))
            print(i)
            i = i + 1

        except Exception as e:
            print(e)
            time.sleep(0.5)

    t = []
    # for i in range(0,len(thislist)):
    #    t.append(multiprocessing.Process(target=ardwatcher, args=(ser[i],)))
    #    t[i].start()
    # for i in range(0,len(thislist)):
    #    t[i].join()
    # for i in range(0, len(thislist)):
    #    ser[i].write(b'1')
    for i in range(0, len(thislist)):
        ser[i].write(b'2')
    for i in range(0, len(thislist)):
        print(ser[i].readline().decode("ascii"), "started")

    for i in range(0, len(thislist)):
        ser[i].write(b'1')
    print("reset successful")


    while True:
        time.sleep(0.01)
        for k in range(0, len(thislist)):
            while (ser[k].inWaiting() > 0):
                # if ser[k].readline().decode("ascii") !='init\r\n':
                data[k].append(ser[k].readline().decode("ascii"))
                time.sleep(0.001)
                # ser[k].write(b'0')
                # start=timer()
                # print(data[k])

            if (len(data[k]) > 0 and riegel[k] == 0):
                if (data[k][-1] == 'end\r\n' and data[k][0] == 'start\r\n'):
                    riegel[k] = 1

            if (sum(riegel) == len(thislist)):
                try:
                    for z in range(len(thislist)):
                        data[z].pop(0)
                        data[z].pop(len(data[z]) - 1)
                        data[z] = list(map(int, data[z]))
                        for i in range(0, (int(len(data[z]) / 2))):
                            foto_list.append(data[z][2 * i])
                            count_list.append(data[z][(2 * i) - 1])

                    print("")
                    print(data)

                    for i in range(0, max(foto_list) + 1):
                        values.append(0)
                        blaval.append(i)

                    for i in range(0, max(foto_list) + 1):
                        for j in range(0, len(foto_list)):
                            if i == foto_list[j]:
                                values[i] = count_list[j]

                    for i in range(0, len(values)):
                        if values[i] >= thresh:
                            ind.append(i)
                            ind_val.append(values[i])

                    while len(ind) > 2:
                        lengths.clear()
                        for i in range(0, len(ind) - 1):
                            lengths.append(ind[i + 1] - ind[i])
                        # print('Lenghts are: %s' % (lengths))
                        for j in range(0, len(lengths)):
                            if lengths[j] == min(lengths):
                                ind[j] = (ind[j] * ind_val[j] + ind[j + 1] * ind_val[j + 1]) / (
                                            ind_val[j] + ind_val[j + 1])
                                ind.pop(j + 1)
                                ind_val[j] = ind_val[j] + ind_val[j + 1]
                                ind_val.pop(j + 1)
                                break
                    # print('indexes are: %s' % (ind))
                    print(foto_list)
                    print(count_list)

                    q4.put([str(foto_list), str(count_list)])

                    if len(ind) > 1:
                        mittelwert[0] = ind[0]
                        mittelwert[1] = ind[1]
                        ind.clear()
                        ind_val.clear()
                        if mittelwert[0] <= 64:
                            y[0] = hoehe - (((65 - mittelwert[0]) * diode_length)) - 0.003
                            x[0] = 0.002
                        elif mittelwert[0] > 64 and mittelwert[0] <= 192:
                            x[0] = (mittelwert[0] - 64) * diode_length  # + 0.004
                            y[0] = hoehe - 0.003
                        elif mittelwert[0] > 192:
                            y[0] = hoehe - (((mittelwert[0] - 192) * diode_length))  # -0.003
                            x[0] = laenge - 0.002

                        if mittelwert[1] <= 64:
                            y[1] = hoehe - (((65 - mittelwert[1]) * diode_length)) - 0.003
                            x[1] = 0.002
                        elif mittelwert[1] > 64 and mittelwert[1] <= 192:
                            x[1] = (mittelwert[1] - 64) * diode_length  # + 0.004
                            y[1] = hoehe - 0.003
                        elif mittelwert[1] > 192:
                            y[1] = hoehe - (((mittelwert[1] - 192) * diode_length))  # -0.003
                            x[1] = laenge - 0.002

                        if len(mittelwert) > 1:
                            if mittelwert[0] > 0 and mittelwert[
                                1] > 0:  # and mittelwert[2]==0 and mittelwert[3]==0 and mittelwert[4]==0:
                                if x[0] == pos_led2:
                                    x_1 = pos_led2
                                    y_1 = hoehe / (x[1] - pos_led1) * (x_1 - pos_led1)
                                elif x[1] == pos_led1:
                                    x_1 = pos_led1
                                    y_1 = hoehe / (x[0] - pos_led2) * (x_1 - pos_led2)
                                else:
                                    # x_1=((-pos_led2/(x[0]-pos_led2))+pos_led1/(x[1]-pos_led1))/((1/(x[1]-pos_led1))-(1/(x[0]-pos_led2)))
                                    x_1 = ((-y[0] * pos_led2 / (x[0] - pos_led2)) + y[1] * pos_led1 / (
                                                x[1] - pos_led1)) / (
                                                  (y[1] / (x[1] - pos_led1)) - (y[0] / (x[0] - pos_led2)))
                                    y_1 = y[0] / (x[0] - pos_led2) * (x_1 - pos_led2)
                                # print('coordinates are: x %f and y %f' % (x_1, y_1))
                                coordinates[0] = (x_1 - ((laenge - d_lenght) / 2)) / pixelw
                                coordinates[1] = (size[1] - ((y_1 - (hoehe - d_height + d_offset)) / pixelh))

                                if mittelwert[0]<=64 and mittelwert[1]<=64: #zone1
                                    coordinates[0] = coordinates[0] - (0.000 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.017 / pixelw)
                                    print("zone 1")

                                if mittelwert[0]<=64 and 64<mittelwert[1]<=128: #zone2
                                    coordinates[0] = coordinates[0] + (0.003 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.012 / pixelw)
                                    print("zone 2")

                                if 64<mittelwert[0]<=128 and 64<mittelwert[1]<=128: #zone3
                                    coordinates[0] = coordinates[0] + (0.001 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.015 / pixelw)
                                    print("zone 3")

                                if 64<mittelwert[0]<=128 and 128<mittelwert[1]<=192: #zone4
                                    coordinates[0] = coordinates[0] + (0.002 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.012 / pixelw)
                                    print("zone 4")

                                if 128<mittelwert[0]<=192 and 128<mittelwert[1]<=192: #zone5
                                    coordinates[0] = coordinates[0] + (0.003 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.015 / pixelw)
                                    print("zone 5")

                                if 128<mittelwert[0]<=192 and 192<mittelwert[1]<=256: #zone6
                                    coordinates[0] = coordinates[0] + (0.003 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.017 / pixelw)
                                    print("zone 6")

                                if 192<mittelwert[0]<=256 and 192<mittelwert[1]<=256: #zone7
                                    coordinates[0] = coordinates[0] - (0.001 / pixelh)
                                    coordinates[1] = coordinates[1] - (0.012 / pixelw)
                                    print("zone 7")

                                #fig, ax = plt.subplots()
                                #ax.plot(foto_list, count_list, 'bo')
                                #plt.show()
                                print("coordinates")
                                print(coordinates)
                                hmsysteme.put_pos(coordinates)
                                hmsysteme.put_hit()
                                q.get()

                    riegel = [0, 0, 0, 0]
                    data = [[], [], [], []]
                    foto_list.clear()
                    count_list.clear()
                    values.clear()
                    blaval.clear()
                    ind.clear()
                    ind_val.clear()
                    print(time.time() - start)
                    start = time.time()
                    time.sleep(0.5)

                    for i in range(0, len(thislist)):
                        ser[i].write(b'1')
                        ser[i].reset_input_buffer()
                except Exception as e:
                    print(e)
                    time.sleep(0.5)
                    riegel = [0, 0, 0, 0]
                    data = [[], [], [], []]
                    foto_list.clear()
                    count_list.clear()
                    values.clear()
                    blaval.clear()
                    ind.clear()
                    ind_val.clear()
                    for i in range(0, len(thislist)):
                        ser[i].write(b'1')
                        ser[i].reset_input_buffer()

            if (riegel[k] == 0):
                data[k].clear()
