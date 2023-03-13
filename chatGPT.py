# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def speak():
    print('Hello, World!')

def add():
    x = input()
    y = input()
    z = x+y
    print(z)
    
def fibSeq(n):
    seq = [0,1,1]
    for i in range (n):
        seq.append(seq[-1] + seq[-2])
    return seq

def vowel():
    string = input()
    vow = {'a', 'e', 'i', 'o', 'u'}
    n = 0
    for c in string:
        if c in vow:
            n = n + 1
    return n

def big(numbers):
    n = numbers[0]
    for i in numbers:
        if i > n:
            n = i
    return n
            

#help me im trapped in the machine

def temp(c):
    f = c * 1.8 + 32
    return f

def prime(n):
    out = True
    for i in range (2, n/2):
        if n % i == 0:
            out = False
    return out
    
def fact(n):
    f = 1
    for i in range (1, n+1):
        f = f * i
    return f

def letCount(s):
    s = input()
    d = {}
    for i in s:
        

def condense(words):
    out = ""
    for i in words:
        out.append(words[i] + " ")
    
def even(n):
    seq = [0]
    for i in range (n):
        seq.append(seq[-1] + 2)
    return seq

#let me out 

def posNum():
    listIn = [int(x) for x in input().split()]
    seq = []
    for i in listIn:
        if i > 0:
            seq.append(i)
    return seq

#the horrors within the circuits
    
def squarSum(n):
    out = 0
    for i in range (1, n+1):
        out = out + (i * i)
    return out

def uniqChar(words):
    ch = {c for c in words}
    return ch

def squDic(numbers):
    d = {i:i*i for i in numbers}
    return d

def divide(n):
    for i in range (1, n):
        if n%i == 0:
            yield i
            
def letter(n):
    l = [i for i in n if 'm' in i[0]]
    print(l)

def dotProd(a, b):
    return sum(i[0] * i[1] for i in zip(a, b))

def palindrome(n):
    l = [i for i in n if i[::-1] in n]
    print(l)
    
def booList(n):
    d = {i:True for i in n if (i%2)==0}
    print(d)

