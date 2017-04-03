# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:15:04 2015
 (301) 265-3336 
@author: gilbe244
"""

class Vector(object):
    def __init__(self, x_coord=0,y_coord=0):
       self.__x_coord=0
       self.__y_coord=0
       
       if x_coord !=0:
           self.__x_coord = x_coord
       if x_coord!=0:
           self.__y_coord= y_coord
       
       
       
    def __repr__(self):
        
        return "({:.2f},{:.2f})".format(self.__x_coord, self.__x_coord)
        
    def __str__(self):
        
        return self.__repr__()
        
    def magnitude(self):
        mag=((self.__x_coord)**2+(self.__y_coord)**2)**(1/2)
        return round(mag,2)
        
        
    def __eq__(self,vector):
        if self.__x_coord==vector.__x_coord:
            if self.__y_coord==vector.__y_coord:
                return True
            else:
                return False
        else:
            return False

    
    def __add__(self,vector):
        x= self.__x_coord+vector.__x_coord
        y= self.__y_coord+vector.__y_coord
        
        return Vector(x, y )
    def __sub__(self,vector):
        x= self.__x_coord-vector.__x_coord
        y= self.__y_coord-vector.__y_coord
        
        return Vector(x,y)
    def __mul__(self,vector):
        if type(vector) == type(self):
            a = (self.__x_coord*vector.__x_coord)+(self.__y_coord*vector.__y_coord)
            return a
        else:
            x1=vector*self.__x_coord
            y1=vector*self.__y_coord
            return Vector(x1,y1)
            
        
        
    def __rmul__(self,vector):
        x1=vector*self.__x_coord
        y1=vector*self.__y_coord
        return Vector(x1,y1)
        
A=Vector(5,2)
B = Vector(1,2)

repr(B)
C = B.magnitude()
print("B.magnitude() :", C)

D = A == B
print(D)

E = A +B
print(E)

F = A -B
print(F)

G = A*B
print(G)

H = 7*B
print(H)

I = B*8
print(I)