#################################################
# Matrix Calculator.py
#
# Your name: Nanditha Niranjan
#################################################

from cmu_112_graphics import *
import random

def appStarted(app):
    app.dim = (0,0)
    app.waitingForFirstKeyPress = True
    app.bH = 60 #button Heigh
    app.bW = 120 #button Width
    app.matrixDim = [0, 0, 0, 0]
    app.isAdd = False
    app.isSubtract = False
    app.isTranspose = False
    app.isScalar = False
    app.isMult = False
    app.isDet = False
    app.waitingMousePressed = True
    app.enterMatrixValues = False
    app.matrixList1 = [[]]
    app.matrixList2 = [[]]
    app.canEnterVal = False
    app.currentCell = None
    app.currentCell2 = None
    app.txt = ""
    app.clicked = False
    app.clicked2 = False
    createList = (app, 0, 0)
    createListAndDict(app, 0, 0)
    app.boxWidth = 45
    app.boxHeight = 30
    app.textEntered = False
    app.tupleDict = {}
    app.tupleDict2 = {}
    app.solutionMatrix = [[]]
    app.solutionNum = 0
    app.done = False
    app.hint = False

def askRowsCols1Matrix(app, canvas):
    if(len(app.matrixDim) >= 1):
        rtxt = str(app.matrixDim[0])
    else:
        rtxt = ""
    if(len(app.matrixDim) >= 2):
        ctxt = str(app.matrixDim[1])
    else:
        ctxt = ""  
    if(len(app.matrixDim) >= 3):
        stxt = str(app.matrixDim[2])
    else:
        stxt = ""
    
    canvas.create_text(app.width/2, 15,
                        text='Enter the number of rows in this matrix: ' + rtxt,
                        font='Arial 14')

    canvas.create_text(app.width/2, 35,
                        text='Enter the number of columns in this matrix: ' 
                        + ctxt, font='Arial 14') 

    if(app.isScalar):
        canvas.create_text(app.width/2, 55,
                        text='Enter the number to multiply the matrix by: ' 
                        + stxt, font='Arial 14') 

def askRowsCols2Matrices(app, canvas):
    if(len(app.matrixDim) >= 1):
        r1txt = str(app.matrixDim[0])
    else:
        r1txt = ""
    if(len(app.matrixDim) >= 2):
        c1txt = str(app.matrixDim[1])
    else:
        c1txt = ""  
    if(len(app.matrixDim) >= 3):
        r2txt = str(app.matrixDim[2])
    else:
        r2txt = ""
    if(len(app.matrixDim) >= 4):
        c2txt = str(app.matrixDim[3])
    else:
        c2txt = ""

    canvas.create_text(app.width/2, 15,
                        text='Enter the number of rows in matrix 1: ' + r1txt,
                        font='Arial 14')

    canvas.create_text(app.width/2, 35,
                        text='Enter the number of columns in matrix 1: ' 
                        + c1txt, font='Arial 14') 

    canvas.create_text(app.width/2, 65,
                        text='Enter the number of rows in matrix 2: ' + r2txt,
                        font='Arial 14')

    canvas.create_text(app.width/2, 85,
                        text='Enter the number of columns in matrix 2: ' 
                        + c2txt, font='Arial 14') 
  
