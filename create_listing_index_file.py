#!/usr/bin/env python

"""create an index.html file that shows a listing with all folders
   and files linked.

The first argument must the folder where to create the index file.

The index.html is only created if it does not exist. In case, the
file should just be (re-)moved before to run the script.

Examples::

    python create_listing_index_file.py .
    python create_listing_index_file.py various_ppdata  # create index.html in various_ppdata

"""

import os, sys
import time

def create_listing_index_file(path='.', name='index.html'):
    """create an html file `name` in `path` containing the linked dir list of `path`"""
    filename = os.path.join(path, name)
    ldir = sorted(os.listdir(path))
    lines = ['<A HREF="{0}">{0}</A></br>'.format(n) for n in ldir
                if not n.startswith('.')  # do not list "hidden" folders or files
                # and os.path.isdir(os.path.join(path, n))  # only list folders
            ]
    if not os.path.exists(filename):
        with open(filename, 'a') as f:  # append such the content is never destroyed
            f.writelines([s + '\n' for s in
                ['<html>',
                 '<head><meta charset="utf-8" /></head>',
                 '<body>',] +
                lines +
                ['<p style="font-size: 70%">Created: {}</p>'.format(time.asctime()),
                 '</body>',
                 '</html>']])
    else:
        print('Warning: nothing done as {} already exists.'
              ' Remove it before to run this script.'.format(filename))

def _create_all_subfolders_listing_index_files(path='.', name='index.html'):
    """walk through all subfolders, often not a good idea as there are too many exceptions"""
    for p, d, f in os.walk(path):
        if ((p.startswith('.') and len(p) > 1 and p[1] != os.path.sep)
            or os.path.sep + '.' in p):  # don't write in ./.git
            continue
        print(p)
        # create_listing_index_file(p, name)
        # os.system('git add {}'.format(os.path.join(p, name)))  # or we needed to add *all* files
        
if __name__ == '__main__':
    if len(sys.argv) < 1 or sys.argv[0].startswith('-'):
        print(__doc__)
    try:
        create_listing_index_file(sys.argv[1])
    except:
        print(__doc__)
