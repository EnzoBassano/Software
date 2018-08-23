#!/usr/bin/env python

import rospy #importar ros para python
from sensor_msgs.msg import Image
from duckietown_msgs.msg import Twist2DStamped
from sensor_msgs.msg import Joy
from cv_bridge import CvBridge
import cv2 as cv
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist


class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		self.subscriber = rospy.Subscriber("/duckiebot/joy", Joy,self.callback)
		self.publisher = rospy.Publisher('/duckiebot/wheels_driver_node/car_cmd', Twist2DStamped, queue_size=1)
		self.twist= Twist2DStamped()
		self.subscriber = rospy.Subscriber("/duckiebot/camera_node/image/rect",Image,self.callback_image)
		self.bridge = CvBridge()
		self.image = Image()



	def callback(self,msg):
		self.twist.v=msg.axes[1]
		self.twist.omega=10*msg.axes[3]
		print self.twist
		self.publisher.publish(self.twist)
		if msg.buttons[5]==1:
			self.twist.v=0
			self.twist.omega=0
			self.publisher.publish(self.twist)

		if msg.buttons[0]==1:
			img = self.bridge.imgmsg_to_cv2(self.image,"bgr8")
			filename = str(rospy.get_time()) + ".jpg"
			cv.imwrite("/home/duckiebot/nopatos/"+filename,img)

	def callback_image(self,msg):
		self.image=msg







	#def publicar(self):

	#def callback(self,msg):


def main():
	rospy.init_node('control') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
