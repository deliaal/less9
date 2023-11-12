import ast
import turtle


varInput = ''

verify = False
database = {}

def getAllRecords():
    global database
    with open('db.txt') as data:
        f = data.read()
        database = ast.literal_eval(f)

def getInput():
    global varInput
    varInput =  input('enter a shape')

def verifyShape(shape):
    global verify
    if shape in database.keys():
        print('Shape found')
        verify = True
        return True
    else:
        print('Not found')
        verify = False
        return False

def printShape(isTrue):
    global varInput
    if isTrue:
        if varInput == 'Triangle':
            drawTriangle()
        elif varInput == 'Square':
            drawSquare()
        elif varInput == 'Circle':
            drawCircle()
        elif varInput == 'Pentagon':
            drawPentagon()
        else:
            print('Finish')
    else:
        print('Shape Not Found')


def drawTriangle():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(100)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

def drawSquare():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(100)
        turtle.right(360/laturi)
    turtle.Screen().exitonclick()

def drawCircle():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(1)
        turtle.right(360 / laturi)
    turtle.Screen().exitonclick()
def drawPentagon():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(100)
        turtle.right(360 / laturi)
    turtle.Screen().exitonclick()


if __name__ == '__main__':
    getAllRecords()
    getInput()
    verifyShape(varInput)
    printShape(verify)
