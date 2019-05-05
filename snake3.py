import arcade
import random
from enum import Enum

SWIDTH  = 300 #square width
SHEIGHT = 300 #square height
RWIDTH  = 20  #square width
RHEIGHT = 20  #square height
MAPSZ_Y = 20
MAPSZ_X = 20

class Unit:
  def __init__(self, px=0, py=0):
    self.px = px
    self.py = py

class Piece(Unit):
  def __init__(self, px, py):
    self.px = px
    self.py = py
    self.next_p =  self
    self.prev_p =  self

  def draw(self, color):
    idx = self.px
    idy = self.py
    arcade.draw_rectangle_filled(idx*RWIDTH + RWIDTH/2, idy*RHEIGHT + RHEIGHT/2, RWIDTH, RHEIGHT, color)
    arcade.draw_rectangle_outline(idx*RWIDTH + RWIDTH/2, idy*RHEIGHT + RHEIGHT/2, RWIDTH, RHEIGHT, arcade.color.AMAZON)

  def respawn(self, px, py):
    arcade.draw_rectangle_filled(self.px*RWIDTH + RWIDTH/2, self.py*RHEIGHT + RHEIGHT/2, RWIDTH, RHEIGHT, arcade.color.BLACK)
    arcade.draw_rectangle_outline(self.px*RWIDTH + RWIDTH/2, self.py*RHEIGHT + RHEIGHT/2, RWIDTH, RHEIGHT, arcade.color.WHITE)
    self.px = px
    self.py = py

class Direction(Enum):
  stop  = 0
  up    = 1
  right = 2
  down  = 3
  left  = 4

class Snake:
  def __init__(self, px, py, change_x=0, change_y=0):
    self.body = []
    self.body.append(Piece(px, py))
    self.ghost_tail = Piece(px, py)
    self.change_x = 0;
    self.change_y = 0;
    self.dir = Direction.stop

  def head(self):
    return self.body[0]

  def eat(self, food):
    self.body.append(Piece(self.ghost_tail.px, self.ghost_tail.py))
    self.body[-1].prev_p = self.body[-2]
    self.body[-2].next_p = self.body[-1]
    px = random.randint(0, int(SWIDTH/RWIDTH)-1)
    pyexcl = [piece.py for piece in self.body if piece.px == px]
    pylist = [y for y in range(0, int(SHEIGHT/RHEIGHT)-1) if y not in pyexcl]
    py = random.choice(pylist)
    #py = random.randint(0, int(SHEIGHT/RHEIGHT)-1)
    food.respawn(px, py)
 
  def go_up(self):
    self.__follow_head()
    self.head().py = self.head().py + 1 
    
  def go_down(self):
    self.__follow_head()
    self.head().py = (self.head().py - 1)

  def go_right(self):
    self.__follow_head()
    self.head().px = (self.head().px + 1)

  def go_left(self):
    self.__follow_head()
    self.head().px = (self.head().px - 1)
  
  def __follow_head(self):
    self.ghost_tail.px = self.body[-1].px
    self.ghost_tail.py = self.body[-1].py
    blen = len(self.body)
    for i in range(blen-1):
      self.body[blen-i-1].px = self.body[blen-i-1].prev_p.px
      self.body[blen-i-1].py = self.body[blen-i-1].prev_p.py

  def dump_body(self):
    print("Snake body list (px, py):")
    for piece in self.body:
      print("(" + str(piece.px) + "," + str(piece.py) + ")")

  def is_out_of_map(self):
    if(self.head().px < 0 or self.head().px > int(SWIDTH/RWIDTH) or self.head().py < 0 or self.head().py > int(SHEIGHT/RHEIGHT)):
      return 1
    else:
      return 0
  def had_self_collide(self):
    for idx in range(len(self.body)-1):
      if(self.head().px == self.body[idx+1].px and self.head().py == self.body[idx+1].py):
        return True
    return False

  def update(self):
    #move the snake
    if(self.dir == Direction.up):
      self.go_up()
    elif(self.dir == Direction.down):
      self.go_down()
    elif(self.dir == Direction.left):
      self.go_left()
    elif(self.dir == Direction.right):
      self.go_right()

  def draw(self):
    for piece in self.body:
        piece.draw(arcade.color.WHITE)

class Game(arcade.Window):
  def __init__(self, width, height, title, px=5, py=5):
    #call the parent class init
    super().__init__(width, height, title)
    self.set_mouse_visible(False)
    #create our snake
    self.snake = Snake(px, py)
    #@todo: add random px, py
    px = random.randint(0, int(SWIDTH/RWIDTH)-1)
    py = random.randint(0, int(SHEIGHT/RHEIGHT)-1)
    self.food = Piece(px, py)
    self.score = 0
    #self.set_update_rate(1/20) 

  def on_draw(self):
    arcade.start_render()
    #draw background
    for i in range(int(SWIDTH/RWIDTH)):
        for j in range(int(SHEIGHT/RHEIGHT)):
          arcade.draw_rectangle_outline(i*RWIDTH + RWIDTH/2, j*RHEIGHT + RHEIGHT/2, RWIDTH, RHEIGHT, arcade.color.WHITE)
    #draw snake
    self.snake.draw()
    if(self.food):
      self.food.draw(arcade.color.YELLOW)

  def on_update(self, delta_time):
    if(self.snake.is_out_of_map() or self.snake.had_self_collide()):
      self.game_over()
    self.snake.update()
    if(self.snake.head().px == self.food.px and self.snake.head().py == self.food.py):
      self.snake.eat(self.food)
      self.score_up()

  def get_food(self):
   return self.food

  def on_key_press(self, key, modifiers):
    if key == arcade.key.LEFT:
      self.snake.dir = Direction.left       
    if key == arcade.key.RIGHT:
      self.snake.dir = Direction.right
    if key == arcade.key.UP:
      self.snake.dir = Direction.up
    if key == arcade.key.DOWN:
      self.snake.dir = Direction.down

  def score_up(self):
    self.score += 1

  def game_over(self): 
    print("Game over! :(")
    print("Score: " + str(self.score))
    arcade.close_window()

def main():
  window = Game(SWIDTH, SHEIGHT, "Snake")
  arcade.run()

if __name__ == "__main__":
    main()
