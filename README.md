Having trouble ordering pizza? Is the timeless conundrum of finding the right pie for the party getting you down? No longer! Use the pizzavalue calculator to quickly determine common za-metrics and optimize your pizza selection like the pros.

# Usage

```
pizzavalue.py [-h] [-n NAME] [-p PEOPLE] [-s] [-x SLICES] cost size

positional arguments:
  cost                  cost of the pizza
  size                  size of the pizza. For round pizzas, this is the
                        diameter. For square pizzas, this is the edge length.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  name of the option, ie. Dimo's 20" BBQ Bacon Chicken
                        Cheddar Ranch
  -p PEOPLE, --people PEOPLE
                        number of people in your party
  -s, --square          pizza is square (defaults to round)
  -x SLICES, --slices SLICES
                        number of slices


```

# Output

With the required arguments, pizzavalue will output the cost per square inch of pizza as a convenient unit comparison.

Including `--people {integer}` will also tell you the square inches and cost per person to help with splitting the tab.

`--slices {integer}` will minimally provide the square inches and cost per slice. Paired with `-p`, it will also tell you how many slices per person.

`--name` is handy if you're testing many possible pizzas. It will be more useful when I get a chance to implement tabular output and multiple pies; this will enable pizza pivots.
