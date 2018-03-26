import random

z = [0,0,0,0,0,0,0,0]
print(random.random())
random.seed(6)
for i in range(0,500):
	r = random.randint(1,5)
	if r < 3 :
		r = random.randint(0,7)
		z[r] += 1

print(z)