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
    app.ended = False

    #text
    app.text1 = ""
    app.text2 = ""
    app.text3 = ""
    app.text4 = ""
    app.text5 = ""
    app.message = "Good morning, Kim Chee! You are a 15112 student and you have your final on Thursday 8 am. Do your best to study for it! Click on Tasks or press T to get started." 
    formatText(app, app.message)

    #studying stuff
    app.isCT = False
    app.isFR = False
    app.isMC = False
    app.ctProgress = 0
    app.frProgress = 0
    app.mcProgress = 0
    app.focus = (app.health / 50 + app.hygiene / 50)/2

    #location

    app.home = 'https://www.cmu.edu/housing/our-communities/housing-images-tours/Donner/Donner%20standard%20double-min.JPG'
    app.lecture = 'https://www.cmu.edu/conferences/images/dh-500x596-min.jpg'
    app.study = 'https://thetartan-assets.s3.amazonaws.com/uploads/31189/original/pillbox_finals_traviswolfe_img_0201.jpg'
    app.bathroom = 'https://www.cmu.edu/housing/our-communities/housing-images-tours/Resnik/Resnik%20suite%20bathroom%20with%20shower-min.JPG'
    app.restaurant = 'https://www.cmu.edu/dining/news/new-images/ABP900x600-min.jpg'
    app.location = app.home

    #kimchee
    app.kimchee = 'https://cdn-icons-png.flaticon.com/128/6518/6518455.png'

    #planner
    app.showPlanner = False
    app.color = 'black'

def formatText(app, str):
    words = str.split()
    # Initialize variables
    output_strings = []
    current_string = ''
    for word in words:
        if len(current_string + word) > 40:
            output_strings.append(current_string.strip())
            current_string = ''
        if current_string:
            current_string += ' '
        current_string += word
    output_strings.append(current_string.strip())
    for num in range(5):
        output_strings.append("")
    app.text1 = output_strings[0].ljust(40)
    app.text2 = output_strings[1].ljust(40)
    app.text3 = output_strings[2].ljust(40)
    app.text4 = output_strings[3].ljust(40)
    app.text5 = output_strings[4].ljust(40)

