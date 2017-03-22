#!/usr/bin/env python

import filecmp
import os
import sys
from time import gmtime, strftime
from datetime import date

os.environ['HOME']

logdate = '{0}_{1}'.format('',strftime('%I%M%S%p_%Y%m%d'))

home = os.environ['HOME']
output_directory = home + '/diffinator/'
if not os.path.isdir(output_directory):
    os.system('mkdir ' + output_directory)

url = sys.argv[1]
os.system('wget -p --reject *.jpg,*.png --directory-prefix=' + output_directory + ' ' + url)
os.system('mv ' + output_directory + url + ' ' + output_directory + url + logdate)
os.system('rm ' + output_directory + url)

path_to_project = output_directory + url + logdate
