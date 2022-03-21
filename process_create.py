#!/usr/local/bin/python3

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form['description'].value

oppend_file = open('data/'+title, 'w')
oppend_file.write(description)
oppend_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