def mousePressed(app, event):
    app.click = (event.x, event.y)
    if(app.width/3 - app.bW/2 < event.x < app.width/3 + app.bW/2):
        if(app.height/5 - app.bH/2 < event.y < app.height/5 + app.bH/2):
            app.isAdd = True
            app.waitingMousePressed = False
    
    if(2*app.width/3 - app.bW/2 < event.x < 2*app.width/3 + app.bW/2):
        if(app.height/5 - app.bH/2 < event.y < app.height/5 + app.bH/2):  
            app.isSubtract = True
            app.waitingMousePressed = False
    
    if(app.width/3 - app.bW/2 < event.x < app.width/3 + app.bW/2):
        if(2*app.height/5 - app.bH/2 < event.y< 2*app.height/5 + app.bH/2):
            app.isTranspose = True
            app.waitingMousePressed = False

    if(2*app.width/3 - app.bW/2 < event.x < 2*app.width/3 + app.bW/2):
        if(2*app.height/5 - app.bH/2 < event.y< 2*app.height/5 + app.bH/2):  
            app.isScalar = True
            app.waitingMousePressed = False
    
    if(app.width/3 - app.bW/2 < event.x < app.width/3 + app.bW/2):
        if(3*app.height/5 - app.bH/2 < event.y< 3*app.height/5 + app.bH/2):
            app.isMult = True
            app.waitingMousePressed = False

    if(2*app.width/3 - app.bW/2 < event.x < 2*app.width/3 + app.bW/2):
        if(3*app.height/5 - app.bH/2 < event.y < 3*app.height/5 + app.bH/2):  
            app.isDet = True
            app.waitingMousePressed = False
    
    if(app.canEnterVal):
        bottomBound = 110
        for rows in range(app.matrixDim[0]):
            leftBound = 0
            rightBound = 0
            topBound = bottomBound + 5
            bottomBound = topBound + app.boxHeight
            for cols in range(app.matrixDim[1]):
                leftBound = rightBound + 5
                rightBound = leftBound + app.boxWidth
                if(leftBound <=event.x<= rightBound):
                    if (topBound <=event.y<= bottomBound):
                        app.currentCell = (rows, cols)
                        app.clicked = True
    
    if(app.canEnterVal and app.matrixDim[2]!=0 and app.matrixDim[3]!=0):
        bottomBound = 110
        for rows in range(app.matrixDim[2]):
            leftBound = 50*(app.matrixDim[1]) + 40
            rightBound = 50*(app.matrixDim[1]) + 40
            topBound = bottomBound + 5
            bottomBound = topBound + app.boxHeight
            for cols in range(app.matrixDim[3]):
                leftBound = rightBound + 5
                rightBound = leftBound + app.boxWidth
                if(leftBound <=event.x<= rightBound):
                    if (topBound <=event.y<= bottomBound):
                        app.currentCell2 = (rows, cols)
                        app.clicked2 = True
    
    if(app.canEnterVal):
        if(140 + app.matrixDim[0]*(app.boxHeight + 5)<=event.y<=170 + app.matrixDim[0]*(app.boxHeight + 5)  and (10<=event.x<=90 or 110<=event.x<=190)):
            if(app.isAdd):
                app.solutionMatrix = createList(app, app.matrixDim[0], app.matrixDim[1])
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        app.solutionMatrix[row][col] = app.matrixList1[row][col] + app.matrixList2[row][col]
                print("*******")
                print(app.solutionMatrix)
                if(10<=event.x<=90):
                    app.done = True
                if(110<=event.x<=190):
                    app.hint = True

            if(app.isSubtract):
                app.solutionMatrix = createList(app, app.matrixDim[0], app.matrixDim[1])
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        app.solutionMatrix[row][col] = app.matrixList1[row][col] - app.matrixList2[row][col]
                print("*******")
                print(app.solutionMatrix)
                if(10<=event.x<=90):
                    app.done = True
                if(110<=event.x<=190):
                    app.hint = True

            if(app.isTranspose):
                app.solutionMatrix = createList(app, app.matrixDim[1], app.matrixDim[0])
                for row in range(app.matrixDim[1]):
                    for col in range(app.matrixDim[0]):
                        app.solutionMatrix[row][col] = app.matrixList1[col][row]
                print("*******")
                print(app.solutionMatrix)
                if(10<=event.x<=90):
                    app.done = True
                if(110<=event.x<=190):
                    app.hint = True

            elif(app.isScalar):
                app.solutionMatrix = createList(app, app.matrixDim[0], app.matrixDim[1])
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        app.solutionMatrix[row][col] = app.matrixList1[row][col] * app.matrixDim[2]
                print("*******")
                print(app.solutionMatrix)
                if(10<=event.x<=90):
                    app.done = True
                if(110<=event.x<=190):
                    app.hint = True

            elif(app.isMult):
                app.solutionMatrix = createList(app, app.matrixDim[0], app.matrixDim[3])
                print("$$$$$$$")
                print(app.solutionMatrix)
                print("$$$$$$$")
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[3]):
                        for row1 in range(app.matrixDim[2]):
                            app.solutionMatrix[row][col] += app.matrixList1[row][row1] * app.matrixList2[row1][col]
                print("*******")
                print(app.solutionMatrix)
                if(10<=event.x<=90):
                    app.done = True
                if(110<=event.x<=190):
                    app.hint = True

            elif(app.isDet):
                
                app.solutionNum = calculateDeterminant2(app.matrixList1)
                print(app.solutionNum)
                
                if(10<=event.x<=90):
                    app.done = True
                if(110<=event.x<=190):
                    app.hint = True
            