def redrawAll(app):
    #location
    drawImage(app.location, 0, 0)

    #kimchee
    drawImage(app.kimchee,140,170) #put after app.location

    #tasks
    drawRect(10, 10, 40, 40, fill='blueViolet')
    drawLabel("Tasks", 30, 30, size=12, fill = 'white', bold = True)
    #health
    drawRect(60, 10, 160, 40, fill='black')
    drawRect(60, 10, app.health*1.6, 40, fill='mediumSeaGreen')
    drawLabel('Health', 140, 30, size=20, fill='white', bold=True)
    #hygiene
    drawRect(230, 10, 160, 40, fill='black')
    drawRect(230, 10, app.hygiene*1.6, 40, fill='royalBlue')
    drawLabel('Hygiene', 310, 30, size=20, fill='white', bold=True)

    #textbox
    drawRect(0, 300, 400, 100, fill='lightgrey')
    #time
    #drawRect(10, 300, 40, 40, fill='lightgrey')
    drawLabel(f'{app.displayTime} {app.timePeriod}', 25, 330, size=14, bold = True)

    #date
    #drawRect(10, 350, 40, 40, fill='lightgrey')
    drawLabel(app.date, 25, 360, size=14, bold = True)

    #message
    drawLabel(app.text1, 225, 315, size=14, font = "monospace", bold = True)
    drawLabel(app.text2, 225, 330, size=14, font = "monospace", bold = True)
    drawLabel(app.text3, 225, 345, size=14, font = "monospace", bold = True)
    drawLabel(app.text4, 225, 360, size=14, font = "monospace", bold = True)
    drawLabel(app.text5, 225, 375, size=14, font = "monospace", bold = True)

    #planner
    if app.showPlanner:
        drawRect(60, 60, 330, 230, fill='white')
        drawLabel('Welcome to your Planner!', 230, 70, size=14, font = "monospace", 
                bold=True)
        #checkboxes
        for i in range(6):
            drawRect(70, 90+(i*30), 20, 20, fill=None, border='black')
            drawLabel(str(i), 80, 100+(i*30))
        for i in range(3):
            drawRect(240, 120+(i*30), 20, 20, fill=None, border='black')
            drawLabel(str(i+6), 250, 130+(i*30))

        # drawRect(240, 90, 20, 20, fill=None, border='black')
        # drawRect(240, 120, 20, 20, fill=None, border='black')
        # drawRect(240, 150, 20, 20, fill=None, border='black')
        #tasks
        
        drawLabel('sleep', 115, 100, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('shower', 120, 130, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('get ready', 134, 160, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('breakfast', 134, 190, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('lunch', 115, 220, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('dinner', 120, 250, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('STUDY:', 315, 100, size=16, font = "monospace", bold=True, fill = app.color)
        drawLabel('code-tracing', 315, 130, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('free response', 320, 160, size=14, font = "monospace", bold=True, fill = app.color)
        drawLabel('multiple choice', 325, 190, size=14, font = "monospace", bold=True, fill = app.color)
        

def pointInSquare(app, mouseX, mouseY):
    left = 10 - 30
    top = 10 - 30
    right = 10 + 30
    bottom = 10 + 30
    return(left <= mouseX <= right) and (top <= mouseY <= bottom)

def onMousePress(app, mouseX, mouseY):
    if pointInSquare(app, mouseX, mouseY):
        app.showPlanner = not app.showPlanner

def selectTask(app):
    app.color = 'fireBrick'

def onStep(app):
    formatText(app, app.message)
    app.focus = (app.health / 50 + app.hygiene / 50)/2

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

    if app.date == 'Thur' and app.time == 8:
        ending(app)


def dateChange(app): #helper function
    if app.date == 'Mon':
        app.date = 'Tues'
    elif app.date == 'Tues':
        app.date = 'Wed'
    elif app.date == 'Wed':
        app.date = 'Thur'
    elif app.date == 'Thur':
        app.date == 'Fri'

# def checkTime(app): #helper function
#     if app.date == 'Thur' and app.time >= 8:
#         ending(app)



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
def doEat(app, meal):
    app.location = app.restaurant
    app.message = f'You have eaten {meal}. The food was inedible. This took 1 hour.'
    if app.health >= 75:
        app.health = 100
    else:
        app.health += 25
    decreaseHygiene(app, 1)
    increaseTime(app, 1)
    

def doSleep(app):
    app.location = app.home
    hours = random.randint(6, 10)
    app.message = f"You slept for {hours} hours listening to Mike Taylor ASMR. You dreamed you aced the final. Make that dream a reality!"
    healthgain = 5 * hours
    if app.health + healthgain >= 100:
        app.health = 100
    else:
        app.health += healthgain
    decreaseHygiene(app, hours//4)
    increaseTime(app, hours)
    if (app.date == 'Thur' and app.time > 8) or app.date =='Fri':
        app.message = 'You slept through the exam. You failed. Press r to reset.'
        app.ended = True

def doShower(app):
    app.location = app.bathroom
    app.message = 'You took a shower, and ended up in a cry session. This took 1 hour.'
    if app.hygiene > 70:
        app.hygiene = 100
    else:
        app.hygiene += 30
    decreaseHealth(app, 1)
    increaseTime(app, 1)
    

def doGetReady(app):
    app.location = app.bathroom
    app.message = 'You were getting ready, and realized you had no one to impress. This took 1 hour.'
    if app.hygiene > 75:
            app.hygiene = 100
    else:
            app.hygiene += 10
    decreaseHealth(app, 1)
    increaseTime(app, 1)
    

def doctStudy(app):
    app.location = app.study
    app.message = 'You studied CTs for your 112 exam. You got everything wrong, and your hatred for CTs grows stronger. This took 1 hour.'
    app.ctProgress += 10 * app.focus
    print('ctProgress', app.ctProgress)
    decreaseHealth(app, 1)
    decreaseHygiene(app, 1)
    increaseTime(app, 1)

def dofrStudy(app):
    app.location = app.study
    app.message = 'You studied FRs for your 112 exam. You wonder why you ever took this class. This took 1 hour.'
    app.frProgress += 10 * app.focus
    print('frProgress', app.frProgress)
    decreaseHealth(app, 1)
    decreaseHygiene(app, 1)
    increaseTime(app, 1)

def domcStudy(app):
    app.location = app.study
    app.message = 'You studied MCs for your 112 exam. Your notes were illegible and you spent 1 hour trying to understand them.'
    app.mcProgress += 10 * app.focus
    print('mcProgress', app.mcProgress)
    decreaseHealth(app, 1)
    decreaseHygiene(app, 1)
    increaseTime(app, 1)

def ending(app):
    app.ended = True
    app.location = app.lecture
    if app.health < 10:
        app.message = 'You died of lack of hunger/sleep. You missed your final too.'
    elif app.hygiene < 10:
        app.message = 'You smelled so bad that everyone fainted. The final got cancelled.'
    else:
        score = (app.ctProgress + app.frProgress + app.mcProgress) // 3
        print(score)
        if score >= 100:
            app.message = 'You got a perfect score and ascended to the level of Mike Taylor'
        elif score >= 90:
            app.message = 'You got an A. Good Job!'
        elif score >= 80:
            app.message = 'You got a B. Nice!'
        elif score >= 70:
            app.message = 'You got a C. Ehhhhh...'
        elif score >= 60:
            app.message = 'You got a D. Better luck next time.'
        else:
            app.message = 'You failed. You made Mike Taylor sad.'
    app.message += ' Press r to reset.'
#tester
def onKeyPress(app, key):
    if key =='t':
        app.showPlanner = not app.showPlanner
    if key == 'r':
        reset(app)
    if app.showPlanner and not app.ended:
        if key == '2':
            app.showPlanner = not app.showPlanner
            doGetReady(app)
        if key == '1':
            app.showPlanner = not app.showPlanner
            doShower(app)
        if key == '6':
            app.showPlanner = not app.showPlanner
            doctStudy(app)
        if key == '7':
            app.showPlanner = not app.showPlanner
            dofrStudy(app)
        if key == '8':
            app.showPlanner = not app.showPlanner
            domcStudy(app)
        if key == '3':
            app.showPlanner = not app.showPlanner
            doEat(app, 'breakfast')
        if key == '4':
            app.showPlanner = not app.showPlanner
            doEat(app, 'lunch')
        if key == '5':
            app.showPlanner = not app.showPlanner
            doEat(app, 'dinner')
        if key == '0':
            app.showPlanner = not app.showPlanner
            doSleep(app)

def main():
    runApp()

main()
