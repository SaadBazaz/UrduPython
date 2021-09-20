# ------------------------------------------------------------
# urdu_python.py
#
# Main driver file. 
# - Arguments are captured here
# - The parsing mode is called from here with the same args as this file
# ------------------------------------------------------------


import argparse

# construct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument('file', metavar='F', type=str, nargs='+',
                    help='File to compile.')
ap.add_argument("-t", "--translate", 
                    action='store_true',
                    default=False, required = False, 
                    help = "Translate variables and functions to English, using the unicode.")
ap.add_argument("-m", "--mode",
                    default="lex", required = False, 
                    help = "The mode to use to translate the code.")
ap.add_argument("-d", "--dictionary",
                    default="./languages/ur/ur_native.lang.yaml", required = False, 
                    help = "The dictionary to use to translate the code.")



group = ap.add_mutually_exclusive_group(required=False)

group.add_argument("-k", "--keep", 
                    action='store_true',
                    default=False, required = False, 
                    help = "Save the compiled file to the specified location.")
group.add_argument("-ko", "--keep-only", 
                    action='store_true',
                    default=False, required = False, 
                    help = "Save the compiled file to the specified location, but don't run the file.")

args = vars(ap.parse_args())

import importlib

mod = importlib.import_module("src."+args["mode"])
mod.run(args)