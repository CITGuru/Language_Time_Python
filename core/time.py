import os
import english.english,yoruba.yoruba,hausa.hausa,igbo.igbo

class Time:
	def __init__(self, lang="english"):
		self.lang = lang
		print english.english


l = Time("yoruba")

