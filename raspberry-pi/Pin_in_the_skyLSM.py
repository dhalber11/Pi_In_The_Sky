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
    while True:
        displaceAlt = altimeter.altitude - startAlt
        if displaceAlt >= releaseAlt:
            dropped = True
        while dropped == True:
            time_elapsed = time.monotonic()
            Xaccel = sensor.acceleration[0] # Reads the X acceleration
            Yaccel = sensor.acceleration[1]
            Zaccel = sensor.acceleration[2]
            Alt = altimeter.altitude

            datalog.write(f"{time_elapsed},{Xaccel},{Yaccel},{Zaccel},{Alt}\n") # Put the data into a chart
            datalog.flush() # Save the data
            time.sleep(.1)