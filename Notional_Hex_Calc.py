# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:43:14 2021

@author: WN
"""

def hexadd(a,b):
    print("The sum of the two hexadecimal inputs "+ str(hex(a)) +" and " + str(hex(b)) +" is:")
    return(hex(a + b))
    
def hexsub(a,b):
    print("The difference of the two hexadecimal inputs "+ str(hex(a)) +" and " + str(hex(b)) +" is:")
    return(hex(a - b))

def hexmult(a,b):
    print("The product of the two hexadecimal inputs "+ str(hex(a)) +" and " + str(hex(b)) +" is:")
    return(hex(a * b))
def hexdiv(a,b):
    print("The quotient of the two hexadecimal inputs "+ str(hex(a)) +" and " + str(hex(b)) +" is:")
    return(hex(a / b))    
    
def hexpow(a,b):
    print( str(hex(a)) + " raised to " + str(hex(b)) +" is:")
    return(hex(a ** b))     