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
We already had the data collection set up from our previous code assignments in class (Data Part 1 and 2) so that was what we used.

### Initial Cad
Cad for this project was started with the wings. Using a community sourced feature studio that allowed for the use and generation of NACA airfoils in Onshape. This was extremely helpful to design and test many different airfoils quickly.


## Week by Week 

### Week 1 (1/8 - 1/12) 
#### Code Progress
This week I designed a system that would record the initial altitude and subtract that from the current altitude to find the height off the ground. When the height reaches a certain altitude (3 meters for testing) it will say that the plane has dropped and data collection will start. Using this system we will only record the necessary data of the actual flight and not the movement before.

#### CAD Progress


### Week 2 (1/15 - 1/19) 
#### Code Progress
After some testing with the MPU 6050 and analyzing data, I realized that the data it produced was highly inaccurate. I realized that for our objectives, this microcomputer would not work. After some research, I found out that a sister to the MPU, the LSM, uses the same syntax but is much more accurate and precise with data. We got the LSM up and running this week after some trouble with library calling syntaxes.

#### CAD Progress

### Week 3 (1/22 - 1/26) 
#### Code Progress
At this point, I was getting very solid data but it was a complete mess and would be almost impossible to read if you hadn't written the code. I wrote some code to organize the data into columns in relation to time. I also put headers in so we could put this data into a Google chart and graph it.

#### CAD Progress


### Week 4 (1/29 - 2/2) 
#### Code Progress
Wiring week! This week I organized all the wires and planned where I would solder all of the wires on the prototyping shield for the pico. This was a very difficult task because I only had limited space on the pico shield and I had a lot of pins that I had to place on the board. I also ended up soldering the shield on the board the wrong way which was a big setback. However, by the end of the week, I had the shield on the board correctly and a plan of where I would fix the wires.

#### CAD Progress


### Week 5 (2/5 - 2/9) 
#### Code Progress
This was the big week for soldering. Luckily it went pretty smoothly with the headers and main modules getting locked in within the first few days. I did have to double-solder some pins to 3v because there was only one pin on the board that provided this voltage. Additionally, there wasn't much space on the breadboard part of the shield so I had to have the battery floating around with only connections through the female-male wires which are traditionally meant to be soldered. However, it all worked in the end as the code ran with no problems on the soldered product.

#### CAD Progress



### Week 6 (2/12 - 2/16) 
#### Code Progress
Launch week! Not much happened on the code side of things because most of our energy went to preparing the plane for launch. The data tracking was tested as we threw our first prototype off the hill next to the CHS student parking lot. The plane itself had some rough flights but we got the data that we needed for analyzing. I would consider this test a success on the code side of things because it recorded the data at the correct height and the modules stayed intact throughout all of the tests.

#### CAD Progress


### Week 7 (2/19 - 2/23) 
#### Code Progress


#### CAD Progress
