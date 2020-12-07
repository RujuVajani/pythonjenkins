import os
import time

name=os.environ["USER_NAME"]

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print("hello "+name)
  time.sleep(100)
