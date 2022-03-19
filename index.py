#!/usr/local/bin/python3
print("content-Type: text/html")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else:
    pageId = 'welcome'
    description = 'hello, web'    
    update_link = ''
print('''<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
      {listStr}
    <ol>
    <a href="create.py">create</a>
    <a href="update.py">update</a>
    <h2>{title}</h2>
    <P>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link))