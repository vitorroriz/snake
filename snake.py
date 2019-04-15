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

  def head(self):
    return self.body[0]

  def eat(self, food):
    self.body.insert(0, Piece(food.px, food.py))
    for i in range(len(self.body)-1):
      self.body[i].next_p = self.body[i+1]
      self.body[i+1].prev_p = self.body[i]
    del food
 
  def go_up(self):
    self.__follow_head()
    self.head().py = self.head().py + 1 
    
  def go_down(self):
    self.__follow_head()
    self.head().py = (self.head().py - 1)
    if(self.head().py < 0):
      head().py = 0

  def go_right(self):
    self.__follow_head()
    self.head().px = (self.head().px + 1) % MAPSZ_X

  def go_left(self):
    self.__follow_head()
    self.head().px = (self.head().px - 1)
    if(self.head().px < 0):
      self.head().py = MAPZ_Y 
  
  def __follow_head(self):
    blen = len(self.body)
    for i in range(blen-1):
      self.body[blen-i-1].px = self.body[blen-i-1].prev_p.px
      self.body[blen-i-1].py = self.body[blen-i-1].prev_p.py

  def dump_body(self):
    print "Snake body list (px, py):"
    for piece in self.body:
      print "(" + str(piece.px) + "," + str(piece.py) + "), p: (" + str(piece.prev_p.px) + "," + str(piece.prev_p.py) + ")"

def game():
  abby = Snake(5,5)
  food1 = Unit(5,6)
  food2 = Unit(5,9)

  abby.dump_body() 
  abby.eat(food1)
  abby.dump_body() 
  abby.go_up()
  abby.dump_body() 
  abby.go_up()
  abby.dump_body() 
  abby.eat(food2)
  abby.dump_body() 
  abby.go_up()
  abby.dump_body() 
  abby.go_up()
  abby.dump_body() 
  print "right"
  abby.go_right()
  abby.dump_body() 
  print "right"
  abby.go_right()
  abby.dump_body() 
  print "down"
  abby.go_down()
  abby.dump_body() 

game()
