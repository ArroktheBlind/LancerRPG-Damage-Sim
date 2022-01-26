#Provides weapon class definitoin for weapons
#and functions for parsing lancer weapon .json objects

class Weapon:
	#def __init__(self, weapon_name):
    #self.data = []
	'''Damage Parameters'''
	num_dice = 0
	die_size = 0
	flat_damage = 0
	damage_type = 0
	self heat = 0
	'''Weapon Tags'''
	#Only tags directly relevant to damage and hit calculations have been included. 
	#Treat as booleans except where noted
	Accurate = 0
	AP = 0
	Inaccurate = 0
	Loading = 0
	Reload = 0 #Helper variable for loading in sim mode. Technically unncessesary because of member creation at runtime
	Overkill = 0
	Reliable = 0 #Specify value of reliable
	Seeking = 0


