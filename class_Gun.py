import class_Ball as cb
import Interface as it
import math

class Gun:
    def __init__(self):
        self.increase_power = 10
        self.clicked_on = 0
        self.angle = 1
        self.id = it.canvas.create_line(20, 450, 50, 420, width=7) # FIXME: don't know how to set it...
        self.x_coord = 20
        self.y_coord = 450
        self.bullet = 0
        self.balls_list = []

    def start_of_fire(self, event):
        self.clicked_on = 1

    def end_of_fire(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        self.bullet += 1
        new_ball = cb.Ball((self.x_coord + max(self.increase_power, 20) * math.cos(self.angle)),\
                           (self.y_coord + max(self.increase_power, 20) * math.sin(self.angle)),\
                           (self.increase_power * math.cos(self.angle)), \
                           (- self.increase_power * math.sin(self.angle)))
        self.balls_list += [new_ball]
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        self.clicked_on = 0
        self.increase_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.clicked_on:
            it.canvas.itemconfig(self.id, fill='orange')
        else:
            it.canvas.itemconfig(self.id, fill='black')
        it.canvas.coords(self.id, self.x_coord, self.y_coord,
                    self.x_coord + max(self.increase_power, 20) * math.cos(self.angle),
                    self.y_coord + max(self.increase_power, 20) * math.sin(self.angle)
                    )

    def power_up(self):
        if self.clicked_on:
            if self.increase_power < 100:
                self.increase_power += 1
            it.canvas.itemconfig(self.id, fill='orange')
        else:
            it.canvas.itemconfig(self.id, fill='black')

