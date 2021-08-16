from ursina import *
import os

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = os.path.join('assets',"sky.png"),
			scale = 150,
			double_sided = True
        )