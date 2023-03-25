from cmu_graphics import *

def onAppStart(app):
    pass

def onStep(app):
    pass

def redrawAll(app):
    #background
    
    #textbox
    #drawRect()
    #planner
    drawRect(10, 10, 40, 40, fill='black')
    #health bar
    drawRect(60, 10, 160, 40, fill='purple')
    #hygiene bar
    drawRect(230, 10, 160, 40, fill='cyan')

def onKeyPress(app, key):
    pass

def main():
    runApp()

main()