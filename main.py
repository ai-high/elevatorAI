
from __future__ import print_function

import numpy as np


class Elevator:
	def __init__(self,floors):
		self.buttons = []
		self.floors = floors
		for f in range(0,floors):
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
	def __init__(self,destination):
		self.destination = destination
		self.wait_time = 0



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
			if floor_no == pos[i]:
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


def prepare_tensor():
	t = []
	for e in elevators:
		t.append(e.curr_floor)
		t += e.buttons
	for f in floors:
		t.append(f.up)
		t.append(f.down)
	print(t)

no_floors = 7
no_elevators = 2

building = Building(no_floors,no_elevators)
elevators = []
floors = []
for i in range(0,no_elevators):
	elevators.append(Elevator(no_floors))
for i in range(0,no_floors):
	floors.append(Floor(i))
elevators[0].move_up(1)
elevators[1].move_up(3)
print(curr_el_position())
print_timestamp()
elevators[0].move_up(1)
elevators[1].move_up(3)
floors[3].up = 1
floors[1].down = 1
print_timestamp()
prepare_tensor()
