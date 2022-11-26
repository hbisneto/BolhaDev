## MacApp File
## This file is used to implement code used to run scripts for Mac

import Tokens
from exception import Exceptions
from mac import FileSystem

def NewTweet():
   print("="*80)
   print("NEW TWEET")
   print("="*80)
   Tweet = str(input(">>[!] Whats happening? "))
   print("="*80)
   print()
   print("-"*80)
   print(">> Your tweet was sent")
   print("-"*80)
   print()
   print("="*80)

   try:
      Tokens.Twitter.update_status(Tweet)
      print(f'>> Your last tweet:')
      print(f' > {Tweet}')
      print("-" * 80)
   except:
      print(">>  Something went wrong: Unabled to connect to Twitter.")

def Main():
   NewTweet()

Main()
