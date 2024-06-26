import os
import time

def typewrite(message):
  for char in message:
        print(char, end="", flush=True)
        time.sleep(0.01)
  print()
  
def clearScreen():
      if os.name == "nt":
                os.system("cls")