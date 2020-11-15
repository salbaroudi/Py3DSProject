#!/usr/bin/env python3.8

import sys
import json


#Script assumes that first argument is the selected file, and second argument is the output file name.
#getopt not implemented, nor error processing. 
#jupyter nbconvert <yournotebook>.ipynb --to <html/pdf> --output <newnotebookname>.ipynb


with open("./" + sys.argv[1], 'r') as f:
    nb = json.load(f)
cells = nb['cells']

newCellList = []

for cell in cells:
    if cell['metadata'].get('tags') is not None: #cell['metadata'].get('tags') != {}:
        newCellList.append(cell)
        
outerSet = {"cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

f = open("./" + sys.argv[2], "w")
outerSet["cells"] = newCellList

f.write(json.dumps(outerSet))  
f.close()
