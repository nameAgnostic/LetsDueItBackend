from flask import Flask

##  ::INFORMATION::
## Required items for using flask (that I've found so far):
##
## I usually name this code launchserver.py (otherwise you'll have to change code later)
## optional? make a secret key
## optional: make a routes.py file
## pip install flask
## this code must be run from the cmd line of the os
##    C:\Users\Shawn\Desktop> python launchserver.py
## browse to the IP that the output in the cmd line tells you


#flask stuff
app = Flask(__name__)
#app.secret_key = ""
#wsgi_app = app.wsgi_app

#launch the server
from routes import * #this is your routes.py code
if __name__ == '__main__':
    app.run()

