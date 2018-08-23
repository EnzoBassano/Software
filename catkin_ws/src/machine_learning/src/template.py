#!/usr/bin/env python

import rospy #importar ros para python
import cv2
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped

class Controller(object):
	def __init__(self, args):
		

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	#rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
