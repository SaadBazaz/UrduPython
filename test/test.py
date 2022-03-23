def my_func():
    print ("lol")

from unidecode import unidecode

import yaml

loaded_dict = yaml.load(open("../urdupython/languages/ur/ur_native.lang.yaml"))
print (loaded_dict)

print ("unidecode('1000') ->", unidecode("1000"))
print ("unidecode('abcd') ->", unidecode("abcd"))

print ("type(my_func) ->", type(my_func))
print ("callable(my_func) ->", callable(my_func))

print ("type(print) -> ", type(print))
print ("callable(print) -> ", callable(print))

# open = my_func

print ("type(open) -> ", type(open))


import types
print ("types.FunctionType -> ", types.FunctionType)

print ("isinstance(print, types.FunctionType) -> ", isinstance(print, types.FunctionType))

print ("isinstance(print, (types.FunctionType, types.BuiltinFunctionType)) -> ", isinstance(print, (types.FunctionType, types.BuiltinFunctionType)))

import functools

print ("isinstance(print, (types.FunctionType, types.BuiltinFunctionType, functools.partial)) -> ", isinstance(print, (types.FunctionType, types.BuiltinFunctionType, functools.partial)))

from inspect import isfunction, isbuiltin, getmodule

import sys

print("isfunction(print) -> ", isfunction(print))
print("isbuiltin(print) -> ", isbuiltin(print))

from numpy import random, array

print ("random.random -> ", random.random)
print ("type(random.random) -> ", type(random.random))
print ("random.random.__name__ -> ", random.random.__name__)
print ("getmodule(random.random) -> ", getmodule(random.random))
# print ("getmodule(random.random).__name__ -> ", getmodule(random.random).__name__)
# print ("random.random.__module__ -> ", random.random.__module__)
# print ("getmodule(random.random) -> ", sys.modules[random.random.__module__])


print ("open -> ", open)
print ("type(open) -> ", type(open))
print ("open.__name__ -> ", open.__name__)
print ("getmodule(open) -> ", getmodule(open))
print ("getmodule(open).__name__ -> ", getmodule(open).__name__)
print ("open.__module__ -> ", open.__module__)
print ("getmodule(open) -> ", sys.modules[open.__module__])




# print ("replaceme -> ", replaceme)
# print ("type(replaceme) -> ", type(replaceme))
# print ("replaceme.__name__ -> ", replaceme.__name__)
# print ("getmodule(replaceme) -> ", getmodule(replaceme))
# print ("getmodule(replaceme).__name__ -> ", getmodule(replaceme).__name__)
# print ("replaceme.__module__ -> ", replaceme.__module__)
# print ("getmodule(replaceme) -> ", sys.modules[replaceme.__module__])

