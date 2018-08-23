#!/usr/bin/env python

import rospy #importar ros para python
import cv2 as cv
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class Velreal(object):
	def __init__(self,args):
		self.suscriber = rospy.Subscriber("/duckiebot/camera_node/image/rect",Image,self.callback_image)
		self.publisher = rospy.Publisher("/duckiebot/camera_node/image/rect/patos", Image, queue_size=1)
		self.bridge = CvBridge()
		self.img = Image()
		self.duck_cascade = cv.CascadeClassifier('/home/duckiebot/duckietown/catkin_ws/src/ros_cap/src/cascade3(LBP).xml')

	def callback_image(self,msg):
		img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
		img=img[90:240,0:320]
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		ducks = self.duck_cascade.detectMultiScale(gray, 1.3, 20)
		for (x,y,w,h) in ducks:
			if w<= 70 and h<=70:
				cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		final_image = self.bridge.cv2_to_imgmsg(img, "bgr8")
		self.publisher.publish(final_image)


def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Velreal('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
