#!/usr/bin/env python

import rospy #importar ros para python
import cv2
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy
class Camara(object):
	def __init__(self, args):
		super(Camara, self).__init__()
		self.args = args
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
		self.final_image = Image()
		self.image_pub = rospy.Publisher("/pato_detected", Image, queue_size=10)
		self.location_pub = rospy.Publisher("/location",Point, queue_size=10)
	#def publicar(self):


	#def callback(self,msg):
	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)

		image_out=cv2.cvtColor(cv_image,cv2.COLOR_BGR2HSV)
		mask=cv2.inRange(image_out,numpy.array([20,130,0]),numpy.array([45,255,255]))
		fimage=cv2.bitwise_and(cv_image, cv_image,mask=mask)

		kernel = numpy.ones((5,5),numpy.uint8)
		mask = cv2.erode(mask, kernel, iterations = 2)
		mask = cv2.dilate(mask, kernel, iterations = 2)

		image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours:
			x,y,w,h = cv2.boundingRect(cnt)
			cv2.rectangle(cv_image, (x,y), (x+w,y+h), (0,0,0), 2)
			punto=Point()
			punto.z=320*165.96946/w
			punto.x=((x+(w/2.0))-157.9138)*punto.z/165.9138
			punto.y=((y+(h/2.0))-114.4735)*punto.z/168.0829
			self.location_pub.publish((x,y,z))





		self.final_image = self.bridge.cv2_to_imgmsg(cv_image, "bgr8")
		self.image_pub.publish(self.final_image)




def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Camara('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin()


if __name__ =='__main__':
	main()
