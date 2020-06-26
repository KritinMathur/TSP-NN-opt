import random
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

def distance(x1,y1,x2,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)
    

a= [[1,2],[2,3],[5,6],[9,2],[3,9],[7,8],[10,11],[6,1],[4,8],[2,0],[8,11]]
u=[]
v=[]
ct = 0

start = [0,2]
end = [0,0]
minlast = 1000

while(1):
    dis = 0
    random.shuffle(a)
    dis = distance(start[0],start[1],a[0][0],a[0][1])
    
    for i in range(len(a)-1):
        dis += distance(a[i][0],a[i][1],a[i+1][0],a[i+1][1])

    dis += distance(a[len(a)-1][0],a[len(a)-1][1],end[0],end[1])

    minnew = dis

    if(minnew<=minlast):
        ct = ct + 1
        minlast = minnew
        print(dis)
        u.clear()
        v.clear()

        u.append(start[0])
        v.append(start[1])
        for i in range(len(a)-1):
            u.append(a[i][0])
            v.append(a[i][1])

        u.append(end[0])
        v.append(end[1])
        
    if(perf_counter()>=10):
                break

print(u)
print(v)

plt.plot(u,v)
plt.scatter([start[0],end[0]],[start[1],end[1]],color = "red")
plt.show()
