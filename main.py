
from __future__ import print_function
import random
import numpy as np
import sys,time


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
		self.curr_floor = self.curr_floor - n
		if self.curr_floor < 0:
			self.curr_floor = 0

	def take_action(self,action):
		self.action = action

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
	print("********** TIMESTEP NUBER "+str(time_step)+" **********")
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
		#floor_no = floor_no - 1
		print("")
		print('||', end = '')
		for i in range(0,no_elevators):
			if floor_no == pos[i]:
				if actions[i] == 1:
					print('xx  xx', end = '')
				else:
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
		floor_no = floor_no - 1
	print('||', end = '')
	for i in range(0,no_elevators):
		print('------', end = '')
		print('||', end = '')
	print("\n")
	print("People waiting: "+str(len(people_waiting)))
	print("People in Lift: "+str(no_people_in_lift()))
	print("\n------------------------------------------------------------\n")



def update_wait_time():
	for f in floors:
		if(f.up):
			f.upTime += 1
		if f.down:
			f.downTime += 1
	for p in people_waiting:
		p.wait_time+=1
	for e in range(0,no_elevators):
		for p in people_in_lift[e]:
			p.wait_time+=1 


def get_reward():
	total = 0
	for p in people_waiting:
		total += p.wait_time
	for e in range(0,no_elevators):
		for p in people_in_lift[e]:
			total += p.wait_time
	return -total

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
			if actions[e] == 1 and p.destination == elevators[e].curr_floor:
				## you have reached your destination
				elevators[e].buttons[elevators[e].curr_floor] = 0
				people_in_lift[e].remove(p)
				delivered.append(0)


	for i in range(0,no_elevators):
		if actions[i] == 1:
			f = elevators[i].curr_floor
			for p in people_waiting:
				if p.floor == f:
					people_in_lift[i].append(p)
					elevators[i].buttons[p.destination] = 1
					people_waiting.remove(p)
					floors[f].up = 0
					floors[f].upTime = 0
					floors[f].down = 0
					floors[f].downTime = 0



def do_action():
	for i in range(0,no_elevators):
		if actions[i] == 1:
			#open doors
			continue
		elif actions[i] == 2:
			elevators[i].move_up(1)
		elif actions[i] == 3:
			elevators[i].move_up(2)
		elif actions[i] == 4:
			elevators[i].move_up(3)
		elif actions[i] == 5:
			elevators[i].move_up(4)
		elif actions[i] == 6:
			elevators[i].move_up(5)
		elif actions[i] == 7:
			elevators[i].move_up(6)
		elif actions[i] == 8:
			elevators[i].move_up(7)
		elif actions[i] == 9:
			elevators[i].move_down(1)
		elif actions[i] == 10:
			elevators[i].move_down(2)
		elif actions[i] == 11:
			elevators[i].move_down(3)
		elif actions[i] == 12:
			elevators[i].move_down(4)
		elif actions[i] == 13:
			elevators[i].move_down(5)
		elif actions[i] == 14:
			elevators[i].move_down(6)
		elif actions[i] == 15:
			elevators[i].move_down(7)

def no_people_in_lift():
	z = 0
	for i in range(0,no_elevators):
		z += len(people_in_lift[i])
	return z


def prepare_tensor():
	t = []
	for e in elevators:
		t.append(e.curr_floor)
		t += e.buttons
	for f in floors:
		t.append(f.up)
		t.append(f.down)
	return t


def one_timestamp():
	do_action()
	post_action()
	print_timestamp()


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

time_step = 0
actions = []
no_floors = 7
no_elevators = 2
building = Building(no_floors,no_elevators)
elevators = []
floors = []
people_in_lift = []
people_waiting = []

#only because global varibles are fked
delivered = []

for i in range(0,no_elevators):
	elevators.append(Elevator(no_floors))
	people_in_lift.append([])
	actions.append(0)
for i in range(0,no_floors+1):
	floors.append(Floor(i))

print_timestamp()

#######################################################

for z in range(0,500):
	if z%3==0:
		r = random.randint(0,7)
		r2 = random.randint(0,7)
		new_person(r,r2)
	a1 = random.randint(0,15)
	a2 = random.randint(0,15)
	actions = [a1,a2]
	do_action()
	post_action()
	update_wait_time()
	print_timestamp()
	print("people delivered: "+str(len(delivered)))
	print(prepare_tensor())
	reward = get_reward()
	print("*****************")
	print("REWARD: "+str(reward))
	print("*****************")
	time_step+=1
	time.sleep(.5)

'''
new_person(5,0)
print_timestamp()
reward = get_reward()
print("*****************")
print("REWARD: "+str(reward))
print("*****************")
time.sleep(1)
actions = [0,1]
do_action()
post_action()
update_wait_time()
print_timestamp()
reward = get_reward()
print("*****************")
print("REWARD: "+str(reward))
print("*****************")
time.sleep(1)
actions = [0,6]
do_action()
post_action()
update_wait_time()
print_timestamp()
reward = get_reward()
print("*****************")
print("REWARD: "+str(reward))
print("*****************")
time.sleep(1)
actions = [0,1]
do_action()
post_action()
update_wait_time()
print_timestamp()
reward = get_reward()
print("*****************")
print("REWARD: "+str(reward))
print("*****************")
'''
