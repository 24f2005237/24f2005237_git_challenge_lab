import numpy as np

def uniform(n, m):
  return np.random.randint(1, n+1, size = m)

no = 0   #variable for storing number of event occurence
for i in range(10000): #repetitions
  die = uniform(6,1)  #experiment
  if die == 1 or die == 3: #Event
    no = no + 1
print(no/10000) #probability estimate by Monte Carlo