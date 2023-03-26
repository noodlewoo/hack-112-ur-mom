from cmu_graphics import *
import random
import copy
import math

def onAppStart(app):
    reset(app)

def reset(app):
    app.health = random.randint(65, 95)
    app.hygiene = random.randint(65, 95)
    #time and date
    app.time = 8
    app.timePeriod = 'am'
    app.displayTime = app.time
    app.date = 'Mon'

    #text
    app.text1 = 'Good morning! You are a 15112 student'.ljust(40)
    app.text2 = "and you have your final on Thursday 8".ljust(40)
    app.text3 = "am. Do your best to study for it!".ljust(40)

    #studying stuff
    app.isCT = False
    app.isFR = False
    app.isMC = False
    app.ctProgress = 0
    app.frProgress = 0
    app.mcProgress = 0
    app.focus = (app.health / 50 + app.hygiene / 50)/2

    #location
    app.atHome = False
    app.atLecture = False
    app.atLibrary = False
    app.atBathroom = False
    app.atRestaurant = True
    app.home = 'https://www.cmu.edu/housing/our-communities/housing-images-tours/Donner/Donner%20standard%20double-min.JPG'
    app.lecture = 'https://www.cmu.edu/computing/services/teach-learn/tes/classrooms/images/doherty_2210.jpg'
    app.study = 'https://thetartan-assets.s3.amazonaws.com/uploads/31189/original/pillbox_finals_traviswolfe_img_0201.jpg'
    app.bathroom = 'https://www.cmu.edu/housing/our-communities/housing-images-tours/Resnik/Resnik%20suite%20bathroom%20with%20shower-min.JPG'
    app.restaurant = 'https://www.cmu.edu/dining/news/new-images/ABP900x600-min.jpg'

def redrawAll(app):
    if app.atHome:
        drawImage(app.home, 0, 0)
    elif app.atLecture:
        drawImage(app.lecture,0,0)
    elif app.atLibrary:
        drawImage(app.study,0,0)
    elif app.atBathroom:
        drawImage(app.bathroom,0,0)
    elif app.atRestaurant:
        drawImage(app.restaurant,0,0)
    #tasks
    drawRect(10, 10, 40, 40, fill='lightgrey')
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
    drawRect(10, 300, 40, 40, fill='lightgrey')
    drawLabel(f'{app.displayTime} {app.timePeriod}', 30, 320, size=12)

    #date
    drawRect(10, 350, 40, 40, fill='lightgrey')
    drawLabel(app.date, 30, 370, size=12)

    #textbox
    drawRect(60, 300, 330, 90, fill='lightgrey')
    drawLabel(app.text1, 235, 315, size=14, font = "monospace")
    drawLabel(app.text2, 235, 330, size=14, font = "monospace")
    drawLabel(app.text3, 235, 345, size=14, font = "monospace")

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

def dateChange(app): #helper function
    if app.date == 'Mon':
        app.date = 'Tues'
    elif app.date == 'Tues':
        app.date = 'Wed'
    elif app.date == 'Wed':
        app.date = 'Thur'

#decrease health per hour
def decreaseHealth(app, hours):    
    if app.health >= 10:
        app.health -= (10 * hours)
    else:
        app.health = 1

#decrease hygiene per hour
def decreaseHygiene(app, hours):
    if app.hygiene >= 10:
        app.hygiene -= (5 * hours)
    else:
        app.hygiene = 1


#All Action Functions
def doEat(app):
    if app.health >= 60:
        app.health = 100
    else:
        app.health += 40
    increaseTime(app, 1)
    decreaseHygiene(1)

def doSleep(app, hours):
    healthgain = 10 * hours
    if app.health + healthgain >= 100:
        app.health = 100
    else:
        app.health += healthgain
    increaseTime(app, hours)

def doShower(app):
    if app.hygiene > 50:
        app.hygiene = 100
    else:
        app.hygiene += 50
    increaseTime(app, 1)
    decreaseHealth(1)

def doGetReady(app):
    if app.hygiene > 75:
            app.hygiene = 100
    else:
            app.hygiene += 25
    increaseTime(app, 1)
    decreaseHealth(1)

def doStudy(app):
    atLibrary = True
    if app.isCT: 
        app.ctProgress += 25 * app.focus
        app.isCT = False
    if app.isFR:
        app.frProgress += 25 * app.focus
        app.isCT = False
    if app.isMC:
        app.mcProgress += 25 * app.focus
        app.isCT = False
    increaseTime(app, 1)


#tester
def onKeyPress(app, key):
    if key =='t':
        increaseTime(app, 1)
    if key == 'r':
        reset(app)
    if key == 'h':
        decreaseHealth(app, 1) 
        decreaseHygiene(app, 1) 

def main():
    runApp()

main()
