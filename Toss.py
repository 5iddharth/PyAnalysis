import numpy as np 
np.random.seed(3)

outcome = []

for i in range(10):

	coin = np.random.randint(0,2)

	if coin == 0:
		outcome.append("Heads")

	else:
		outcome.append("Tails")

print(outcome)