a=int(input())
if (a % 4) == 0:
   if (a % 100) == 0:
       if (a % 400) == 0:
           print("yes".format(a))
       else:
           print("no".format(a))
   else:
       print("yes".format(a))
else:
   print("no".format(a))