def keyPressed(app, event):
    if(app.isAdd == True or app.isSubtract == True):
        if(app.matrixDim[0] == 0):
            app.matrixDim[0] = int(event.key)
        elif(app.matrixDim[1] == 0):
            app.matrixDim[1] = int(event.key)
            app.matrixList1 = createListAndDict(app, app.matrixDim[0], app.matrixDim[1])

        elif(app.matrixDim[2] == 0):
            app.matrixDim[2] = int(event.key)
        elif(app.matrixDim[3] == 0):
            app.matrixDim[3] = int(event.key)
            app.matrixList2 = createListAndDict(app, app.matrixDim[2], app.matrixDim[3])

        app.canEnterVal = True

        app.isTranspose = False
        app.isScalar = False
        app.isMult = False
        app.isDet = False
    
    elif(app.isMult == True):
        if(app.matrixDim[0] == 0):
            app.matrixDim[0] = int(event.key)
        elif(app.matrixDim[1] == 0):
            app.matrixDim[1] = int(event.key)
            app.matrixList1 = createListAndDict(app, app.matrixDim[0], app.matrixDim[1])

        elif(app.matrixDim[2] == 0):
            app.matrixDim[2] = int(event.key)
        elif(app.matrixDim[3] == 0):
            app.matrixDim[3] = int(event.key)
            app.matrixList2 = createListAndDict(app, app.matrixDim[2], app.matrixDim[3])

        app.canEnterVal = True

        app.isAdd = False
        app.isSubtract = False
        app.isTranspose = False
        app.isScalar = False
        app.isDet = False

    elif(app.isTranspose == True):
        if(app.matrixDim[0] == 0):
            app.matrixDim[0] = int(event.key)
        elif(app.matrixDim[1] == 0):
            app.matrixDim[1] = int(event.key)
            app.matrixList1 = createListAndDict(app, app.matrixDim[0], app.matrixDim[1])

        app.canEnterVal = True

        app.isAdd = False
        app.isSubtract = False
        app.isScalar = False
        app.isMult = False
    
    elif(app.isDet == True ):
        if(app.matrixDim[0] == 0):
            app.matrixDim[0] = int(event.key)
        elif(app.matrixDim[1] == 0):
            app.matrixDim[1] = int(event.key)
            app.matrixList1 = createListAndDict(app, app.matrixDim[0], app.matrixDim[1])

        app.canEnterVal = True

        app.isAdd = False
        app.isSubtract = False
        app.isScalar = False
        app.isMult = False

    elif(app.isScalar == True):
        if(app.matrixDim[0] == 0):
            app.matrixDim[0] = int(event.key)
        elif(app.matrixDim[1] == 0):
            app.matrixDim[1] = int(event.key)
            app.matrixList1 = createListAndDict(app, app.matrixDim[0], app.matrixDim[1])
        elif(app.matrixDim[2] == 0):
            app.matrixDim[2] = int(event.key)
        
        app.canEnterVal = True

        app.isAdd = False
        app.isSubtract = False
        app.isTranspose = False
        app.isMult = False
        app.isDet = False

    if(app.canEnterVal and app.clicked):

        app.matrixList1[app.currentCell[0]][app.currentCell[1]] = int(event.key)
        app.tupleDict[(app.currentCell[0], app.currentCell[1])] = True
        print(app.matrixList1)
        print("---------------")
        app.txt = event.key

    if(app.canEnterVal and app.clicked2):
        app.matrixList2[app.currentCell2[0]][app.currentCell2[1]] = int(event.key)
        app.tupleDict2[(app.currentCell2[0], app.currentCell2[1])] = True
        print(app.matrixList2)
        app.txt = event.key

    app.clicked = False
    app.clicked2 = False
    

    # elif (event.key == 's'):
        # this was only here for debugging, before we turned on the timer
        # takeStep(app)

