#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:12:36 2021

@author: jadenbayrooti
"""

from graphics import *
from perlin_noise import PerlinNoise

xpix, ypix = 500, 500
noise = PerlinNoise(octaves=10, seed=1)

print([[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)])

print(noise([i/xpix, j/ypix]))
"""win = GraphWin("My Window", 500, 500)
pt1 = Point(250 + noise.noise(coordinates=(250,250)),250 + noise.noise(coordinates=(250,250)))
pt2 = Point(250 + noise.noise(coordinates=(250,250)),250 + noise.noise(coordinates=(250,250)))
pt3 = Point(250 + noise.noise(coordinates=(250,250)),250 + noise.noise(coordinates=(250,250)))
pt4 = Point(250 + noise.noise(coordinates=(250,250)),250 + noise.noise(coordinates=(250,250)))
pt5 = Point(250 + noise.noise(coordinates=(250,250)),250 + noise.noise(coordinates=(250,250)))
poly = Polygon(pt1,pt2,pt3,pt4,pt5)
poly.draw(win)

win.getMouse()
win.close()"""
