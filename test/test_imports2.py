# References:
# - https://stackoverflow.com/questions/9439480/from-import-vs-import
# - https://stackoverflow.com/questions/4858100/how-to-list-imported-modules

import types
def imports():
    for name, val in globals().items():
        if isinstance(val, types.ModuleType):
            yield val.__name__

imports ()



import sys
modulenames = set(sys.modules) & set(globals())
allmodules = [sys.modules[name] for name in modulenames]
print ("sys.modules:", [mod for mod in sys.modules])
print ("globals():", [_global for _global in globals()])


print ("Intersected modules:")
for module in allmodules:
    print (module.__name__)


# print ("=======================")

# from numpy import random

# modulenames = set(sys.modules) & set(globals())
# allmodules = [sys.modules[name] for name in modulenames]
# print ("sys.modules:", [mod for mod in sys.modules])
# print ("globals():", [_global for _global in globals()])


# print ("Intersected modules:")
# for module in allmodules:
#     print (module.__name__)


# print ("=======================")

# import pandas as pd

# modulenames = set(sys.modules) & set(globals())
# allmodules = [sys.modules[name] for name in modulenames]
# print ("sys.modules:", [mod for mod in sys.modules])
# print ("globals():", [_global for _global in globals()])


# print ("Intersected modules:")
# for module in allmodules:
#     print (module.__name__)



# print ("=======================")

# import pandas as پد

# modulenames = set(sys.modules) & set(globals())
# allmodules = [sys.modules[name] for name in modulenames]
# print ("sys.modules:", [mod for mod in sys.modules])
# print ("globals():", [_global for _global in globals()])


# print ("Intersected modules:")
# for module in allmodules:
#     print (module.__name__)

# print ("type(پد): ", type(پد).__name__)
# print ("type(pandas): ", type(pandas).__name__)

# print ("=======================")

# from urllib import request

# modulenames = set(sys.modules) & set(globals())
# allmodules = [sys.modules[name] for name in modulenames]
# print ("sys.modules:", [mod for mod in sys.modules])
# print ("globals():", [_global for _global in globals()])


# print ("Intersected modules:")
# for module in allmodules:
#     print (module.__name__)

code_pyfile = open("sample_import_code.py")
code = code_pyfile.readlines()

print ("Code is:", code)

import test_lex

for line in code:
    returned = test_lex.run(args = {
                            'translate': True,
                            'dictionary': './ur_native_3.lang.yaml',
                            'reverse': False,
                            'keep': False,         
                            'keep_only': False,
                            'return': True,
                        },
                code = line
                )
    print (returned)
