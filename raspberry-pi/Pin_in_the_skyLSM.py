#type:ignore
import time
import board
import busio
import adafruit_mpl3115a2
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c


sensor = LSM6DSOX(i2c, address=0x6a)
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)

startAlt = altimeter.altitude
releaseAlt = 3
dropped = False

with open("/data.csv", "a") as datalog: # When Data Mode is Active
    datalog.write("Time(s),X-accel,Y-accel,Z-accel,X-tilt,Y-tilt,Z-tilt,Altitude(m)\n") # Put the data into a chart
    datalog.flush
    while True:
        time_elapsed = time.monotonic()
        datalog.write(f"{time_elapsed}, , ,{Zaccel}, , , ,{altimeter.altitude}\n")
        datalog.flush() # Save the data
        displaceAlt = altimeter.altitude - startAlt
        if displaceAlt >= releaseAlt:
            dropped = True

        while dropped == True:
            time_elapsed = time.monotonic()
            Xaccel = sensor.acceleration[0] # Reads the X acceleration
            Yaccel = sensor.acceleration[1]
            Zaccel = sensor.acceleration[2]
            Alt = altimeter.altitude
            Xtilt = sensor.gyro[0]
            Ytilt = sensor.gyro[1]
            Ztilt = sensor.gyro[2]

            datalog.write(f"{time_elapsed},{Xaccel},{Yaccel},{Zaccel},{Xtilt},{Ytilt},{Ztilt},{Alt}\n") # Put the data into a chart
            datalog.flush() # Save the data
            time.sleep(.1)