import os
import sys

cmd = ""
for i in range(1,len(sys.argv)):
     cmd = cmd + "-path " + sys.argv[i] + " -prune -o "
cmd = "find . " + cmd + "-name '*' -print | sed -e 's;[^/]*/;|_ ;g;s;_ |;  |;g'"
os.system(cmd)