from tkinter import *
import random

# Global variables used
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True


# Function used for creating prey for the snake
def create_block():
    """ Creates an apple to be eaten """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="red")
# main function to control the game
def main():
    """ Handles game process """
    global IN_GAME
    if IN_GAME:
        s.move()
        #setting the coordinates for the moving snake
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords
        # Checking for the collision with walls of gamefield
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        if x2 > WIDTH or x1 <0 or y1 < 0 or y2 > HEIGHT :
            IN_GAME = False
        # Eating apples
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()
        # Bitting up itself / Self-Eating
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        root.after(100, main)
    # stop game and print message when game overs
    else:
        c.create_text(WIDTH/2, HEIGHT/2,
                      text="GAME OVER!!!",
                      font="Arial 20",
                      fill="red")

# class which determine the snakes formation th roughout the game and segment
class Segment(object):
    """ Single snake segment """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+SEG_SIZE, y+SEG_SIZE,
                                           fill="white")
# class ehich holds functions for determining the mmovement of the snake throughout the game
class Snake(object):
    """ initializing the snakes movement """
    def __init__(self, segments):
        self.segments = segments
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Right"]
        # defination for moving the snake automatically
    def move(self):
        """ Moves the snake with the specified vector"""
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
                 x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)
