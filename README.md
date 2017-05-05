# ros_pimoroni_sts_pi

ROS wrapper for Pimoroni STS PI. Uses standard Twist. The idea is you have your Raspberry PI on your Pimoroni STS PI and you can control your Pimoroni from your PC via ROS

# Installation

```
cd ~/catkin_ws/src
git clone https://github.com/forthtemple/ros_pimoroni_sts_pi.git
cd ~/catkin_ws
catkin_make 
```
# Running
In on terminal run specifying the IP address of your Raspberry PI:
```
roslaunch pimoroni_sts_pi pimoroni_sts_pi.launch ip_address:=192.168.1.107
```
To control it use:
```
rosrun pimoroni_sts_pi teleop_twist_keyboard.py
```
