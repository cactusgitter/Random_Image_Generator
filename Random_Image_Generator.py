# This is a program that will draw all possible black and white
# images that are within a 100 x 100 bounding box.

import kivy
kivy.require('1.11.1') 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
#from kivy.graphics.instructions import Instruction
from kivy.lang import Builder
from kivy.clock import Clock

import random

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

class RootBoxLayout(BoxLayout):	
	def __init__(self, **kwargs):
		super(RootBoxLayout, self).__init__(**kwargs)
		self.grid_size = 50
		self.end_num = 2 ** (self.grid_size * self.grid_size)
			
	def play(self):
		self.ids.print_box.canvas.clear()
		
		"""Randomize the matrix"""
		new_rando = random.randint(0, self.end_num) # Create the random decimal integer
		new_rando = bin(new_rando) # Convert it to binary
		new_rando = list(new_rando) # Convert the binary to a list
		new_rando.pop(0)
		new_rando.pop(0)
		
		self.matrix = [[0 for i in range(self.grid_size)] for j in range(self.grid_size)]

		
		i = 0
		j = 0
		while i < self.grid_size:
			j = 0 
			while j < self.grid_size:
				if new_rando:  # If new_rando is not empty
					self.matrix[i][j] = int(new_rando.pop(0))
				else:
					i = self.grid_size # Break out of the loop
					j = self.grid_size # Break out of the loop
				j += 1
			i += 1
		
		self.draw_next_image()
				
	def draw_next_image(self, *args):
		
		with self.ids.print_box.canvas:
			"""Pixel here refers to a rectangle that represents pixels"""
			pixel_width = self.ids.print_box.width * (1/self.grid_size)    # how wide to draw the pixel
			pixel_height = self.ids.print_box.height * (1/self.grid_size)  # how tall to draw the pixel
			pixel_x = self.ids.print_box.x	# x position of the pixel
			pixel_y = self.ids.print_box.y	# y position of the pixel
			
			i = 0
			j = 0
			
			while i < self.grid_size:
				j = 0
				while j < self.grid_size:
					new_pos = (pixel_x + (j * pixel_width), pixel_y + (i * pixel_height))
				
					if self.matrix[i][j] == 0:	# If the matrix is 0
						Color(rgba=(0,0,0,1)) # Draw a black rectangle						
					else: # If the matrix is 1
						Color(rgba=(1,1,1,1)) # Draw a white rectangle
						
					Rectangle(pos = new_pos,
							  size = (pixel_width, pixel_height))
					j += 1
				i += 1
			
			# Draw the rectangle
			Rectangle(pos = new_pos,
					  size = (pixel_width, pixel_height))

class Main(App):
	def build(self):
		Builder.load_file("Random_Image_Generator.kv")
		root = RootBoxLayout()
		return root

if __name__ == '__main__':
	Main().run()
