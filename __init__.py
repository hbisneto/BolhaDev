## __init__.py File
## Here the contents will be processed to choose the best platform to go

try:
   ## Imported Libraries
   from sys import platform

   ## Local Libraries
   from exception import Exceptions
except:
   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

def Main():
   Platform = platform

   ## Linux
   if Platform == "linux" or Platform == "linux2":
      from linux import Linux
      Linux.Linux()

   ## Mac
   elif Platform == "darwin":
      from mac import Mac
      Mac.Mac()

   ## Windows
   elif Platform == "win32" or Platform == "win64":
      from windows import Windows
      Windows.Windows()

Main()