def timerFired(app):
    pass

def additionOrSubtraction(app, canvas):

    if(app.isAdd or app.isSubtract):
        askRowsCols2Matrices(app, canvas)
        if(app.matrixDim[0] != app.matrixDim[2] and app.matrixDim[2] != 0):
            canvas.create_text(app.width/2, app.height-40,
                                text = 'Cannot have different number of rows!',
                                font = 'Arial 20 bold')
        if(app.matrixDim[1] != app.matrixDim[3] and app.matrixDim[3] != 0):
            canvas.create_text(app.width/2, app.height-20,
                                text='Cannot have different number of columns!',
                                font = 'Arial 20 bold')

        if(app.done or app.hint):
            canvas.create_text(50, 190 + app.matrixDim[0]*(app.boxHeight + 5),
                                text = "SOLUTION:",
                                font = 'Arial 16 bold' )
            
            if(app.isAdd):
                x = 10
                y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)

                        canvas.create_text(x+app.boxWidth/2 - 10, y+app.boxHeight/2 + 2,
                                                text = app.matrixList1[row][col],
                                                fill = 'blue',
                                                font = 'Arial 12' )

                        canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                                text = '+',
                                                font = 'Arial 12' )

                        canvas.create_text(x+app.boxWidth/2 + 10, y+app.boxHeight/2 + 2,
                                                text = app.matrixList2[row][col],
                                                fill = 'red',
                                                font = 'Arial 12' )

                        x = x+50
                    x = 10
                    y = y+35

            if(app.isSubtract):
                x = 10
                y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)

                        canvas.create_text(x+app.boxWidth/2 - 10, y+app.boxHeight/2 + 2,
                                                text = app.matrixList1[row][col],
                                                fill = 'blue',
                                                font = 'Arial 12' )

                        canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                                text = '-',
                                                font = 'Arial 12' )

                        canvas.create_text(x+app.boxWidth/2 + 10, y+app.boxHeight/2 + 2,
                                                text = app.matrixList2[row][col],
                                                fill = 'red',
                                                font = 'Arial 12' )

                        x = x+50
                    x = 10
                    y = y+35

            if(app.done):
                canvas.create_text(30 + (app.boxWidth+5)*(app.matrixDim[1]),
                                210 + app.matrixDim[0]*(app.boxHeight + 5)*1.5,
                                text = '=',
                                font = 'Arial 20 bold' )
            
            
                x = 50 + (app.boxWidth+5)*(app.matrixDim[1])
                y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)
                        canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                                text = app.solutionMatrix[row][col],
                                                font = 'Arial 12' )
                        x = x+50
                    x = 50 + (app.boxWidth+5)*(app.matrixDim[1])
                    y = y+35

def transpose(app, canvas):
    if(app.isTranspose):
        askRowsCols1Matrix(app, canvas)
        if(app.done):
            canvas.create_text(50, 190 + app.matrixDim[1]*(app.boxWidth + 5),
                                text = "SOLUTION:",
                                font = 'Arial 16 bold' )
            x = 10
            y = 210 + app.matrixDim[1]*(app.boxWidth + 5)
            for row in range(app.matrixDim[1]):
                for col in range(app.matrixDim[0]):
                    canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)
                    canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                            text = app.solutionMatrix[row][col],
                                            font = 'Arial 12' )
                    x = x+50
                x = 10
                y = y+35

