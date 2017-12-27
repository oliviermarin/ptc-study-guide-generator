# -*- coding: utf-8 -*-

class Color:
	def __init__(self,r_init, g_init, b_init):
		self.r = r_init
		self.g = g_init
		self.b = b_init

	def __repr__(self):
		return "".join(["Color(", str(self.r), ",", str(self.g), ",", str(self.b), ")"])
