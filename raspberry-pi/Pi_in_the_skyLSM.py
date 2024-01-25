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
    #datalog.write("Time(s),X-accel,Y-accel,Z-accel,X-tilt,Y-tilt,Z-tilt,Altitude(m)\n") # Put the data into a chart
    datalog.write(f"time_elapsed,X-accel,Y-accel,Z-accel,Xvelocity,Yvelocity,Zvelocity,Alt")
    datalog.flush()
    while True:
        time_elapsed = time.monotonic()
        #datalog.write(f"{time_elapsed}, , , , , , ,{altimeter.altitude}\n")
        #datalog.flush() # Save the data
        displaceAlt = altimeter.altitude - startAlt
        if displaceAlt >= releaseAlt:
            dropped = True

        while dropped == True:
            time_elapsed = time.monotonic()
            Xa = sensor.acceleration[0] # Reads the X acceleration
            Ya = sensor.acceleration[1]
            Za = sensor.acceleration[2]
            Alt = altimeter.altitude
            Xg = sensor.gyro[0]
            Yg = sensor.gyro[1]
            Zg = sensor.gyro[2]

            time.sleep(.2)

            Xv = ((sensor.acceleration[0] + Xa)/2) * (time.monotonic() - time_elapsed)
            Yv = ((sensor.acceleration[1] + Ya)/2) * (time.monotonic() - time_elapsed)
            Zv = ((sensor.acceleration[2] + Za)/2) * (time.monotonic() - time_elapsed)

            #datalog.write(f"{time_elapsed},{Xa},{Ya},{Za},{Xg},{Yg},{Zg},{Xv},{Yv},{Zv},{Alt}\n") # Put the data into a chart
            datalog.write(f"{time_elapsed},{Xa},{Ya},{Za},{Xv},{Yv},{Zv}\n")
            datalog.flush() # Save the data