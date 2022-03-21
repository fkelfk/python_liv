#!/usr/local/bin/python3

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form['description'].value

oppend_file = open('data/'+pageId, 'w')
oppend_file.write(description)
oppend_file.close()


os.rename('data/'+pageId, 'data/'+title)

#Redirection
print("Location: index.py?id="+title)
print()
