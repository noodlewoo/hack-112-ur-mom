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
    app.atHome = True
    app.atLecture = False
    app.atLibrary = False
    app.home = 'https://www.cmu.edu/housing/our-communities/housing-images-tours/Donner/Donner%20standard%20double-min.JPG'
    app.lecture = 'https://www.cmu.edu/computing/services/teach-learn/tes/classrooms/images/doherty_2210.jpg'
    app.study = 'https://thetartan-assets.s3.amazonaws.com/uploads/31189/original/pillbox_finals_traviswolfe_img_0201.jpg'

def onStep(app):
    pass

def redrawAll(app):
    #backgrounds
    if app.atHome:
        drawImage(app.home, 0, 0)
    if app.atLecture:
        drawImage(app.lecture,0,0)
    if app.atLibrary:
        drawImage(app.study,0,0)
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


