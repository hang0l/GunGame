import math
import time
import class_Gun as cg
import class_Target as ct
import Interface as it


target_list = []
def new_target():
    global target_list
    for i in range(it.KOLICH):
        target = ct.Target()
        target_list.append(target)
gun_examp = cg.Gun()
screen1 = it.canvas.create_text(400, 300, text='', font='28')


def game():
    new_target()
    gun_examp.bullet = 0
    it.canvas.bind('<Button-1>', gun_examp.start_of_fire)
    it.canvas.bind('<ButtonRelease-1>', gun_examp.end_of_fire)
    it.canvas.bind('<Motion>', gun_examp.targetting)
    while target_list or gun_examp.balls_list:
        if it.NEW_GAME == 1:
            for target in target_list:
                it.canvas.delete(target.id)
                target_list.remove(target)
            it.NEW_GAME = 0
            game()
        if target_list:
            for target in target_list:
                target.movement()
                for ball in gun_examp.balls_list:
                    ball.move()
                    if ball.hittest(target):
                        target.hit()
                        target_list.remove(target)
                    if not target_list:
                        it.canvas.bind('<Button-1>', '')
                        it.canvas.bind('<ButtonRelease-1>', '')
                        if gun_examp.bullet == 1:
                            bullet_quant =' выстрел'
                        elif gun_examp.bullet in (2, 3, 4):
                            bullet_quant = ' выстрела'
                        else:
                            bullet_quant = ' выстрелов'
                        it.canvas.itemconfig(screen1, text='Вы уничтожили цели за ' + str(gun_examp.bullet) + bullet_quant)
                    if ball.speedometr < 10 and ball.y > 500:
                            it.canvas.delete(ball.id)
                            gun_examp.balls_list.remove(ball)
        if gun_examp.balls_list and not target_list:
            for ball in gun_examp.balls_list:
                ball.move()
                if ball.speedometr < 10 and ball.y > 500:
                        it.canvas.delete(ball.id)
                        gun_examp.balls_list.remove(ball)
        it.canvas.update()
        time.sleep(0.03)
        gun_examp.targetting()
        gun_examp.power_up()
    it.root.after(750, game)
    it.canvas.itemconfig(screen1, text='')
    it.root.mainloop()
game()
