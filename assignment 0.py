#!/usr/bin/env python
# coding: utf-8

# In[1]:


#assignment 0

# 1. Design and implement a class representing a rectangle and operations like area, perimeter,
# change dimensions, report dimensions, on it. Write code to test your classes


class rectangle():
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self,length,breadth):
        Area = length *  breadth
        print("Area is ",Area)
        
    def perimeter(self,length,breadth):
        Perimeter = 2*(length+breadth)
        print ("perimeter is : ",Perimeter)
        
    def report (self):
        return self.length,self.breadth
    
    def changedimension (self,newlen,newbre):
        self.length =newlen
        self.breadth=newbre
        print("New length and breadth are :",self.length ,"&",self.breadth)
        
        
        
    
        
        
rect =rectangle(6,10)
rect.area(6,10)

Perimeter = rectangle(6,10)
Perimeter.perimeter(6,10)


rect.changedimension(15,20)
rect.area(15,20)
rect.report()


# In[ ]:




