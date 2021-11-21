# # client.py
# # import socket

# import subprocess

# from threading import Thread
# from time import sleep


# # s = socket.socket()
# # s.connect(('localhost', 1337))
# popen = None

# def execute(cmd):
#     print ("im here")
#     popen = subprocess.Popen(cmd, 
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE, universal_newlines=True)
#     for stdout_line in iter(popen.stdout.readline, ""):
#         yield stdout_line 
#     popen.stdout.close()
#     return_code = popen.wait()
#     if return_code:
#         raise subprocess.CalledProcessError(return_code, cmd)

# # Example

# def output_loop():
#     for path in execute(["python"]):
#         print(path, end="")

# # Example
# # await execute("python")
#     # print(path, end="")

# if __name__ == "__main__":

#     input ("First input")

#     thread = Thread(target = output_loop)


#     thread.start()
#     thread.join()

#     sleep(2)
#     # popen.communicate(str(input("I am here")).encode('utf-8'))
#     popen.stdin.write(str(input("I am here").encode('utf-8')))
#     sleep(2)

#     print("thread finished...exiting")


# # popen = subprocess.Popen(['python',], stdout=subprocess.PIPE, universal_newlines=True)
# # for stdout_line in iter(popen.stdout.readline, ""):
# #     yield stdout_line 
# #     popen.communicate(str(input()).encode('utf-8'))
# # popen.stdout.close()

# # while (process.wait()):
#     # process.communicate(str(input()).encode('utf-8'))



#from subprocess import Popen, PIPE

#p1 = Popen(['python'],stdin=PIPE, stdout=PIPE)
# # p2 = Popen(['sed', '/^$/d'],               stdin=p1.stdout, stdout=PIPE)
# # p3 = Popen(['awk', 'NR > 1 { print $2 }'], stdin=p2.stdout, stdout=PIPE)

#p1.stdin.write("print('hello world!')".encode('utf-8'))

#p1.wait()
# stdout, _ = p1.communicate()





#!/usr/bin/env python3
import time
#from subprocess import Popen, PIPE
import subprocess

proc = subprocess.Popen("python", stdin=subprocess.PIPE)
#while (proc.poll() is None):
proc.stdin.write("print('hello world!!')".encode('utf-8')) # etc
    #time.sleep(4)