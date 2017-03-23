#!/usr/bin/env python

import os
import sys
import difflib
import subprocess
from filecmp import dircmp
from time import gmtime, strftime

logdate = '{0}_{1}'.format('',strftime('%I%M%S%p_%Y%m%d'))
home = os.environ['HOME']

output_directory = home + '/diffinator/'
if not os.path.isdir(output_directory):
    os.system('mkdir ' + output_directory)


def main():
    # if flag --diff used:
    # $ diffinator --diff www.winterline.com
    # using '--diff' downloads the updated site and diffs it with the original
    if sys.argv[1] == '--diff':
        url = sys.argv[2]
        wget(url)
        # outputfile = '../../diffinator/' + url + '_diff_' + logdate + '.txt'
        outputfile = '../../diffinator/' + url + '_diff' + '.txt'

        # search for old url directory that matches sys.argv[2]
        for directory in os.listdir(output_directory):
            # do the diff'ing here
            if directory.startswith(url):
                newdir = url + logdate
                out = os.popen('diff -r ../../diffinator/' + newdir + ' ../../diffinator/' + directory + ' >> ' + outputfile, 'w')

    # else->wget 1st url copy
    # $ diffinator www.winterline.com
    else:
        url = sys.argv[1]
        wget(url)

# wget wrapper. ignores images, puts output in /diffinator/ directory under current User
# with the timestamped date and time of download
def wget(url):
    os.system('wget -p --reject *.jpg,*.png --directory-prefix=' + output_directory + ' ' + url)
    os.system('mv ' + output_directory + url + ' ' + output_directory + url + logdate)

if __name__ == '__main__':
    main()
