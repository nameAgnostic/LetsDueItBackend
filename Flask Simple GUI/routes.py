from flask import Flask, url_for, request, render_template, jsonify, session, redirect, flash
from launchserver import app #gets the app variable from launchserver.py
#import mainfunctions

@app.route('/')
def mainpage():
    return '<h1>Main Page!</h1>'

@app.route('/interactive')
def interactive():
    try:
        return render_template("interactive.html")
    except Exception as e:
        return(str(e))

@app.route('/background_process')
def background_process():
    try:
        input1 = request.args.get('userInput')
        input2 = request.args.get('userInput2')
        #do stuff with userInput
        output = "1: " + input1 + "    2: " + input2
        return jsonify(result='This is what I came up with:'+output)
    except Exception as e:
        return(str(e))
