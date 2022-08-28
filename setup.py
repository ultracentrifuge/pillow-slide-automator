import os
import time

opersys = input("What device are you on? (Windows/Mac/Linux) ")

match opersys:
  case "Windows":
    os.system("pip install pillow")
  case "Mac":
    os.system("pip3 install pillow")
  case "Linux":
    os.system("pip install pillow")

print("All done!")

time.sleep(2)
