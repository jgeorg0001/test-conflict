#! /ust/bin/python3
import os,sys,re
#import subprocess

def f2(y):
    y = y * 2
    return y

def f1(x):
    y = f2(x)
    return y

if __name__ == "__main__":
   x = 10
   k = f1(x)
   print(k)
