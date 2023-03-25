from cmu_graphics import *

def onAppStart(app):
    reset(app)

def reset(app):
    app.health = 57
    app.hygiene = 43

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
    
    drawRect(10, 350, 40, 40, fill='yellow')
    drawRect(60, 300, 330, 90, fill='cyan')
    drawRect(10, 300, 40, 40, fill='lightgreen')
    
    drawLabel('8 am', 30, 320, size=12)
    drawLabel('Tues', 30, 370, size=12)
    drawLabel('Insert text here...', 225, 345, size=12)

def onKeyPress(app, key):
    pass

def main():
    runApp()

main()
