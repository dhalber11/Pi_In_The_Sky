# Pi_In_The_Sky- 2023/24
## Grant Gastinger and Dylan Halbert
&nbsp;
## Table of Contents
* [Project_Proposal]()
&nbsp;
## Project Proposal
### Criteria
* Survivability: the payload (RPi Pico, sensors, etc) must survive and function post-flight.
* Custom circuit board: breadboards are for prototyping, not for finished products.  Solder headers onto your board so everything is compact but you can add/remove the Pico and other sensors.
* Data collection: your payload must collect data throughout the flight and save that data to the Pico’s onboard storage. Examples: spin rate (MPU6050), altitude (MPL3115A2), location (GPS).
* Data presentation: Show off the data you collected! Plot the data in some way that is meaningful to your project.
### Overview
For this assignment, we are given a very broad range of possibilities. The criteria above are the only set rules for this project. Seeing the project's name, we had the idea of designing, building, and flying a glider that met the criteria. We originally came up with two different possibilities for launching the glider that we proposed. The first was to design and build a rail launching system using bands or some other static propulsion. The other was to drop the glider from a drone that would carry it to a higher altitude and then allow it to glide and collect data. While both are acceptable ways of launching a plane they have their differences. The one thing that would stay the same would be the glider. While both options have their challenges they are both viable options for collecting data.

### Materials
* Purchased Glider? (Foam/Balsa)
* Pico
* Laser cut balsa
* Big rubber bands
* Wires
* Solder
* MPU 
* Screws
* Wax paper/covering for frame
<img src= "https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/2%20Planes.png?raw=true" width= 300>

##### This is a possible testing glider
&nbsp;

### Objectives
These objectives mainly encompass the values that we want to track during our flight. 
Those are: 
* Tracking Altitude
* Tracking Hang Time
### Sketches + Images
<img src= "https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/2%20Wings.png?raw=true" width= 300>
<img src= "https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/Sketches.jpg?raw=true" width= 1000>

##### This is what our wings will most likely look like with a paper-covering

### Rail-Launched Glider 
#### Pros
* Satisfaction of launch by hand
* Starts with a high acceleration (Cooler data?)
* Plane could be bigger
* More control of the aim
#### Cons 
* Low start height(less distance)
* Might not get too high
* Good rubber bands may be hard to find
* Difficult to fabricate launch rail
&nbsp;
### Drone-Dropped Glider
#### Pros 
* Constant controllable start altitude'
* Longer flight time
* Consistency
#### Cons
* Limited weight
* Limited flying conditions
&nbsp;
### The Look of Success
If we are successful, our glider will soar through the air for a decent amount of time and collect the hang time and altitude while doing so. The glider will not crash in a hard way that destroys any of its mechanics. The data will then be graphed in an easily comprehensible way. 
&nbsp;
### Schedule/Milestones
* Finish Planning - First week of December
* Initial Code (works on the ground) done - End of January
* Rough Prototype that just flies by hand - End of January
* Prototype complete - 2/28
* Ready for Launch - 3/30
* Everything Finished - 5/19

## The Project
After reviewing the possibilities and looking over options and logistics for both of the above options. We settled on the drone dropped version of this glider. This would use a simple servo mechanism to drop the glider at a certain altitude. As well as capture in flight data as it <falls> glides to the ground
### Finalized Materials
* Basswood and Balsa (Fuselage and wings)
* Dowels (Wing struts)
* ABS (Main body supports)
* Clear thermoplastic (Initial Prototype Wing covering)
* Paper (Wing covering)
* Pico W (with Pi Cowbell)
* Accelerometer
* Servo
* Altimeter
* Switch and Battery


### Initial Code

### Initial Cad
Cad for this project was started with the wings. Using a community sourced feature studio that allowed for the use and generation of NACA airfoils in Onshape. This was extremely helpful to design and test many different airfoils quickly.


###
