import Interface as it
from random import randrange as rnd, choice

POINTS = 0
points_desk = it.canvas.create_text(30,30,text = POINTS,font = '28')
class Target():

    def __init__(self):
        global POINTS
        self.live = 1
        self.id = it.canvas.create_oval(0,0,0,0)
        self.new_target()
        self.dx = choice((-5, -4, -3, 3, 4, 5))
        self.dy = choice((self.dx, -(self.dx)))
    
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 770)
        y = self.y = rnd(300, 480)
        r = self.r = rnd(2, 50)
        it.canvas.coords(self.id, x - r, y - r, x + r, y + r)
        it.canvas.itemconfig(self.id, fill = choice(['red', 'orange', 'yellow', 'green', 'blue']))

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global POINTS, points_desk
        it.canvas.coords(self.id, -10, -10, -10, -10)
        POINTS += 1
        it.canvas.itemconfig(points_desk, text=POINTS)

    def movement(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 200:
            self.dx = -self.dx
        if self.y < 200:
            self.dy = -self.dy
        if self.x > 780:
            self.dx = -self.dx
        if self.y > 480:
            self.dy = -self.dy
        it.canvas.coords(self.id, self.x - self.r, self.y - self.r,
                      self.x + self.r, self.y + self.r)
        

