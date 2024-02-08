"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.start_x = (window_width-ball_radius*2)/2       # get the x-coordinates of the initial ball
        self.start_y = (window_height-ball_radius*2)/2      # get the y-coordinates of the initial ball
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.start_x, y=self.start_y)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_ball)

        # turn on the switch to initialize the game
        self.switch = False

        # By using two "for loop" to draw specific amount of bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height, x=(BRICK_WIDTH+BRICK_SPACING)*j,
                                   y=(BRICK_ROWS+BRICK_HEIGHT)*i+BRICK_OFFSET)
                self.brick.filled = True

                # set up the color of the bricks
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'

                elif i == 2 or i == 3:
                    self.brick.fill_color = 'orange'

                elif i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'

                elif i == 6 or i == 7:
                    self.brick.fill_color = 'green'

                elif i == 8 or i == 9:
                    self.brick.fill_color = 'blue'

                self.window.add(self.brick)

    def move_paddle(self, mouse):
        # move the mouse to control paddle
        self.paddle.x = mouse.x - self.paddle.width / 2

        # solve the problem that mouse is out of window.
        if mouse.x <= 0 + self.paddle.width / 2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width

    def start_ball(self, mouse):
        # the velocity of the ball will be set up if the switch be turned on.
        if not self.switch:
            self.switch = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def get_vx(self):
        # give user the velocity for the ball
        return self.__dx

    def gey_vy(self):
        # give user the velocity for the ball
        return self.__dy

    def rebound_y(self):
        # the velocity x for the ball will rebound when it collide with object or walls.
        self.__dy = -self.__dy

    def rebound_x(self):
        # the velocity y for the ball will rebound when it collide with object or walls.
        self.__dx = -self.__dx

    def restart_the_game(self):
        # restart a game and create new object which have the same name "ball".
        self.ball = GOval(self.ball.width, self.ball.height, x=self.start_x, y=self.start_y)
        self.ball.filled = True
        self.window.add(self.ball)
        self.switch = False












