from cmu_graphics import *

def onAppStart(app):
    reset(app)

def reset(app):
    app.health = 57
    app.hygiene = 43
    app.time = 8
    app.timePeriod = 'am'
    app.date = 'Mon'
    app.text = 'Insert text here...'

def onStep(app):
    pass

def redrawAll(app):
    drawRect(10, 10, 40, 40, fill='black')
    #health
    drawRect(60, 10, 160, 40, fill='black')
    drawRect(60, 10, app.health*1.6, 40, fill='red')
    #hygiene
    drawRect(230, 10, 160, 40, fill='black')
    drawRect(230, 10, app.hygiene*1.6, 40, fill='green')
    
    #time
    drawRect(10, 300, 40, 40, fill='grey')
    drawLabel(f'{app.time} {app.timePeriod}', 30, 320, size=12)

    #date
    drawRect(10, 350, 40, 40, fill='grey')
    drawLabel(app.date, 30, 370, size=12)

    #time and date
    drawRect(60, 300, 330, 90, fill='grey')
    drawLabel('Insert text here...', 225, 345, size=12)

def onKeyPress(app, key):
    pass

def main():
    runApp()

main()
