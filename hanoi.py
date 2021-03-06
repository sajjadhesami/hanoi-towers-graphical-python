import color
import random
import stddraw
import sys


def drawDiscs(Sticks, Red, Green, Blue):
    '''
    draws the current state of the discs on the canvas
    :param Sticks: the 2D array of sticks
    :param Red: red color array
    :param Green: green color array
    :param Blue: blue color array
    :return: NoneType
    '''
    PEN_RADIUS = 0.5
    LINE_WIDTH = 2
    h = 0
    for i in range(0, len(Sticks[0])):
        stddraw.setPenRadius(PEN_RADIUS * (0.9 ** Sticks[0][i]))
        stddraw.setPenColor(color.Color(Red[Sticks[0][i]], Green[Sticks[0][i]], Blue[Sticks[0][i]]))

        stddraw.line(3 - (LINE_WIDTH * (0.9 ** Sticks[0][i]) / 2), h, 3 + (LINE_WIDTH * (0.9 ** Sticks[0][i]) / 2), h)
        h += 1.5 * PEN_RADIUS * (0.9 ** Sticks[0][i])

    h = 0
    for i in range(0, len(Sticks[1])):
        stddraw.setPenRadius(PEN_RADIUS * (0.9 ** Sticks[1][i]))
        stddraw.setPenColor(color.Color(Red[Sticks[1][i]], Green[Sticks[1][i]], Blue[Sticks[1][i]]))

        stddraw.line(6 - (LINE_WIDTH * (0.9 ** Sticks[1][i]) / 2), h, 6 + (LINE_WIDTH * (0.9 ** Sticks[1][i]) / 2), h)
        h += 1.5 * PEN_RADIUS * (0.9 ** Sticks[1][i])

    h = 0
    for i in range(0, len(Sticks[2])):
        stddraw.setPenRadius(PEN_RADIUS * (0.9 ** Sticks[2][i]))
        stddraw.setPenColor(color.Color(Red[Sticks[2][i]], Green[Sticks[2][i]], Blue[Sticks[2][i]]))

        stddraw.line(9 - (LINE_WIDTH * (0.9 ** Sticks[2][i]) / 2), h, 9 + (LINE_WIDTH * (0.9 ** Sticks[2][i]) / 2), h)
        h += 1.5 * PEN_RADIUS * (0.9 ** Sticks[2][i])
    stddraw.show(200)


def moves(n, F, H, D, Red, Green, Blue, Sticks):
    '''
    Recursively moves the discs
    :param n: the number of discs to move
    :param F: the id of the stick that the disc will be moved From
    :param H: the id of the Helper stick
    :param D: the id of the Destination stick
    :param Red: red color array
    :param Green: green color array
    :param Blue: blue color array
    :param Sticks: the 2D array of sticks
    :return: NoneType
    '''
    if n == 0:
        return
    moves(n - 1, F, D, H, Red, Green, Blue, Sticks)
    Sticks[D].append(Sticks[F][-1])
    print("from stick #%1d to stick #%1d" % ((F + 1),  (D + 1)))
    del Sticks[F][-1]
    drawSticks()
    drawDiscs(Sticks, Red, Green, Blue)
    moves(n - 1, H, F, D, Red, Green, Blue, Sticks)


def drawSticks():
    '''
    Simply clears the canvas and draws three vertical lines
    :return: NoneTyper
    '''
    stddraw.clear(color.WHITE)
    stddraw.setPenColor(color.BLACK)
    stddraw.setPenRadius(0.01)

    stddraw.line(3, 0, 3, 4)
    stddraw.line(6, 0, 6, 4)
    stddraw.line(9, 0, 9, 4)


def main():
    stddraw.setCanvasSize(1000, 300)
    stddraw.setXscale(0, 12)
    stddraw.setYscale(0, 5)
    if (len(sys.argv)!=2):
        print("Please run the script with correct arguments.")
        print("Example: hanoi.py 5")
    N = int(sys.argv[1])
    Red, Green, Blue = [], [], []

    for i in range(N):
        Red.append(random.randrange(0, 255))
        Green.append(random.randrange(0, 255))
        Blue.append(random.randrange(0, 255))
    Sticks = [[], [], []]
    Sticks[0] = list(range(0, N))
    Sticks[1] = []
    Sticks[2] = []
    drawSticks()
    drawDiscs(Sticks, Red, Green, Blue)
    moves(N, 0, 1, 2, Red, Green, Blue, Sticks)


if __name__ == "__main__":
    main()
