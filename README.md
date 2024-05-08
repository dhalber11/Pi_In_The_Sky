# Pi_In_The_Sky- 2023/24
## Grant Gastinger and Dylan Halbert
<img src= "https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/Goofy.png?raw=true" width= 500>
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
For the first week of CAD testing I wanted to make sure that the most difficult and lengthy design process came first. Looking at all of the options I figured out that the wings would be the most lengthy process and I tried to free hand design some ailerons, as our idea was to make many aielerons and cover them in some substance. This quickly proved to be difficult and I ended up finding an online feature studio that allows the user to generate ailerons in a very efficient manner. This allowed me to use NACA digits to make airfoils, which I spent this week working on.

### Week 2 (1/15 - 1/19) 
#### Code Progress
After some testing with the MPU 6050 and analyzing data, I realized that the data it produced was highly inaccurate. I realized that for our objectives, this microcomputer would not work. After some research, I found out that a sister to the MPU, the LSM, uses the same syntax but is much more accurate and precise with data. We got the LSM up and running this week after some trouble with library calling syntaxes.

#### CAD Progress
Following some tweaking and continued work on the wings we came up with a system of using three bamboo skewers to hold the wings together and as the base of our wings. I then started the process of designing a fuselage to attach to the wings that I had already designed. Thinking back to this moment, I would reccomend that I had started with the fuselage and then designed the wings based off of that. My reasoning being simply making the weight more evenly dispersed with the entire fuselage and being able to place the wings more specifically.

### Week 3 (1/22 - 1/26) 
#### Code Progress
At this point, I was getting very solid data but it was a complete mess and would be almost impossible to read if you hadn't written the code. I wrote some code to organize the data into columns in relation to time. I also put headers in so we could put this data into a Google chart and graph it.

#### CAD Progress
Week three continued the process of designing the fuselage and making improvements and tweaks to the fit and design of the whole body. This was a relatively quick process for version 1 as there was not much extensive design with the fuselage. The general design was  

### Week 4 (1/29 - 2/2) 
#### Code Progress
Wiring week! This week I organized all the wires and planned where I would solder all of the wires on the prototyping shield for the pico. This was a very difficult task because I only had limited space on the pico shield and I had a lot of pins that I had to place on the board. I also ended up soldering the shield on the board the wrong way which was a big setback. However, by the end of the week, I had the shield on the board correctly and a plan of where I would fix the wires.

<img src= "https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/Screenshot%2024-04-17%091529.png?raw=true" width= 500>
Final Wiring Diagram

#### CAD Progress
This week I began the first fabrication and making of the v.1 wings. I decided to use plastic sheeting that we had spare in the back of the lab from covid times, it used to be used for face masks and seemed to work wonders as a shrink wrap for the ailerons on the wings. Using a heat gun I went along and tried to secure it down, eventually with the help of some hot glue it was done. However the issue that arose was the weight along with the finish of the plastic on the wings. There was a large amount of bumps and rough patches on the wings from where the heat gun either hadn't been or had burnt the plastic. This left a rough and unproffesional looking finish on the wings that coupled with the weight was not something I was happy with. Although they were wings that looked the part. 
<img src= "(https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/v1%20top%20down.jpg?raw=true)" width= 300>
##### This is the first version of V.1 before adding brackets for extra stability

### Week 5 (2/5 - 2/9) 
#### Code Progress
This was the big week for soldering. Luckily it went pretty smoothly with the headers and main modules getting locked in within the first few days. I did have to double-solder some pins to 3v because there was only one pin on the board that provided this voltage. Additionally, there wasn't much space on the breadboard part of the shield so I had to have the battery floating around with only connections through the female-male wires which are traditionally meant to be soldered. However, it all worked in the end as the code ran with no problems on the soldered product.

#### CAD Progress
This week was basically a continuation of the last. Already seeing flaws in the first way of making the wings I knew there was a lot to be improved upon. The see-through wings was a good solution but it did not have the benefits of weight reduction. This brought me to think of other options but still reinforce the wings even more to prepare for next weeks launch. The wings also had a sag to them as they were not connected through the body of the plane, this brought a lot of flex to them that may have hurt the efficiency. To counteract this we tried to add a wire that ran along the top of the plane to each wingtip to support the wings. On top of this we added brackets to the top and bottom of the body of the fuselage to be able to both hold the wings and keep the box of the fuselage together. 

<img src= "https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/assemblyv.1.png?raw=true" width= 300>

##### This is the assembly of the V.1 plane

<img src= "(https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/v1%20side%20view.jpg?raw=true)" width= 300>

##### This is the fully fabricated version of the above CAD assembly, including the new brackets and wire for stability.

### Week 6 (2/12 - 2/16) 
#### Code Progress
Launch week! Not much happened on the code side of things because most of our energy went to preparing the plane for launch. The data tracking was tested as we threw our first prototype off the hill next to the CHS student parking lot. The plane itself had some rough flights but we got the data that we needed. I would consider this test a success on the code side of things because it recorded the data at the correct height and the modules stayed intact throughout all of the tests.

#### CAD Progress
This week brought a lot of lessons learned. The launch was not as great a success as hoped and the plane barely had any lift. We attributed this to the wing size and weight of the plane as well as where our CG(Center of Gravity) was located. This brought a lot of ideas for weight reduction and also new longer wings that used thicker and straighter dowels. These we found, would run through the entire body of the plane and fix the wings to a certain angle. This was helpful to increase stability and keep the wings straight. I also looked for options to move away from the plastic covering on the wings. To solve this we used paper normally used for teachers posters and room decoration. This was surprisingly lightweight and similar in texture to a thicker tissue paper so it provided a much cleaner finish over the wings without the cost of weight. Below is the most succesful flight that we had with the first version. 

