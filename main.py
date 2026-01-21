import numpy as np

def uniform(n, m):
  return np.random.randint(1, n+1, size = m)

no_heads = 0   #variable for storing number of heads
for i in range(1000): #repeat 1000 times
  if uniform(2, 1) == 1: #check if coin toss is heads
    no_heads = no_heads + 1
print(no_heads/1000) #probability estimate by Monte Carlo