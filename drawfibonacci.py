#!/usr/bin/env python 2.7.5
#-*- coding:utf-8 -*-
"""
draw fibonacci spiral
"""

import turtle
import math
"""
turtle.speed=10
fib={}
fib[0]=20
fib[1]=20
angle = 90
limit=6

def drawArc():
    global angle
    for h in range(1,angle):
        turtle.forward(1)
        turtle.left(angle)
        angle = angle+5
for i in range(2,limit):
    #global fib
    fib[i]=fib[i-2]+fib[i-1]
for i in range(0,limit):
    length=(2*fib[i]*math.pi)/10
    drawArc()
    textWindow.writeLine("Fib("+i+")="+fib[i])

"""
"""
This programs draws a Fibonacci spiral and writes down the
corresponding Fibonacci numbers and their ratios.

Sequence:

S_ini:  1
S_next: F(n) / F(n-1)
S_end:  ratio converges
"""

import turtle
# Epsilon to check the ratio convergence
EPSILON=1e-7

# main =====================================================
if __name__ == "__main__":
	# Write the first Fibonacci number
	print "x= 1"

	# Start sequence: S_ini
	xb = 0.1
	xc = 0.1
	ratio_prev = 0.
	ratio      = xc / xb

	# Check whether the sequence has ended: S_end
	while ( abs(ratio-ratio_prev) > EPSILON ):
        

		# Write Fibonacci number at ratio
		print "x=", xc, "ratio=", ratio

		# Draw with the turtle
		# - Square
		turtle.color("red")
		turtle.forward( xc )
		# - back
		turtle.up()
		turtle.backward( xb )
		turtle.down()

		# - Circle
		turtle.color("blue")
		turtle.circle(xb, 90)
		# - back
		turtle.up()
		turtle.backward( xb )
		turtle.down()

		# Compute next element in the sequence: S_next
		xa = xb
		xb = xc
		xc = xa + xb

		ratio_prev = ratio
		ratio      = float(xc) / float(xb)

