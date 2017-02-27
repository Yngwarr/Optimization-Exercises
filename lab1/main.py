#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from math import sqrt, log, ceil, floor
from sys import argv, exit
from copy import deepcopy

GR = 1.6180339887499

def dichotomy(f, a, b, eps, delta):
    lx = None
    rx = None
    _a = deepcopy(a)
    _b = deepcopy(b)
    n = log((_b - _a)/eps) / log(2)
    print('n = ' + str(n))
    for i in range(0, int(ceil(n))):
        lx = (_a + _b - delta) / 2
        rx = (_a + _b + delta) / 2
        fl = f(lx)
        fr = f(rx)
        print('_a, _b = ' + str((_a,_b)))
        print('lx, rx = ' + str((lx,rx)))
        print('f: ' + str((fl,fr)))
        print
        if fl < fr: _b = rx
        else: _a = lx
    return lx if f(lx) < f(rx) else rx

def golden_ratio(f, a, b, eps):
    global GR
    lx = None
    rx = None
    _a = deepcopy(a)
    _b = deepcopy(b)
    while abs(_b - _a) >= eps:
        lx = _b - (_b - _a)/GR
        rx = _a + (_b - _a)/GR
        fl = f(lx)
        fr = f(rx)
        print('_a, _b = ' + str((_a,_b)))
        print('lx, rx = ' + str((lx,rx)))
        print('f: ' + str((fl,fr)))
        print
        if fl < fr: _b = rx
        else: _a = lx
    return lx if f(lx) < f(rx) else rx

# didn't see any differences with two-summand numerator
def fib(n):
    return ceil(floor(((1+sqrt(5))/2)**n)/sqrt(5))

def fibonacci(f, a, b, eps):
    lx = None
    rx = None
    _a = deepcopy(a)
    _b = deepcopy(b)
    # as fibonacci numbers are growing fast, we can use this loop
    n = 1
    while (_b - _a)/eps >= fib(n + 2):
        n += 1
    print('n = ' + str(n))
    for k in range(0,n + 1):
        lx = _a + fib(n - k + 1)/fib(n - k + 3)*(_b - _a)
        rx = _a + fib(n - k + 2)/fib(n - k + 3)*(_b - _a)
        fl = f(lx)
        fr = f(rx)
        print('_a, _b = ' + str((_a,_b)))
        print('lx, rx = ' + str((lx,rx)))
        print('f: ' + str((fl,fr)))
        print
        if fl < fr: _b = rx
        else: _a = lx
    return lx if f(lx) < f(rx) else rx

if __name__ == '__main__':
    if len(argv) < 4:
        print('Usage: ' + argv[0] + ' a b eps delta')
        exit(1)

    pd = [float(x) for x in argv[1:]]
    f = lambda x: x**2 + 2*x - 4

    xd = dichotomy(f, pd[0], pd[1], pd[2], pd[3])
    xg = golden_ratio(f, pd[0], pd[1], pd[2])
    xf = fibonacci(f, pd[0], pd[1], pd[2])
    
    print(xd, xg, xf)
    print(xd + 1, xg + 1, xf + 1)
