"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 30        # 100 frames per second (initial parameter is 10)
NUM_LIVES = 3			# Number of attempts (initial parameter is 3)


def main():
    graphics = BreakoutGraphics()

    # game termination conditions
    counter = NUM_LIVES     # gamer lives
    brick_num = 0           # brick number

    # Add the animation loop here!
    while True:
        if graphics.switch:
            vx = graphics.get_vx()
            vy = graphics.gey_vy()
            graphics.ball.move(vx, vy)

            # if graphics.ball.x < graphics.window.width
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                graphics.rebound_x()
            if graphics.ball.y <= 0:
                graphics.rebound_y()

            # detect the four corner of the ball to make sure whether happens collision or not
            maybe_obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)        # upper left
            maybe_obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                       graphics.ball.y)                         # upper right
            maybe_obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y +
                                                       graphics.ball.width)                     # lower left
            maybe_obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                       graphics.ball.y + graphics.ball.width)   # lower right

            # A switch. If any four corner of the ball contact a object, "detector" will be False
            detector = True
            # A variable to avoid the bug occurred in the middle of the paddle. (keep colliding it up and down)
            optimized_height = graphics.paddle.y - graphics.ball.width + graphics.paddle.height/2

            if maybe_obj1 is not None and detector and graphics.ball.y < optimized_height:
                graphics.rebound_y()
                detector = False
                # print("5")       (analysis used.)
                if maybe_obj1 is not graphics.paddle:
                    graphics.window.remove(maybe_obj1)
                    brick_num += 1
                    # print("1")    (analysis used.)

            if maybe_obj2 is not None and detector and graphics.ball.y < optimized_height:
                graphics.rebound_y()
                detector = False
                if maybe_obj2 is not graphics.paddle:
                    graphics.window.remove(maybe_obj2)
                    brick_num += 1

            if maybe_obj3 is not None and detector and graphics.ball.y < optimized_height:
                graphics.rebound_y()
                detector = False
                if maybe_obj3 is not graphics.paddle:
                    graphics.window.remove(maybe_obj3)
                    brick_num += 1

            if maybe_obj4 is not None and detector and graphics.ball.y < optimized_height:
                graphics.rebound_y()
                detector = False
                if maybe_obj4 is not graphics.paddle:
                    graphics.window.remove(maybe_obj4)
                    brick_num += 1

            # lose one life after the ball fall, and recreate a new ball.
            if graphics.ball.y > graphics.window.height:
                counter -= 1
                graphics.restart_the_game()

        # the termination condition: "no more lives" or "delete all bricks"
        if counter == 0 or brick_num == 100:
            break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
