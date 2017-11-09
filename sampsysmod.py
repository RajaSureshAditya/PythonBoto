#!/usr/bin/env python

import sys

print sys.argv

for i in range(len(sys.argv)):
     if i == 0:
         print "Funcion aname is %s" + sys.argv[0]
     else:
         print "%d. arguments are %s" % (i,sys.argv[i])
