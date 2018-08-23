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
		self.publisher = rospy.Publisher("/duckiebot/camera_node/cara", Image, queue_size=10)
		self.bridge = CvBridge()
		self.img = Image()

	def callback_image(self,msg):
		self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
		face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		final_image = self.bridge.cv2_to_imgmsg(self.img, "bgr8")
		self.publisher.publish(final_image)

def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Velreal('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()
