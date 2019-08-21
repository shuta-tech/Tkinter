import tkinter as tk
import sys

#global variable
g = 9.8
t = 0.5
e = -0.9
e_c = -0.6
e_w = -0.8
f_x = f_y = 0.7

# initial
win_width = 600
win_height = 400
win_center_x = win_width/2
win_center_y = win_height/2
tick = 40

#class of ball
class ball:
    x = 100
    y = 50
    w = 10

    dx = ddx = 0.5
    dy = -0.5
    color = "red"

    def draw_ball(self):
        cv.delete('all')    #バッファの削除
        cv.create_oval(self.x-self.w, self.y-self.w, self.x+self.w, self.y+self.w, fill = self.color, tag = "ball")
        cv.pack()

#action function
    def move(self):
        self.dx += self.ddx*t
        self.dy += g*t

        self.x += self.dx*t + 0.5*self.ddx*t*t
        self.y += self.dy*t + 0.5*g*t*t

    def colision_wall(self):
        dis1 = paddle.x - paddle.px
        dis2 = paddle.x + paddle.px

        if self.y + self.w > 400:
            self.dy *= e
            self.dx *= f_x
            self.y = 390

        elif self.x + self.w > 600:
            self.dx *= e_w
            self.x = 590

        elif self.y - self.w < 0:
            self.dy *= e_c
            self.y = 10

        if self.y + self.w > paddle.y - paddle.py and self.x + self.w > dis1 and self.x - self.w < dis2:
            self.dy *= paddle.p_e
            self.y = paddle.y - paddle.py


    def delete(self):
        cv.delete("ball")

class paddle():
    x = win_center_x-120
    y = win_height-50
    px = 75
    py = 10
    dx = 20
    p_e = -1.2
    color = "green"

    def draw(self):
        cv.create_rectangle(self.x - self.px, self.y - self.py, self.x + self.px, self.y + self.py, fill = self.color, tag = "paddle")

    def Right(self, event):
        self.x -= self.dx
    def Left(self, event):
        self.x += self.dx

    def move(self):
        root.bind("<Key-a>", self.Right)
        root.bind("<Key-d>", self.Left)

#main function　and set of window
root = tk.Tk()
root.title(u"Shuta-CIT")
root.geometry("600x400")
cv = tk.Canvas(root, width = win_width, height = win_height, bg = "blue")
cv.place(x = 0, y = 0)

ball = ball()
paddle = paddle()

#initial discribe
ball.draw_ball()
ball.move()
ball.colision_wall()
#ball.colision_paddle()
paddle.draw()
paddle.move()

def gameloop():
    ball.draw_ball()
    ball.move()
    ball.colision_wall()
    #ball.colision_paddle()
    paddle.draw()
    paddle.move()
    root.after(tick, gameloop)

gameloop()
root.mainloop()
