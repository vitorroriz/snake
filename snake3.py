import arcade
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

class Snake:
  def __init__(self, px, py, change_x=0, change_y=0):
    self.body = []
    self.body.append(Piece(px, py))
    self.ghost_tail = Piece(px, py)
    self.change_x = 0;
    self.change_y = 0;

  def head(self):
    return self.body[0]

  def eat(self, food):
    self.body.append(Piece(self.ghost_tail.px, self.ghost_tail.py))
    self.body[-1].prev_p = self.body[-2]
    self.body[-2].next_p = self.body[-1]
    del food
 
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
    if(self.head().px < 0 or self.head().px > MAPSZ_X or self.head().py < 0 or self.head().py > MAPSZ_Y):
      return 0
    else:
      return 1
  def die(self):
    print("Game over!")

  def update(self):
    #move the snake
    self.__follow_head()
    self.head().px += self.change_x
    self.head().py += self.change_y

  def checkout(self):
    if(self.is_out_of_map()):
      self.die()

class Game(arcade.Window):
  def __init__(self, width, height, title, px=5, py=5):
    #call the parent class init
    super().__init__(width, height, title)
    self.set_mouse_visible(False)
    #create our snake
    self.snake = Snake(px, py)
    #@todo: add random px, py
    self.food = Unit(3, 3)

  def on_draw(self):
    arcade.start_render()
    self.snake.draw()

  def update(self, delta_time):
    self.snake.update()
    if(self.snake.head().px == self.food.px and self.snake.head().py == self.food.py):
      self.snake.eat(self.food)

  def get_food(self):
   return self.food


def main():
  window = Game(20, 20, "Snake")
  arcade.run()
#  mygame = Game(5, 5)
#  food1 = Unit(5,6)
#  food2 = Unit(5,9)
#
#  mygame.food = food1
#  mygame.snake.dump_body() 
#  mygame.snake.go_up()
#  mygame.checkout()
#  mygame.snake.dump_body() 
#  mygame.snake.go_up()
#  mygame.snake.dump_body() 
#  mygame.snake.go_up()
#  mygame.snake.dump_body() 
#  mygame.food = food2
#  mygame.snake.go_up()
#  mygame.checkout()
#  mygame.snake.dump_body() 
#  mygame.snake.go_up()
#  mygame.snake.dump_body() 
#  mygame.snake.go_up()
#  mygame.snake.dump_body() 
#  print("right")
#  mygame.snake.go_right()
#  mygame.snake.dump_body() 
#  print("right")
#  mygame.snake.go_right()
#  mygame.snake.dump_body() 
#  print("down")
#  mygame.snake.go_down()
#  mygame.snake.dump_body() 

if __name__ == "__main__":
    main()
