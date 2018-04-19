#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped

class Controller(object):
	def __init__(self, args):
		super(Controller, self).__init__()
		self.args = args
		self.subscriber = rospy.Subscriber("/duckiebot/joy", Joy, self.callback)
		self.publisher = rospy.Publishe("/duckiebot/wheels_driver_node/car_cmd", Twist, queue_size=10)

	#def publicar(self):
	
			
	#def callback(self,msg):
	def callback(self,mag):
		x = msg.axes[1]
		z = msg.axes[3] 
		f = msg.button[5]

		self.twist.v = x
		self.twist.omega = z
		if f == 1:
			self.twist.v = 0

		self.publisher.publish(self.twist)



def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	#rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
