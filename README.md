# TSP-NN-opt
Optimization of the Nearest neighbor greedy algorithm for Traveling salesman problem.

## What is the Travelling Salesman Problem

The traveling salesman problem (also called the traveling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in theoretical computer science and operations research.

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/GLPK_solution_of_a_travelling_salesman_problem.svg/800px-GLPK_solution_of_a_travelling_salesman_problem.svg.png)

## What is Nearest Neighbour

The nearest neighbor algorithm was one of the first algorithms used to solve the traveling salesman problem approximately. In that problem, the salesman starts at a random city and repeatedly visits the nearest city until all have been visited. The algorithm quickly yields a short tour, but usually not the optimal one.

## Requirments

For path visualization matplotlib is used.
use `pip install matplotlib` to install matplot lib

## Contents
### native.py
It uses the native approach to find the best path between n random points by calculating the total distance for every possible sequence of points. the figure in the scatter plot shows the best path which has been calculated. 

:warning: do not use native.py for more than 10 points

### opt.py
It uses an optimized Nearest Neighbour algorithm to find the optimal path between n random points. The figure 1 scatter plot shows the path calculated by the nearest neighbor algorithm and figure 2 shows the optimizations made to the previous path.

example for figure 1
https://drive.google.com/file/d/1sNbR8SqojGa1KxhIpG-Wqi1O05Mu5TW4/view?usp=sharing

example for figure 2
https://drive.google.com/file/d/1DBTgeKOJKsjiVgwggQE5OIJd4l8t5add/view?usp=sharing
