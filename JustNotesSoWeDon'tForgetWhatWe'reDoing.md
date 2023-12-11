https://keyglove.net/2011/10/12/acceleration-velocity-position-and-dead-reckoning/
  *This website has a lot of stuff on dead reckoning
*Maybe try to get intervals of data to 1 second exactly?

// velocity
vx += ((ax + ax0)/2) * (t - t0);
vy += ((ay + ay0)/2) * (t - t0);
vz += ((az + az0)/2) * (t - t0);

// position;
px += ((vx + vx0)/2) * (t - t0);
py += ((vy + vy0)/2) * (t - t0);
pz += ((vz + vz0)/2) * (t - t0);
