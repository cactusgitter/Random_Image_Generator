# This is a program that will draw all possible black and white
# images that are within a 100 x 100 bounding box.

import kivy
kivy.require('1.11.1') 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import Instruction
from kivy.lang import Builder
from kivy.clock import Clock

import random

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

class RootBoxLayout(BoxLayout):	
	def __init__(self, **kwargs):
		super(RootBoxLayout, self).__init__(**kwargs)
		self.event = None
			
	def play(self):
		if self.event == None:
			self.event = Clock.schedule_interval(self.create_random_image, 0.1)
		else:
			self.event.cancel()
			self.event = None

		
	def create_random_image(self, *args):
		self.ids.print_box.canvas.clear()
		with self.ids.print_box.canvas:
			i = 0
			j = 0
			pixel_width = self.ids.print_box.width * 0.1
			pixel_height = self.ids.print_box.height * 0.1 
			pixel_x = self.ids.print_box.x
			pixel_y = self.ids.print_box.y
			while i < 10:
				j = 0
				while j < 10:
					new_pos = (pixel_x + (j * pixel_width), pixel_y + (i * pixel_height))
				
					if random.randint(0,1) == 1:				
						Color(rgba=(1,1,1,1)) #White
						Rectangle(pos = new_pos,
								  size = (pixel_width, pixel_height))
					else:
						Color(rgba=(0,0,0,1)) #Black
						Rectangle(pos = new_pos,
								  size = (pixel_width, pixel_height))
					j += 1
				i += 1
				
		

class Main(App):
	def build(self):
		Builder.load_file("Random_Image_Generator.kv")
		root = RootBoxLayout()
		return root

if __name__ == '__main__':
	Main().run()
