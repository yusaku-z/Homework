#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

if __name__== '__main__':
    print"モールス信号の練習を始めます"
    print"「・」は「t」, 「-」は「-」で入力"
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', String, queue_size=50)
    rate = rospy.Rate(1)

    while  not rospy.is_shutdown():
       n = raw_input()
        
       pub.publish(n)
       rate.sleep()
