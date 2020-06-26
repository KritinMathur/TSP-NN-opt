import matplotlib.pyplot as  plt
import random

def distance(x1,y1,x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def swapPositions(list, pos1, pos2): 
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def posShift(list,src,trg):
    temp = list[src]
    list.pop(src)
    list.insert(trg,temp)
    return(list)

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
inputcords = [[4,1]]

for i in range(int(input("no. of cordinates"))):
   #inputcords.append([int(input("x")),int(input("y"))])
   inputcords.append([random.randint(0,100),int(random.randint(0,100))])

inputcords = Remove(inputcords)

#start = [4,1]
#end = [5,0.5]

#nearest neighbour

for index1 in range(len(inputcords)-1):

    mindis = distance(*inputcords[index1],*inputcords[index1+1])
    swap_index = index1+1
    swap_cordinate = inputcords[index1+1]
    
    for index2 in range(index1+1,len(inputcords)):
        dis = distance(*inputcords[index1],*inputcords[index2])
        
        if(mindis > dis):
            mindis = dis
            swap_index = index2

    inputcords = swapPositions(inputcords,swap_index,index1+1)

inputcords.append([5,0.5])
nncords = inputcords.copy()

#My algo :)

p1 = -1
p2 = -1

while True:
    same = False
    min_diff = 10000
    for edge_index in range(1,len(inputcords)-1):
        for point_index in range(1,len(inputcords)-1):
            if(point_index == edge_index or point_index == edge_index -1):
                continue
            
            disgain = distance(*inputcords[edge_index-1],*inputcords[point_index])+distance(*inputcords[point_index],*inputcords[edge_index])-distance(*inputcords[edge_index-1],*inputcords[edge_index])
            disloss = distance(*inputcords[point_index-1],*inputcords[point_index]) + distance(*inputcords[point_index+1],*inputcords[point_index]) - distance(*inputcords[point_index+1],*inputcords[point_index-1])    

            diff = disgain - disloss
            
            if(disloss > disgain):
                print(edge_index,point_index,disloss-disgain)

                if(min_diff > diff):
                    min_diff = diff
                    p1 = edge_index
                    p2 = point_index
                    same = True

    print(p1,p2,same)
    if(same == True):
        inputcords = posShift(inputcords,p2,p1)
    else:
        break
            
#display cords

displayx_nn = []
displayy_nn = []

for cords in nncords:
    displayx_nn.append(cords[0])
    displayy_nn.append(cords[1])

f1 = plt.figure(1)

plt.scatter(displayx_nn,displayy_nn)
plt.plot(displayx_nn,displayy_nn,color = "yellow")

displayx = []
displayy = []

for cords in inputcords:
    displayx.append(cords[0])
    displayy.append(cords[1])

f1 = plt.figure(2)

plt.scatter(displayx,displayy)
plt.plot(displayx,displayy,color = "yellow")

plt.show()

        

        

        
