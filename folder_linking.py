# -*- coding: UTF-8 -*-
#
# Hobin Liang 08/20/2019
#

import os, sys

if len(sys.argv) == 1:
    print("Usage: " + sys.argv[0] + " SRC")
    exit(0)

path = sys.argv[1]
if not os.path.isdir(path):
    print("cannot access '" + path + "': No such directory")
    exit(0)

# setting
exclude = {
    "Temp": True,
}

files = os.listdir(path)
for file in files:
    # print("file: " + file)
    src = path + "\\" + file
    if exclude.has_key(file):
        print("exclude file: " + file)
    elif os.path.exists(file):
        print("file exists: " + file)
    else:
        opt = os.path.isdir(src) and " /j" or ""
        cmd = "mklink" + opt + " \"" + file + "\" \"" + src + "\""
        print(cmd)
        os.system(cmd)
        