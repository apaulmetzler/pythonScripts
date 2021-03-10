#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:28:06 2020
@author: paulmetzler

this program was created to find a third of a sample that has been collected
on grided filter paper when the circle is of variable size
"""


## Circle segment calculator

def circleSegment():
    print("\nthis program calculates the distance between the circle center and\n\
the line that creates a circle segment with area about equal to one third\n")
    import math
    rad = float(input("what is the radius of the filterpaper (mm)?"))
    area = (rad**2)*math.pi
    third = area/3
    grid = float(input('what is the size of your filter paper square in mm (usually 3.1)?'))
    print("\nradius =",rad,"area =",area,"third =",third)
    a = grid/2
    g = 0
    segAreaList = []
    maxLength = math.ceil(2*rad/grid)
    #print("max length =",maxLength)
    for x in range(0,maxLength):
        sectDeg = 2*(math.acos(a/rad))*(180/math.pi)
        #print("sector degrees =",sectDeg)
        o = math.sqrt((rad**2)-(a**2))
        #print("opposite =",o)
        isosTriangleArea = a*o
        #print("triangle area =",isosTriangleArea)
        sectArea = (sectDeg/360)*area
        #print("sectarea =",sectArea)
        segArea = sectArea-isosTriangleArea
        print("segment area =",segArea)
        g = g+0.5
        print(g)
        segAreaList.append(segArea)
        if segArea < third:
            #print("\nthe line segment is between",g-0.5,"and",g,"squares away from the filter paper center")
            print("\nat {} gridlines, the segment area is {:.2f}\n\
one third of the area is equal to {:.2f}\n\
at {} gridlines, the segment area is {:.2f}".format(g-.5,segAreaList[-2],third,g,segAreaList[-1]))
            break
        a = a+(grid/2)
