from numpy           import linspace, reshape
from matplotlib      import pyplot
from multiprocessing import Pool
import time

xmin, xmax = -2.0 ,0.5   # x range
ymin, ymax = -1.25,1.25  # y range
nx  , ny   =  1000,1000  # resolution
maxiter    =  50         # max iterations

def mandelbrot(z): # computation for one pixel
  c = z
  for n in range(maxiter):
    if abs(z)>2: return n  # divergence test
    z = z*z + c
  return maxiter

def compute_all_x(y):
  Z = [complex(x,y) for x in X]
  return list(map(mandelbrot,Z))

X = linspace(xmin,xmax,nx) # lists of x and y
Y = linspace(ymin,ymax,ny) # pixel co-ordinates

# main loops
if __name__=='__main__':

  # record start time
  start = time.time()

  p = Pool()
  N = p.map(compute_all_x,Y)

  N = reshape(N, (nx,ny)) # change to rectangular array

  # record end time
  end = time.time()
  # print the difference between start
  # and end time in milli. secs
  print("The time of execution of above program is :",
        (end-start) * 10**3, "ms")

  pyplot.imshow(N) # plot the image
  pyplot.show()
