import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

points = 2000000 # initiating a variable 'points' for quantifying the number of random points (co-ordinates) to be generated.


rand = 2*np.random.rand(2*points) -1  # the random function from numpy library generates float points in range 0.0 to 1.0
                                      # we are scaling the points by 2 and shifting them by -1, so the range becomes-> -1.0 to 1.0 [to cover the entire area of the square]
                                      # the points are doubled, since each x,y co-ordinate requires two values

randpoints = rand.reshape( points,2 ) # creating a list of pairs from "rand", each of these pairs are distinct co-ordinates on x-y plane

normpoints = (randpoints[:,0]**2 + randpoints[:,1]**2)**0.5  # from the list of pairs from "randpoints" we are taking each (x,y) co-ordinate
                                                             # and calculating its distance from (0,0), the centre of the circle

pointsOut = randpoints[normpoints > 1] # points lying outside the circle [not necessary for this experiment]
pointsIn = randpoints[normpoints <= 1] # points lying inside or on the boundary of the circle

piapprox = 4 * len(pointsIn)/points  # applying the Monte Carlo principle, to calculate pi
print("The approximate value of pi is", piapprox)



print("Error:", (piapprox - np.pi))  # error in approximation