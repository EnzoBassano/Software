import rospy #importar ros para python
import cv2
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs import Point
import numpy
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped
import camara.py
import controller.py

class Velreal(object):
	def __init__(self,args):
		self.suscriber = rospy.Subscriber("/comando",Twist,self.callback_comando)
		self.suscriber = rospy.Subscriber("/location",Point,self.callback_location)
		self.publisher = rospy.Publisher("/duckiebot/wheels_driver_node/car_cmd", Twist, queue_size=10)
		self.twist = Twist()
	
	def callback_comando(self,msg):
		self.twist = msg

	def callback_location(self,msg):
		self.point= msg
		if self.point.x==0 and self.point.y==0 and self.point.z==0:
			self.publisher.publish(self.twist)
		else:
			correcion=Twist()
			correcion.v=0
			correcion.omega=0
			self.publisher.publish(correcion)

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Velreal('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
