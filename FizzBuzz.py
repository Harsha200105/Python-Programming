#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 06:35:45 2018

@author: yashkumararora
"""

def fizzbuzz(r):
    for i in range(1,r+1):
        if(i%3==0 and i%5==0):
            print(str(i)+" = FizzBuzz")
        else: 
            if(i % 5 == 0):
                print(str(i)+" = Buzz")
            else: 
                if(i % 3 == 0):
                    print(str(i)+" = Fizz")
                else:
                    print(str(i))
                    
fizzbuzz(50)