def scalarMultiplication(app, canvas):
    if(app.isScalar):
        askRowsCols1Matrix(app, canvas)
        if(app.done or app.hint):
            canvas.create_text(50, 190 + app.matrixDim[0]*(app.boxHeight + 5),
                                text = "SOLUTION:",
                                font = 'Arial 16 bold' )

            x = 10
            y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
            for row in range(app.matrixDim[0]):
                for col in range(app.matrixDim[1]):
                    canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)

                    canvas.create_text(x+app.boxWidth/2 - 10, y+app.boxHeight/2 + 2,
                                            text = app.matrixList1[row][col],
                                            fill = 'blue',
                                            font = 'Arial 12' )

                    canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                            text = 'x',
                                            font = 'Arial 10' )

                    canvas.create_text(x+app.boxWidth/2 + 10, y+app.boxHeight/2 + 2,
                                            text = app.matrixDim[2],
                                            fill = 'red',
                                            font = 'Arial 12' )

                    x = x+50
                x = 10
                y = y+35
            
            if(app.done):
                canvas.create_text(30 + (app.boxWidth+5)*(app.matrixDim[1]),
                                    210 + app.matrixDim[0]*(app.boxHeight + 5)*1.5,
                                    text = '=',
                                    font = 'Arial 20 bold' )
                    
                x = 50 + (app.boxWidth+5)*(app.matrixDim[1])
                y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[1]):
                        canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)
                        canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                                text = app.solutionMatrix[row][col],
                                                font = 'Arial 12' )
                        x = x+50
                    x = 50 + (app.boxWidth+5)*(app.matrixDim[1])
                    y = y+35

def matrixMultiplication(app, canvas):
    if(app.isMult):
        askRowsCols2Matrices(app, canvas)
        if(app.matrixDim[1] != app.matrixDim[2] and app.matrixDim[2]!=0):
            canvas.create_text(app.width/2, app.height-20,
                                text='Cannot have different number of columns and rows!',
                                font = 'Arial 20 bold')
        if(app.done or app.hint):
            canvas.create_text(50, 190 + app.matrixDim[0]*(app.boxHeight + 5),
                                text = "SOLUTION:",
                                font = 'Arial 16 bold' )

            x = 10
            y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
            numLoc = -50
            multLoc = -40
            num2Loc = -30
            plusLoc = -20
            #app.solutionMatrix[row][col] += app.matrixList1[row][row1] * app.matrixList2[row1][col]
            for row in range(app.matrixDim[0]):
                for col in range(app.matrixDim[3]):
                    canvas.create_rectangle(x, y, x+(app.boxWidth*3), y+app.boxHeight)
                    for row1 in range(app.matrixDim[2]):
                        canvas.create_text(x+app.boxWidth*3/2+numLoc, y+app.boxHeight/2 + 2,
                                        text = app.matrixList1[row][row1],
                                        fill = 'blue',
                                        font = 'Arial 12' )
                        canvas.create_text(x+app.boxWidth*3/2+multLoc, y+app.boxHeight/2 + 2,
                                            text = 'x',
                                            font = 'Arial 10' )
                        canvas.create_text(x+app.boxWidth*3/2+num2Loc, y+app.boxHeight/2 + 2,
                                            text = app.matrixList2[row1][col],
                                            fill = 'red',
                                            font = 'Arial 12' )
                        numLoc += 40
                        multLoc += 40
                        num2Loc += 40

                    for row1 in range(app.matrixDim[2] - 1):
                        canvas.create_text(x+app.boxWidth*3/2+plusLoc, y+app.boxHeight/2 + 2,
                                        text = '+',
                                        font = 'Arial 12' )
                        
                        plusLoc += 40
                    
                    numLoc = -50
                    multLoc = -40
                    num2Loc = -30
                    plusLoc = -20

                    x = x+5 + (app.boxWidth*3)
                y = y+35
                x=10
            
            if(app.done):
                canvas.create_text(30 + (app.boxWidth*3+5)*(app.matrixDim[3]),
                                    210 + app.matrixDim[0]*(app.boxHeight + 5)*1.5,
                                    text = '=',
                                    font = 'Arial 20 bold' )

                x = 50 + (app.boxWidth * 3 +5)*(app.matrixDim[3])
                y = 210 + app.matrixDim[0]*(app.boxHeight + 5)
                for row in range(app.matrixDim[0]):
                    for col in range(app.matrixDim[3]):
                        print(row, col)
                        canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)
                        canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                                text = app.solutionMatrix[row][col],
                                                font = 'Arial 12' )
                        x = x+50
                    x = 50 + (app.boxWidth * 3 +5)*(app.matrixDim[3])
                    y = y+35

