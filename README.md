# Pimoroni STS PI ROS Gazebo Simulation

This provides a Gazebo Simulation and ROS wrapper for Pimoroni STS PI.  Allows you to control your Pimoroni STS PI from your PC running ROS. Uses standard Twist. 


[![Youtube sumo](http://forthtemple.com/pimoroni/pimoroniyoutube.jpg)](https://www.youtube.com/watch?v=zDb48-HvZDI) 

https://github.com/sandyjmacdonald/sts_pi_controller

# Installation
Install ROS (eg http://wiki.ros.org/indigo/Installation/Ubuntu if from ubuntu)

```
cd ~/catkin_ws/src
git clone https://github.com/forthtemple/ros_pimoroni_sts_pi.git
cd ~/catkin_ws
catkin_make 
```
# Running
In one terminal run the following specifying the IP address of your Raspberry PI:
```
roslaunch pimoroni_sts_pi pimoroni_sts_pi.launch ip_address:=192.168.1.107
```
On another terminal to control your STS PI via a keyboard use:
```
rosrun pimoroni_sts_pi teleop_twist_keyboard.py
```

To record a real Pimoroni STS PI
```
rosbag record cmd_vel
```
To play it to your Gazebo Pimoroni STS PI replace xx-xxx-xx with your recorded bag file name
```
rosbag play xx-xxx-xx.bag
```
