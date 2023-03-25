from cmu_graphics import *
import random
import copy
import math

def onAppStart(app):
    reset(app)

def reset(app):
    app.health = random.randint(70, 99)
    app.hygiene = random.randint(70, 99)
    app.time = 8
    app.timePeriod = 'am'
    app.displayTime = app.time
    app.date = 'Mon'
    app.text = 'Insert text here...'

def onStep(app):
    pass

def redrawAll(app):
    #tasks
    drawRect(10, 10, 40, 40, fill='grey')
    drawLabel("Tasks", 30, 30, size=12)
    #health
    drawRect(60, 10, 160, 40, fill='black')
    drawRect(60, 10, app.health*1.6, 40, fill='red')
    drawLabel('Health', 140, 30, size=20, fill='white', bold=True)
    #hygiene
    drawRect(230, 10, 160, 40, fill='black')
    drawRect(230, 10, app.hygiene*1.6, 40, fill='green')
    drawLabel('Hygiene', 310, 30, size=20, fill='white', bold=True)
    
    #time
    drawRect(10, 300, 40, 40, fill='grey')
    drawLabel(f'{app.displayTime} {app.timePeriod}', 30, 320, size=12)

    #date
    drawRect(10, 350, 40, 40, fill='grey')
    drawLabel(app.date, 30, 370, size=12)

    #time and date
    drawRect(60, 300, 330, 90, fill='grey')
    drawLabel('Insert text here...', 225, 345, size=12)

def increaseTime(app, hours):
    app.time += hours

    #checks for overflow
    if app.time > 24:
        app.time -= 24
        dateChange(app)
    
    #changes the am and pm
    if app.time >= 12 and app.time < 24:
        app.timePeriod = 'pm'
    else:
        app.timePeriod = 'am'
    
    #changes the displayed time
    if app.time <= 12:
        app.displayTime = app.time
    else:
        app.displayTime = app.time - 12

def dateChange(app):
    if app.date == 'Mon':
        app.date = 'Tues'
    elif app.date == 'Tues':
        app.date = 'Wed'
    elif app.date == 'Wed':
        app.date = 'Thur'
    


def onKeyPress(app, key):
    if key =='t':
        increaseTime(app, 1)
    if key == 'r':
        reset(app)

def main():
    runApp()

main()
