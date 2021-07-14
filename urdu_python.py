ur_pyfile = open("سامپل۔پے")

language_dict = {
    "،":    ",",
    "۱":    "1",
    "۲":    "2",
    "۳":    "3",
    "۴":    "4",
    "۵":    "5",
    "۶":    "6",
    "۷":    "7",
    "۸":    "8",
    "۹":    "9",
    "۰":    "0",
    "چھاپ": "print",
    "اگر":  "if",
    "ورنہ": "else",
    "جبتک": "while",
    "جو":   "for",
    "اندر": "in", 
}

words = ur_pyfile.read()

for key, value in language_dict.items():
    words = words.replace(key, value)

eng_pyfile = open("eng.py", "wt")
n = eng_pyfile.write(words)
eng_pyfile.close()

import eng

import os
if os.path.exists("eng.py"):
  os.remove("eng.py")
else:
  print("The file does not exist")