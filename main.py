
from __future__ import print_function
import random
import numpy as np


class Elevator:
	def __init__(self,floors):
		self.buttons = []
		self.floors = floors
		for f in range(0,floors+1):
			self.buttons.append(0)
		self.curr_floor = 0

	def move_up(self,n):
		self.curr_floor = self.curr_floor + n
		if self.curr_floor > self.floors:
			self.curr_floor = self.floors

	def move_down(self,n):
		self.curr_floor = curr_floor - n
		if self.curr_floor < 0:
			curr_floor = 0

class Floor:
	def __init__(self,floor_no):
		self.up = 0
		self.upTime = 0
		self.down = 0
		self.downTime = 0
		self.floor_no = floor_no

class Building:
	def __init__(self,floors,elevators):
		self.floors = floors
		self.elevators = elevators


class Person:
	def __init__(self,floor,destination):
		self.destination = destination
		self.wait_time = 0
		self.floor = floor

def curr_el_position():
	f = []
	for e in elevators:
		f.append(e.curr_floor)
	return f


def print_timestamp():
	floor_no = no_floors
	pos = curr_el_position()
	for z in range(0,no_floors+1):
		print('||', end = '')
		for i in range(0,no_elevators):
			print('------', end = '')
			print('||', end = '')
		print("")
		print('||', end = '')
		for i in range(0,no_elevators):
			print('      ', end = '')
			print('||', end = '')
		print('Floor: '+str(floor_no), end = '')
		floor_no = floor_no - 1
		print("")
		print('||', end = '')
		for i in range(0,no_elevators):
			if floor_no + 1 == pos[i]:
				print('  xx  ', end = '')
			else:
				print('      ', end = '')
			print('||', end = '')
		if floors[floor_no].up:
			print('Up Button Pressed!', end = '')
			print('        ', end = '')
			print('Waiting time: '+str(floors[floor_no].upTime), end = '')
		print("")
		print('||', end = '')
		for i in range(0,no_elevators):
			print('      ', end = '')
			print('||', end = '')
		if floors[floor_no].down:
			print('Down Button Pressed!', end = '')
			print('        ', end = '')
			print('Waiting time: '+str(floors[floor_no].downTime), end = '')
		print("")
	print('||', end = '')
	for i in range(0,no_elevators):
		print('------', end = '')
		print('||', end = '')
	print("")
	print("\n\n------------------------------------------------------------\n")


def update_wait_time():
	for f in floors:
		if(f.up):
			f.upTime += 1
		if f.down:
			f.downTime += 1


def get_reward():
	total = len(people_waiting)
	for i in range(0,no_elevators+1):
		total += len(people_in_lift[i])
	return total

def action():
	return random.randint(0,15)

def new_person(destination,floor):
	if destination > floor:
		floors[floor].up = 1
		people_waiting.append(Person(floor,destination))
	elif destination < floor:
		floors[floor].down = 1
		people_waiting.append(Person(floor,destination))


def post_action():
	for e in range(0,no_elevators):
		for p in people_in_lift[e]:
			print("destination: " + str(p.destination))
			print(e)
			print("")



def prepare_tensor():
	t = []
	for e in elevators:
		t.append(e.curr_floor)
		t += e.buttons
	for f in floors:
		t.append(f.up)
		t.append(f.down)
	print(t)
	return t


############################
       ## STATES ###
###########################

# elevator 1 position
# elevator 1 buttons (8)
# elevator 2 position
# elevator 2 buttons (8)
# floor up btton pressed? (8)
# floor down button pressed? (8)




############################
       ## ACTIONS ###
###########################

# 0 - nothing
# 1 - open doors
# 2 - move up 1
# 3 - move up 2
# 4 - move up 3
# 5 - move up 4
# 6 - move up 5
# 7 - move up 6
# 8 - move up 7
# 9 - move down 1
# 10 - move down 2
# 11 - move down 3
# 12 - move down 4
# 13 - move down 5
# 14 - move down 6
# 15 - move down 7


#####################################################
###################   SET UP  #######################

no_floors = 7
no_elevators = 2
building = Building(no_floors,no_elevators)
elevators = []
floors = []
people_in_lift = []
people_waiting = []

for i in range(0,no_elevators):
	elevators.append(Elevator(no_floors))
	people_in_lift.append([])
for i in range(0,no_floors):
	floors.append(Floor(i))

print_timestamp()

#######################################################


for i in range(0,10):
	a = random.randint(0,7)
	b = random.randint(0,7)
	people_in_lift[0].append(Person(a,b))

for i in range(0,6):
	a = random.randint(0,7)
	b = random.randint(0,7)
	people_in_lift[1].append(Person(a,b))


post_action()