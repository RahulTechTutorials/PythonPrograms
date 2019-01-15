from turtle import *
def createTriangle(point, color):
    fillcolor(color)
    penup()
    goto(point[0][0],point[0][1])
    pendown()
    begin_fill()
    goto(point[1][0],point[1][1])
    goto(point[2][0],point[2][1])
    goto(point[0][0],point[0][1])
    end_fill()

def mid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2 )

def sierpinski(points,level):
    colormap = ['yellow','blue','brown','white','black','orange','violet']
    createTriangle(points,colormap[level % len(colormap)])
    if level > 0:
        sierpinski([points[0], mid(points[0],points[1]),mid(points[0],points[2])],level-1)
        sierpinski([points[1], mid(points[1],points[0]),mid(points[1],points[2])],level-1)
        sierpinski([points[2], mid(points[2],points[0]),mid(points[2],points[1])],level-1)

def main():
    endpoints = [(-100,-50),(0,100),(100,-50)]
    level = int(input('Enter the number of levels you want: '))
    sierpinski(endpoints,level)
    done()

if __name__ == '__main__':
    main()
    
