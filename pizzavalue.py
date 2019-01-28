#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sys
import math
import argparse

ROUND  = 0
SQUARE = 1

parser = argparse.ArgumentParser(description='Calculate the cost per square inch of a pizza')
parser.add_argument('diameter', type=float, help='size of the pizza. For square pizzas, this is the edge length')
parser.add_argument('cost', type=float, help='cost of the pizza')
parser.add_argument('-n','--name', help='name of the option, ie. Dimo\'s 20" Chicken Bacon Cheddar Ranch')
parser.add_argument('-s','--square', dest='shape', action='store_const',
                    const=SQUARE, default=ROUND,
                    help='pizza is square (default: round)')

args = parser.parse_args()

diameter = args.diameter
cost     = args.cost
area     = 1 # default

if args.shape == ROUND:
	area = math.pi * ((diameter / 2.0) ** 2)
elif args.shape == SQUARE:
	area = diameter ** 2

cpa = cost / area

label = ''
if args.name:
	label = '{}: '.format(args.name)

print("{}{:.0f} inch diameter for ${:.2f}: {:.0f} square inches of pizza for ${:.2f} per square inch".format(label,diameter,cost,area,cpa))
