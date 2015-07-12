#!/usr/bin/python
import string
from random import randint
import sys
def main(length, passes, mode):
   pw = []
   sz = ['!','$','%','&','?','@','>','<']
   for p in range(passes):
      for i in range(length):
         r4 = randint(0, mode)
         if r4 == 0:
            pw.append(randint(0, 9))
         elif r4 == 1:
            pw.append(string.lowercase[randint(0, 25)])
         elif r4 == 2:
            pw.append(string.uppercase[randint(0, 25)])
         elif r4 == 3:
            pw.append(sz[randint(0, 7)])
      for letter in pw:
         if type(letter) == int: sys.stdout.write(str(letter))
         else: sys.stdout.write(letter)
      sys.stdout.write('\n')
      pw = []
   uniqueness = 10;
   if mode == 1:
      uniqueness += 26
   elif mode == 2:
      uniqueness += 52
   elif mode == 3:
      uniqueness += 60
   print "Guesability: " + str(uniqueness**length)

def usage():
   print "password generator:"
   print "usage: pw.py <number of characters> <number of passes> [<mode>]"
   print "mode 0: only numbers"
   print "     1: numbers and lowercase letters"
   print "     2: numbers and letters"
   print "     3: numbers, letters and special characters (default)"
   exit(1)

if __name__ == '__main__':
   for i in range(len(sys.argv)-1):
      try:
         int(sys.argv[i+1])
      except:
	 print sys.argv[i+1]
	 print type(sys.argv[i+1])
         usage()
   if len(sys.argv) == 3:
      main(int(sys.argv[1]), int(sys.argv[2]), 3)
   elif len(sys.argv) == 4 and int(sys.argv[3]) >= 0 and int(sys.argv[3]) <= 3:
      main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
   else:
      usage()