<img src= "(https://github.com/dhalber11/Pi_In_The_Sky/blob/main/images/v.1success.gif?raw=true)" width= 400>

##### This was our proudest moment thus far

### Week 7 (2/19 - 2/23) 
#### Code Progress
Data analyzing week. I imported the data from an Excel file on the board into a Google sheet. The data was already formatted into organized columns based on acceleration and altitude so there wasn't much I needed to do there. However, I wanted to see what the data was saying more clearly so I graphed it on the Google sheet. The altitude was pretty clear except for a few outliers but the acceleration was all over the place. The next few weeks will need to be dedicated to smoothing out the acceleration readings and making more sense of them.

#### CAD Progress
This week was focused on improving and fabricating v.2. Looking back I do wish that we had taken more time to work on this and think through issues that may have arisen from the changing of the plane. This was a roughly smooth week however and the wings were coming along well. The new solution with paper was coming along very well as the glue we used held the paper on very nicely. 
### Week 8 (2/26 - 3/1)
#### Code Progress
This week I took a lesson from Paul Weder on how to filter data using the Pico. He uses a lot of niche libraries that can find what points are outliers and give them less weight on the average curve. Next, he used the trapezoid rule to take the integral of the acceleration curve and find its velocity and then position. I tried setting this method up on my computer but it didn't work because I had admin restrictions on the libraries I could download. Paul used his own computer so he didn't have that problem. After checking this out for a week, I realized it wouldn't work because crucial libraries like scipy were restricted.

#### CAD Progress 

### Week 9 (3/4 - 3/8)
#### Code Progress
This week was the start of the launch dropping mechanism. On the code side of things, the task was rather small because all we had to do was spin a servo to pull out a pin when the plane reached a certain height. My code was already organized to the point where I had separated it into lines that run before the drop and lines that run after. All I had to do was write a line that would make the servo turn to the closed position at the start and a line to open the servo up when the set altitude is reached. The benefits of keeping your code organized are great, especially down the road when you need to add something quickly.

#### CAD Progress
The dropping mechanism was relatively simple to assemble and complete, however I have to give much of the credit to Grant for this part as he was bored with code and wanted to try his hand at the CAD side of things. This mechanism was an addition to the already designed bracket that can be seen on v.1, we completed this by adding a solid ceiling and then mounting the servo on that. All together it didn't add that much weight as the servo was the only electronics added.
### Week 10 (3/11 - 3/15)
#### Code Progress
Not much happened in code this week because I had to do some last-minute Onshape and assembly so that we could launch before spring break. However, I did play around with the dropping height to figure out what a good test would be and settled upon 10 meters. 10 meters wasn't too high that it would get destroyed if it crashed but high enough that it would have time to recover and possibly glide before it hit the ground.

#### CAD Progress


### Week 11 (3/18 - 3/22)
#### Code Progress
Launch week (and the last real week before spring break)! The difference in this test was that we were dropping it from the drone as others were just thrown from a hill. There were many problems in this test but I'll just stick to the code ones and let Dylan go over the physical problems. The problem with the code was that the servo wasn't spinning because a wire was unplugged. The pin was not put in solidly because the servo wasn't getting any voltage. In the future, I will solder the servo wires so that they can stay connected.

#### CAD Progress
For this launch we decided to try out the drone drop system as we were confident that the glider might fly with a little more height. Our first mistake was setting the height to 10 meters where it woudld drop. The next issue was the prop blast from the drone, the down force hit the wings as the drone took of and made the plane swing around wildly almost taking out the drone in the process. This wild swinging is what ended up breaking the drop pin and sending the plane plummeting to the ground. All in all it was a helpful test to show us the fatal flaws in our system. We need to find some way to seperate or immobilize the plane before it is dropped as well as move weight around in the plane to make it more stable in the air. This was the end of V.2 and we moved on to making the third version after this test.
### Week 12 (4/8 - 4/12)
#### Code Progress
Another issue we had with this launch was that we didn't seal the top up and so the LSM module flew out when the glider dropped. We spent an entire day searching for it in the grass but ended up just having to use a new one. It took a little while to set this back up with soldering and finding the I2C number of the device. So that this won't happen again, I got into onshape and redesigned the top so that all of the modules would be sealed inside of the plane.

#### CAD Progress

### Week 13 (4/15 - 4/19)
#### Code Progress
This week I took another look at acceleration and did some tests to see if we could do anything with it. However, the data we were collecting was way too inaccurate so we decided to focus more on elevation data. We borrowed the capsule that Nick and Ali designed and dropped the pico from the balcony to collect data. The elevation height over time was very precise and gave us a good measurement of height over time. I think we are going to pivot to using height instead of acceleration as our main data from the glider.

#### CAD Progress

### Week 14 (4/22 - 4/26)
#### Code Progress
This week I had to redesign the servo-dropping mechanism because the top of the plane broke when we changed the size of the plane. I made it a lot more symmetrical so that the weight wouldn't carry it to one side or another. Once we printed it, I had to find all of the angles of the servo again so that I could calculate how far we needed it to turn to pull the pin out. A significant change I made to this system was that the pin was a balsa dowel instead of 3D printed material to reduce friction. On the dowel, I drilled a hole and put a wire through instead of string because that broke last time. This mechanism works a lot cleaner than the previous one because of these changes. 

#### CAD Progress

### Week 15 (4/29 - 5/3)
#### Code Progress
This week our plan was to launch on Thursday or Friday but weather and other issues kept us from going. The only change I made in the code was the drop height which I increased to 20 meters. Other than that I was helping Dylan to assemble this plane and get it ready for flying next week.

#### CAD Progress

### Week 16 (5/6 - 5/10)
#### Code Progress

#### CAD Progress
