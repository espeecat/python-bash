# Python function to call Unix Diff command recursively over files
#  
#  I have borrowed some of this from a web site but can't find the URL
#  
#  Jason Bailey May  2013

# Use python filename.py >  /tmp/file2log.txt 2>&1
# The 2>&1 will send stderr to stdout too so you also get
# diff errors of file or directory not found -which is useful too.
import os
import subprocess
from subprocess import call
print "Starting now...."

# I am using frm and target. I replace frm (from) with target
# to match the new location of files
frm = '/Volumes/path/to/from/location/'
target = '/Volumes/path/to/to/location/'

# This is just getting the frm location and uses str.replace to get
# the target location of the diff
# Now to build the diff calls
# Building diff -u frmhere totarget

for dirname, dirnames, filenames in os.walk(frm):
    # path to all filenames.
    for filename in filenames:
        # Using replace to get new (target) path of file to diff.
        fromhere = os.path.join(dirname, filename)
        fromhere = os.path.abspath(fromhere)  # not necessary I was messing to get rid of error
        totarget= fromhere.replace(frm, target)
        totarget = os.path.abspath(fromhere.replace(frm, target)) # not necessary I was messing.	
        # ensure each parameter of unix xommand is a comma separated string
		# otherwise you get the error file not find.
		# use -u to get unified output which includes filenames
        call(["diff" , "-u", fromhere,  totarget ])
    if '.svn' in dirnames:
        # don't go into any SVN directories
        dirnames.remove('.svn')
print "The End"	
