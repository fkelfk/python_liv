#!/usr/local/bin/python3
print("content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
PageID = form["id"].value

print('''<!doctype html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.html">WEB</a></h1>
    <ol>
        <li><a href="index.py?id=HTML">HTML</a></li>
        <li><a href="index.py?id=CSS">CSS</a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    <ol>
    <h2>{title}</h2>
    <P>the World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are indntified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the Wolrd Wide Web in 1989. He wrote the firist web browser computer program in 1990 while employed at CERN in Switzerland. [2][3]  The Web browser was released outside of CERN in 1991, first to other research institution starting in January 1991 and to the general public on th Internet in August 1991.
    </p>
</body>
</html>
'''.format(title=PageID))
