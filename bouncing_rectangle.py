"""
This simple animation example shows how to bounce a rectangle
on the screen.

It assumes a programmer knows how to create functions already.

It does not assume a programmer knows how to create classes. If you do know
how to create classes, see the starting template for a better example:

http://arcade.academy/examples/starting_template.html

Or look through the examples showing how to use Sprites.

A video walk-through of this example is available at:
https://vimeo.com/168063840

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.bouncing_rectangle

"""

import arcade
import snake3
# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Bouncing Rectangle Example"

# Size of the rectangle
RECT_WIDTH = 20 
RECT_HEIGHT = 20 

def draw_piece(piece):
    idx = piece.px
    idy = piece.py
    arcade.draw_rectangle_filled(idx*RECT_WIDTH + RECT_WIDTH/2, idy*RECT_HEIGHT + RECT_HEIGHT/2, RECT_WIDTH, RECT_HEIGHT, arcade.color.WHITE)
    arcade.draw_rectangle_outline(idx*RECT_WIDTH + RECT_WIDTH/2, idy*RECT_HEIGHT + RECT_HEIGHT/2, RECT_WIDTH, RECT_HEIGHT, arcade.color.AMAZON)

def update(snake):
    on_draw(1/80)
    for piece in snake.body:
      draw_piece(piece)
      
def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    """

    # Start the render. This must happen before any drawing
    # commands. We do NOT need a stop render command.
    arcade.start_render()

    # Draw a rectangle.
    # For a full list of colors see:
    # http://arcade.academy/arcade.color.html
    for i in range(int(SCREEN_WIDTH/RECT_WIDTH)):
      for j in range(int(SCREEN_WIDTH/RECT_HEIGHT)):
        #print("(" + str(i*RECT_WIDTH) + "," + str(j*RECT_HEIGHT) + ")");
        arcade.draw_rectangle_outline(i*RECT_WIDTH + RECT_WIDTH/2, j*RECT_HEIGHT + RECT_HEIGHT/2, RECT_WIDTH, RECT_HEIGHT, arcade.color.WHITE)
    
def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    abby = snake3.Snake(10, 10)
    f1 = snake3.Unit(10, 11)
    f2 = snake3.Unit(10, 12)
    f3 = snake3.Unit(10, 13)
    abby.eat(f1)
    abby.eat(f2)
    abby.eat(f3)
    abby.go_right() 
    abby.go_right() 
    abby.go_down() 
    update(abby)
    # Tell the computer to call the draw command at the specified interval.
    #arcade.schedule(update, 1/80)
    arcade.finish_render()
    # Run the program
    arcade.run()


if __name__ == "__main__":
    main()
