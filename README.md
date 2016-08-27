# Pype

A general purpose sh-like forward pipe operator for Python.

# Simple Example
```
from pype.pype import p

def hello_world(x):
    print "Hi {0}!".format(x)

>>> 'Charles' |p| hello_world
Hi Charles!
```
# Slightly More Complex Example
```
from pype.pype import p

def double_and_sum(num_lst):
    # Create a curried mapper function
    create_mapper = lambda (fn): lambda (lst): map(fn, lst)
    mult = lambda n: n * 2
    # Application of multiple pipes
    return num_lst |p| (mult |p| create_mapper) |p| sum

>>> [n for n in range(100)] |p| double_and_sum
9900
```
