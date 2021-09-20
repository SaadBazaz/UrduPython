def my_func():
    print ("lol")

from unidecode import unidecode

import yaml

loaded_dict = yaml.load(open("./ur_native.yaml"))
print (loaded_dict)

print ("unidecode('1000') ->", unidecode("1000"))
print ("unidecode('abcd') ->", unidecode("abcd"))
print ("unidecode('א') ->", unidecode("א"))

print ("type(my_func) ->", type(my_func))
print ("callable(my_func) ->", callable(my_func))

print ("type(print) -> ", type(print))
print ("callable(print) -> ", callable(print))

open = "lol"

print ("type(open) -> ", type(open))


import types
print ("types.FunctionType -> ", types.FunctionType)

print ("isinstance(print, types.FunctionType) -> ", isinstance(print, types.FunctionType))

print ("isinstance(print, (types.FunctionType, types.BuiltinFunctionType)) -> ", isinstance(print, (types.FunctionType, types.BuiltinFunctionType)))

import functools

print ("isinstance(print, (types.FunctionType, types.BuiltinFunctionType, functools.partial)) -> ", isinstance(print, (types.FunctionType, types.BuiltinFunctionType, functools.partial)))

from inspect import isfunction, isbuiltin

print("isfunction(print) -> ", isfunction(print))
print("isbuiltin(print) -> ", isbuiltin(print))