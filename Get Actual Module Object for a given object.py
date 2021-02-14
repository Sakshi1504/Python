#get the actual module object for a given object
from inspect import getmodule
from math import pow
from os.path import basename
print(getmodule(pow))
print(getmodule(basename))