#!/usr/bin/env python
import rospy
import urllib2
import sys
from geometry_msgs.msg import Twist
#response = urllib2.urlopen('http://192.168.1.107/forward')
#html = response.read()

def callback(msg):
    #ip = '192.168.1.107'
    global ip
    if msg.linear.x>0:
         urllib2.urlopen('http://'+ip+'/forward')
    elif msg.linear.x<0:
         urllib2.urlopen('http://'+ip+'/back')
    elif msg.angular.z>0:
         urllib2.urlopen('http://'+ip+'/clockwise')
    elif msg.angular.z<0:
         urllib2.urlopen('http://'+ip+'/anti-clockwise')
    else:
         urllib2.urlopen('http://'+ip+'/stop')

if __name__ == '__main__':
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    if len(sys.argv) < 2:
        print("usage: roslaunch pimoroni_sts_pi pimoroni_sts_pi.launch ip_address:=xxx.xxx.xxx.xxx")
    else:
        ip = sys.argv[2]
        rospy.init_node('cmd_vel_listener')#, anonymous=True)

        rospy.Subscriber("/cmd_vel", Twist, callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

