#!/usr/bin/env python3

import os
import cgi
from templates import *
from secret import *

form = cgi.FieldStorage()
enteredUsername = form.getfirst("username")
enteredPassword = form.getfirst("password")
header = "Content-Type: text/HTML"
body = ""

loginString = "loggedIn"
loginValueTrue = "1"
cookieVal = os.environ["HTTP_COOKIE"]
loginValue = False
for v in cookieVal.split("; "):
    items = v.split("=")
    if items[0] == loginString:
        loginValue = items[1] == loginValueTrue


# if enteredUsername != username or enteredPassword != password:
#     body=after_login_incorrect()

if enteredUsername == username and enteredPassword == password:
    header+=f"\nSet-Cookie: {loginString}={loginValueTrue}"
    body=secret_page(username=username, password=password)
else:
    body=login_page()

if loginValue:
    body=secret_page(username=username, password=password)

print(header)
print()
print(body)
