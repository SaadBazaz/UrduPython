# UrduPython
Write simple Python in Urdu.

## Pre-requisites
- Python 3+
- Pip
- (optional but recommended) Virtual environment, like ```conda``` or ```virtualenv```

## How to Install
1. Download this repo as a ZIP, or clone it via Git.
2. Open the repo's folder in your Terminal.
3. Run ```pip install -r requirements.txt```

## How to Use
1. Create a new file in a folder.
2. Write some Urdu code in this new file.
The mappings are as following:

| Python (original)   | 🇵🇰 Ur          |
| -------------       | ------------- |
|    ```print```             |       لکھو|
|    ```if```                |       اگر|
|    ```elif```              |       ورنہاگر|
|    ```else```              |       ورنہ|
|    ```while```             |       جبتک|
|    ```for```               |       جو|
|    ```in```               |       اندر|
|    ```input```             |       داخله|
|    ```break```             |       توڑ|
|    ```continue```          |       جاری|
|    ```pass```              |       گزر|
|    ```True```              |       حق|
|    ```False```             |       باطل|
|    ```is```                |       ہے|
|    ```class```             |       طبقه|
|    ```def```               |       وضح|
|    ```init```              |       ابتدا|
|    ```self```              |       خود|
|    ```return```            |       واپس|
|    ```string```            |       ستلی|
|    ```str```               |   ستل|
|    ```append```                |   شامل|
|    ```pop```               |   نکل|
|    ```and```               |   اور|
|    ```or```                   |   یا|
|    ```all```               |   سب|
|    ```any```               |   کوئ|
|    ```None```              |   ندارد
|    ```,```                |       ،       |
|    ```.```                |       ۔|
|    ```0```                 |       ۰|
|    ```1```                 |       ۱|
|    ```2```                 |       ۲|
|    ```3```                 |       ۳|
|    ```4```                 |       ۴|
|    ```5```                 |       ۵|
|    ```6```                 |       ۶|
|    ```7```                 |       ۷|
|    ```8```                 |       ۸|
|    ```9```                 |       ۹|

Find the whole list at ```languages/ur/ur_native.lang.yaml```. Don't worry if you can't find a mapping, you can also use English Python!

An example of a Hello World Program:
```
print ("Hello world!")
```
would be
```
لکھو ("Hello world!")
```

3. Open a Terminal in the folder of this file.
4. Run the code in one command: ```python urdu_python__ply.py <NAME_OF_YOUR_FILE>```

For more help, run ```python urdu_python__ply.py --help```. For better understanding, do run the sample code files in the "samples" folder.

## Guide
### For macOS
Use TextEdit (default text editor) to write Urdu code. Activate right-to-left typing through Menu: Format->Text->Writing Direction->Right-to-Left

### For Linux/Windows
Download and install Notepad++. Right click and activate RTL (Right-to-left).

## Tests
### Platform(s) tested on
macOS Big Sur 11.1
