#type:ignore
import time
import board
import busio
import adafruit_mpl3115a2
import pwmio
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX
from adafruit_motor import servo

sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c

sensor = LSM6DSOX(i2c, address=0x6a) # Set up the LSM
altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60) # Set up the altimeter

pwm = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin A2.
my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500) # Define the servo

startAlt = altimeter.altitude #Find Ground Zero
releaseAlt = 20 # In meters
dropped = False

with open("/data.csv", "a") as datalog: # When Data Mode is Active
    datalog.write("Time(s),X-accel,Y-accel,Z-accel,Altitude(m)\n") # Set headers for the graph
    datalog.flush() # Put the data into a chart
    my_servo.angle = 180  # Locks with drone

    while True:

        time_elapsed = time.monotonic()
        displaceAlt = altimeter.altitude - startAlt # Find distance from ground
        if displaceAlt >= releaseAlt: # When drop height is reached
            my_servo.angle = 120 # Bombs awayyyyy
            dropped = True
            
        while dropped == True:
            time_elapsed = time.monotonic()

            Xa,Ya,Za = sensor.acceleration # Sensor readings
            Alt = altimeter.altitude # Altitude readings
            Xg,Yg,Zg = sensor.gyro
          
            time.sleep(.00001) # So there isn't an overload

            datalog.write(f"{time_elapsed},{Xa},{Ya},{Za},{Alt}\n") # Compile the data
            datalog.flush() # Save the data
