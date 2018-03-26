from __future__ import print_function

no_elevators = 2
no_floors = 7
floor_no = no_floors

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
		print('      ', end = '')
		print('||', end = '')
	print("")
print('||', end = '')
for i in range(0,no_elevators):
	print('------', end = '')
	print('||', end = '')
print("")

