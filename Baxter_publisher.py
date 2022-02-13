#!/usr/bin/env python
# license removed for brevity
import rospy
from baxter_interface import CHECK_VERSION
from baxter_core_msgs.msg import JointCommand


joint_publisher = rospy.Publisher('/robot/limb/left/joint_command', JointCommand, queue_size=10)
cmd=JointCommand()
cmd.mode=1
cmd.names = ["left_s0", "left_s1", "left_e0", "left_e1", "left_w0", "left_w1","left_w2"]
cmd.command = [0, 0, 0, 0, 0, 0,0]

def move0():
    global cmd
    cmd.command[0] = 0
    cmd.command[1] = 0
    cmd.command[2] = 0
    cmd.command[3] = 0
    cmd.command[4] = 0
    cmd.command[5] = 0
    cmd.command[6] = 0


    joint_publisher.publish(cmd)
    rospy.sleep(1)


def movea():
    global cmd
    i=0
   

    while(i<32):
        cmd.command[0]-=0.01
        joint_publisher.publish(cmd)
        rospy.sleep(0.1)
        i+=1


def moveb():
    global cmd
    i=0
   

    while(i<32):
        cmd.command[0]+=0.01
        joint_publisher.publish(cmd)
        rospy.sleep(0.1)
        i+=1



if __name__ == '__main__':
    rospy.init_node('Movement')
    try:
        move0()
        while not rospy.is_shutdown():
            movea()
            moveb()


    except rospy.ROSInterruptException:
        pass