#https://stackoverflow.com/questions/3819500/code-to-solve-determinant-using-python-without-using-scipy-linalg-det

def calculateDeterminant2(matrix):
    determinant = 0
    for col in range(len(matrix[0]) - 1):
        row = col + 1 
        if(matrix[row][col] != 0):
            multiple = matrix[row][col]/matrix[row - 1][col]

            for column in range(col+1, len(matrix[0])):
                matrix[row][column] -=  multiple * matrix[row - 1][column]
    
        matrix[row][col] = 0  

    for i in range(len(matrix) - 1):
        determinant += matrix[i][i] * matrix[i+1][i+1]
        return determinant

def determinant(app, canvas):
    if(app.isDet):
        askRowsCols1Matrix(app, canvas)
        if(app.matrixDim[0] != app.matrixDim[1] and app.matrixDim[1] != 0):
            canvas.create_text(app.width/2, app.height-40,
                                text = 'Cannot have different number of rows and columns!',
                                font = 'Arial 20 bold')
        
        if(app.done):
            canvas.create_text(80, 190 + app.matrixDim[0]*(app.boxHeight + 5),
                                text = "SOLUTION: " + str(round(app.solutionNum, 2)),
                                font = 'Arial 16 bold' )

def drawBoard(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='white')

def drawButtons(app, canvas):
    #Addition
    canvas.create_oval(app.width/3 - app.bW/2, app.height/5 - app.bH/2,
                        app.width/3 + app.bW/2, app.height/5 + app.bH/2, 
                        fill='blue')
    canvas.create_text(app.width/3, app.height/5,
                        text='Addition',
                        font='Arial 12 bold')

    #Subtraction
    canvas.create_oval(2*app.width/3 - app.bW/2, app.height/5 - app.bH/2,
                        2*app.width/3 + app.bW/2, app.height/5 + app.bH/2, 
                        fill='red')
    canvas.create_text(2*app.width/3, app.height/5,
                        text='Subtraction',
                        font='Arial 12 bold')

    #Transpose
    canvas.create_oval(app.width/3 - app.bW/2, 2*app.height/5 - app.bH/2,
                        app.width/3 + app.bW/2, 2*app.height/5 + app.bH/2, 
                        fill='green')
    canvas.create_text(app.width/3, 2*app.height/5,
                        text='Transpose',
                        font='Arial 12 bold')

    #Scalar Multiplication
    canvas.create_oval(2*app.width/3 - app.bW/2, 2*app.height/5 - app.bH/2,
                        2*app.width/3 + app.bW/2, 2*app.height/5 + app.bH/2, 
                        fill='orange')
    canvas.create_text(2*app.width/3, 2*app.height/5,
                        text='Scalar Multiplication',
                        font='Arial 12 bold')

    #Matrix Multiplication
    canvas.create_oval(app.width/3 - app.bW/2, 3*app.height/5 - app.bH/2,
                        app.width/3 + app.bW/2, 3*app.height/5 + app.bH/2, 
                        fill='purple')
    canvas.create_text(app.width/3, 3*app.height/5,
                        text='Matrix Multiplication',
                        font='Arial 12 bold')

    #Determinant
    canvas.create_oval(2*app.width/3 - app.bW/2, 3*app.height/5 - app.bH/2,
                        2*app.width/3 + app.bW/2, 3*app.height/5 + app.bH/2, 
                        fill='aqua')
    canvas.create_text(2*app.width/3, 3*app.height/5,
                        text='Determinant',
                        font='Arial 12 bold')

