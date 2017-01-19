#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def cb(message):
    if message.data == "t-":
        print "A"
    if message.data == "-ttt":
        print "B"
    if message.data == "-t-t":
        print "C"
    if message.data == "-tt":
        print "D"
    if message.data == "t":
        print "E"
    if message.data == "tt-t":
        print "F"
    if message.data == "--t":
        print "G"
    if message.data == "tttt":
        print "H"
    if message.data == "tt":
        print "I"
    if message.data == "t---":
        print "J"
    if message.data == "-t-":
        print "K"
    if message.data == "t-tt":
        print "L"
    if message.data == "--":
        print "M"
    if message.data == "-t":
        print "N"
    if message.data == "---":
        print "O"
    if message.data == "t--t":
        print "P"
    if message.data == "--t-":
        print "Q"
    if message.data == "t-t":
        print "R"
    if message.data == "ttt":
        print "S"
    if message.data == "-":
        print "T"
    if message.data == "tt-":
        print "U"
    if message.data == "ttt-":
        print "V"
    if message.data == "t--":
        print "W"
    if message.data == "-tt-":
        print "X"
    if message.data == "-t--":
        print "Y"
    if message.data == "--tt":
        print "Z"
    if message.data == "ttt---ttt":
        print "SOS"

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', String, cb)
    rospy.spin()
