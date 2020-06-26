import matplotlib.pyplot as  plt
from itertools import permutations
import random

def distance(x1,y1,x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def td(cords):
    sum = distance(4,1,*cords[0])
    for xandy in range(len(cords)-1):
        sum = sum + distance(*cords[xandy],*cords[xandy+1])
    sum = sum + distance(*cords[len(cords)-1],5,0.5)
    return sum

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

raw = []

for i in range(int(input("no. of cordinates"))):
   #raw.append([int(input("x")),int(input("y"))])
   raw.append([random.randint(0,100),int(random.randint(0,100))])

raw = Remove(raw)

perm = list(permutations(raw))
final = []


md = 100000
for comb in perm:
    if(md > td(comb)):
        md = td(comb)
        final = comb

print(final)

final2 = list(final)
final2.append([5,0.5])
final2.insert(0,[4,1])

displayx = []
displayy = []

for cords in final2:
    displayx.append(cords[0])
    displayy.append(cords[1])

f1 = plt.figure(1)

plt.scatter(displayx,displayy)
plt.plot(displayx,displayy,color = "yellow")

plt.show()






