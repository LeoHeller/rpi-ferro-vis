#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi

# enable debugging
import cgitb
cgitb.enable()

# get form value
form = cgi.FieldStorage()
magnet0 = form.getvalue("magnet0")
magnet1 = form.getvalue("magnet1")
magnet2 = form.getvalue("magnet2")
magnet3 = form.getvalue("magnet3")

with open("/tmp/server_values.txt", "w") as myfile:
    help = "%s %s %s %s\n" % (magnet0, magnet1, magnet2, magnet3)
    myfile.write(help)

# print("Content-Type: text/plain\n")
print("Location: index.html\n")

