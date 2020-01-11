# Three points, P1, P2 and P3, are randomly selected within a unit square.
# Consider the three rectangles with sides parallel to the sides of the
# unit square and a diagonal that is one of the three line segments.
# Find the area of the second largest rectangle formed.
import numpy as np
import random

def pick_points():
    points_list=[]
    for points in range(0,3):
        x = random.random()
        y = random.random()
        point=(x,y)
        points_list.append(point)
    return points_list

exp_area_list = []
for i in range(0,100000000):

    points_list = pick_points()

    x1 = points_list[0][0]
    y1 = points_list[0][1]
    x2 = points_list[1][0]
    y2 = points_list[1][1]
    x3 = points_list[2][0]
    y3 = points_list[2][1]

    R1=np.abs(x1-x3)*np.abs(y1-y3)
    R2=np.abs(x1-x2)*np.abs(y1-y2)
    R3=np.abs(x2-x3)*np.abs(y3-y2)
    area_list = [R1,R2,R3]
    area_list.pop()
    exp_area_list.append(max(area_list))

print(round(np.mean(exp_area_list), 10))
