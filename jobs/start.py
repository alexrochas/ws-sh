#!/usr/bin/env python
import sys
from subprocess import check_output

print "Content-Type: text/html\n\n"
print "OK"
cmd = ['./jobs/job.sh']
sys.stderr.write("Starting job.\n")
sys.stderr.write(check_output(cmd))
