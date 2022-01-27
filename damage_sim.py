#A program to help simulating damage per round in the Lancer RPG
import random
import weapon_class

def roll_accuracy(value):
	maxroll = 1
	for x in range(value):
		roll = random.randint(1,6)
		if roll == 6: return 6
		if roll > maxroll: maxroll = roll
	return maxroll
		

def calc_accuracy(num_accuracy = 0, num_difficulty = 0):
	net = num_accuracy-num_difficulty
	if net == 0: return 0
	if net>0:
		return roll_accuracy(net)
	elif net<0:
		return -1*roll_accuracy(-1*net)
		
def roll_d20():
	return random.randint(1,20);
	
#def roll_damage(hits, crits , flat_bonus):
	

var_a = calc_accuracy()
print(var_a)