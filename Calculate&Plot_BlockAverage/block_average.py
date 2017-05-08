import numpy as np
import matplotlib.pyplot as plt


def blockavg(data,n):
# block-average data in blocks of length n
# data: input [x,y] (x,y: 1D-arrays of same length)
# n: number of points in each block
# returns array of block averages of both x and y
    ntot=len(data[0])
    nnew=ntot/n
    x=np.zeros(nnew,dtype=float)
    y=np.zeros(nnew,dtype=float)
    for i in range(nnew):
        x[i]=np.sum(data[0][i*n:(i+1)*n])/float(n)
        y[i]=np.sum(data[1][i*n:(i+1)*n])/float(n)
    return [x,y]#[lex]

#here is the main part wich you need to "tweak"

x=[]
y=[]

# Open f i l e
f = open ( 'PE.txt' , 'r' )
# Read and ignore header lines if needed
#header1 = f.readline ( )
# Loop over lines and extract variables of interest
for line in f :
    line    = line.strip()
    columns = line.split()
    data0   = float(columns[0])
    data1   = float(columns[1])
    x=np.append(x,data0)
    y=np.append(y,data1)

  
data=[x,y] 

[x1,y1]=blockavg(data,100)

f1 = plt.figure(1)
plt.plot(x,y ,'--', markersize =1.2 )
f1.suptitle('Original data')
plt.xlabel( 'data0' )
plt.ylabel( 'data1')
plt.grid()
plt.savefig('original.png', bbox_inches='tight')

f2 = plt.figure(2)
plt.plot(x1,y1 ,'r-', markersize =1.2 )
f2.suptitle('Block-averaged data')
plt.xlabel( 'data0' )
plt.ylabel( 'data1')
plt.grid()
plt.savefig('block_average.png', bbox_inches='tight')
