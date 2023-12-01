#type:ignore
import board
import time
import adafruit_mpu6050
import busio

sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
mpu = adafruit_mpu6050.MPU6050(i2c) # Sets up the MPU

startAlt = altimeter.altitude
releaseAlt = 10000
dropped = False

with open("/data.csv", "a") as datalog: #When Data Mode is Active
    while True:
        displaceAlt = altimeter.altitude - startAlt
        if displaceAlt >= releaseAlt:
            dropped = True
        while dropped == True:
            time_elapsed = time.monotonic()
            Xaccel = mpu.acceleration[0] #Reads the X acceleration
            Yaccel = mpu.acceleration[1]
            Zaccel = mpu.acceleration[2]
            Alt = altimeter.altitude

            datalog.write(f"{time_elapsed},{Xaccel},{Yaccel},{Zaccel},{Alt}\n") #Put the data into a chart
            datalog.flush() # Save the data
            time.sleep(.1)