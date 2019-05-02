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
  def __init__(self, px, py):
    self.body = []
    self.body.append(Piece(px, py))
    self.ghost_tail = Piece(px, py)

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

class Game:
   def checkout(self):
     if(self.snake.is_out_of_map()):
         self.snake.die()
     if(self.snake.head().px == self.food.px and self.snake.head().py == self.food.py):
       self.snake.eat(self.food)

   def get_food(self):
     return self.food

   def __init__(self, px=5, py=5):
     self.food = Unit(0, 0)
     self.snake = Snake(px, py)

def game():
  mygame = Game(5, 5)
  food1 = Unit(5,6)
  food2 = Unit(5,9)

  mygame.food = food1
  mygame.snake.dump_body() 
  mygame.snake.go_up()
  mygame.checkout()
  mygame.snake.dump_body() 
  mygame.snake.go_up()
  mygame.snake.dump_body() 
  mygame.snake.go_up()
  mygame.snake.dump_body() 
  mygame.food = food2
  mygame.snake.go_up()
  mygame.checkout()
  mygame.snake.dump_body() 
  mygame.snake.go_up()
  mygame.snake.dump_body() 
  mygame.snake.go_up()
  mygame.snake.dump_body() 
  print("right")
  mygame.snake.go_right()
  mygame.snake.dump_body() 
  print("right")
  mygame.snake.go_right()
  mygame.snake.dump_body() 
  print("down")
  mygame.snake.go_down()
  mygame.snake.dump_body() 

game()