def drawDone(app, canvas):
    canvas.create_rectangle(10, 140 + app.matrixDim[0]*(app.boxHeight + 5), 90,
                             170 + app.matrixDim[0]*(app.boxHeight + 5), 
                            fill='light blue')
    canvas.create_text(50, 155 + app.matrixDim[0]*(app.boxHeight + 5),
                        text = 'Done!', font = 'Arial 18')

def drawHint(app, canvas):
    canvas.create_rectangle(110, 140 + app.matrixDim[0]*(app.boxHeight + 5), 190,
                             170 + app.matrixDim[0]*(app.boxHeight + 5), 
                            fill='purple')
    canvas.create_text(150, 155 + app.matrixDim[0]*(app.boxHeight + 5),
                        text = 'Hint?', font = 'Arial 18')


def drawMatrix(app, canvas):
    x = 10
    y = 120
    for row in range(app.matrixDim[0]):
        for col in range(app.matrixDim[1]):
            canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)
            #check if it is the cell the user clicked on/enter the val and show thats where they are typing and youd store them in the 
            if(app.currentCell == (row, col)):
                canvas.create_text(x+23, y+6,
                                    text = 'Enter:',
                                    font = 'Arial 9' )

            if(app.tupleDict[(row, col)] == True):
                canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                    text = round(app.matrixList1[row][col],2),
                                    fill = 'blue',
                                    font = 'Arial 12' )
            x = x+50
        x = 10
        y = y+35

    if(app.matrixDim[2]!= 0 and app.matrixDim[3]!= 0):
        x = 50*(app.matrixDim[1]) + 40 #40 = 10+30
        y = 120
        for row in range(app.matrixDim[2]):
            for col in range(app.matrixDim[3]):
                canvas.create_rectangle(x, y, x+app.boxWidth, y+app.boxHeight)

                if(app.currentCell2 == (row,col)):
                    canvas.create_text(x+23, y+6,
                                        text = 'Enter:',
                                        font = 'Arial 9' )
                
                if(app.tupleDict2[(row, col)] == True):
                    canvas.create_text(x+app.boxWidth/2, y+app.boxHeight/2 + 2,
                                        text = app.matrixList2[row][col],
                                        fill = 'red',
                                        font = 'Arial 12' )

                x = x+50
            x = 50*(app.matrixDim[1]) + 40
            y = y+35
    
def createList(app, rows, cols):
    matrixList = [([0]*cols) for row in range(rows)]
    return matrixList
    
def createListAndDict(app, rows, cols):
    matrixList = [([0]*cols) for row in range(rows)]
    for row in range(app.matrixDim[0]):
        for col in range(app.matrixDim[1]):
            app.tupleDict[(row, col)] = False
    for row in range(app.matrixDim[2]):
        for col in range(app.matrixDim[3]):
            app.tupleDict2[(row, col)] = False
    return matrixList


def enterValues(app, canvas):
    if(app.canEnterValues):
        canvas.create_text(app.width/2, 35,
                        text=app.txt, font='Arial 14') 

def redrawAll(app, canvas):
    if (app.waitingMousePressed):
        canvas.create_text(app.width/2, app.height/12,
                           text='Select an operation!',
                           font='Arial 26 bold')
        drawButtons(app, canvas)
    else:
        drawBoard(app, canvas)
        additionOrSubtraction(app, canvas)
        transpose(app, canvas)
        scalarMultiplication(app, canvas)
        matrixMultiplication(app, canvas)
        determinant(app, canvas)
        drawMatrix(app, canvas)
        drawDone(app, canvas)
        if(app.isAdd or app.isSubtract or app.isScalar or app.isMult):
            drawHint(app, canvas)
        drawMatrix(app, canvas)
runApp(width=1000, height=500)

