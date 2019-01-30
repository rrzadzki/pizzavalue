#!/usr/bin/python3

import sys
import math
import argparse

ROUND  = 0
SQUARE = 1

# Make a dict of output formats and assign it early
OUTPUT_OPTIONS_TABULAR = ['t','tab','tabular']
OUTPUT_OPTIONS_CSV     = ['c','csv']

parser = argparse.ArgumentParser(description='Calculate common pizza metrics')

parser.add_argument('cost',
                    help='cost of the pizza',
                    type=float)

parser.add_argument('size',
                    help='size of the pizza. For round pizzas, this is the diameter. For square pizzas, this is the edge length.', 
                    type=float)

parser.add_argument('-n','--name',
                    help='name of the option, ie. Dimo\'s 20" BBQ Bacon Chicken Cheddar Ranch')

'''
# Not yet implemented
parser.add_argument('-o','--output',
                    help='output format',
                    default='paragraph')
'''

parser.add_argument('-p','--people',
                    help='number of people in your party',
                    type=int)

parser.add_argument('-s','--square',
                    help='pizza is square (defaults to round)',
                    dest='shape',
                    action='store_const',
                    const=SQUARE,
                    default=ROUND)

parser.add_argument('-x','--slices',
                    help='number of slices',
                    dest='slices',
                    type=int)

'''
 TODO:
 + Type of pizza (thick, thin, etc.) and some volume / weight calculations
 + Arguments for additional pizzas for comparison's sake
 + Output format - include tabular and CSV to support pivoting and charting pizzas
'''

args = parser.parse_args()

pizza = {}

if args.name:
	pizza['Name'] = args.name

pizza['Size'] = args.size
pizza['Cost'] = args.cost

if args.shape == ROUND:
	pizza['Area'] = round(math.pi * ((args.size / 2.0) ** 2),2)
elif args.shape == SQUARE:
	pizza['Area'] = round(args.size ** 2,2)

pizza['Cost per unit area'] = round(args.cost / pizza['Area'],2)

if args.people:
    pizza['Cost per person'] = round(args.cost / args.people,2)
    pizza['Area per person'] = round(pizza['Area'] / args.people)

if args.slices:
    pizza['Area per slice'] = round(pizza['Area'] / args.slices,2)
    pizza['Cost per slice'] = round(args.cost / args.slices,2)
    if args.people:
        pizza['Slices per person'] = round(args.slices / args.people, 2)

for key in list(pizza.keys()):
    print("{}: {}".format(key,pizza[key]))

