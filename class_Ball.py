import Interface as it
from random import randrange as rnd, choice
import math


class Ball:
    def __init__(self, x, y, vx, vy):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = it.canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30
        self.speedometr = 0

    def set_coords(self):
        it.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.speedometr = (self.vy ** 2 + self.vx ** 2) ** 0.5
        self.x += self.vx
        self.y -= self.vy
        if self.x >= 780:
            self.vx = -(self.vx / 2)
            self.x = 779
        if self.y > 500:
            if self.speedometr > 10:
                self.vy = - (self.vy / 2)
                self.vx = self.vx / 2
                self.y = 499
        if self.y < 500:
            self.vy -= 1.2
            self.vx *= 0.99
        it.canvas.coords(self.id, self.x - self.r, self.y - self.r,
                      self.x + self.r, self.y + self.r)
        

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        target_x_list = list(range((obj.x - obj.r), (obj.x + obj.r)))
        target_y_list = list(range((obj.y - obj.r), (obj.y + obj.r)))
        ball_x_list = list(range(int((self.x - self.r)), int((self.x + self.r))))
        ball_y_list = list(range(int((self.y - self.r)), int((self.y + self.r))))
        if self.r < obj.r:
            if (int(self.x - self.r)) in target_x_list and (int(self.y - self.r)) in target_y_list:
                return True
            elif (int(self.x + self.r)) in target_x_list and (int(self.y + self.r)) in target_y_list:
                return True
        else:
            if (int(obj.x - obj.r)) in ball_x_list and (int(self.y - self.r)) in ball_y_list:
                return True
            elif (int(obj.x + self.r)) in ball_x_list and (int(obj.y + obj.r)) in ball_y_list:
                return True


