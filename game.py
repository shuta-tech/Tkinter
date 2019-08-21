import tkinter as tk
import sys

# initial
win_width = 600
win_height = 400
win_center_x = win_width/2
tick = 40

#class of ball
class ball:
    x = 300
    y = 200
    w = 20

    dx = dy = 2
    color = "red"

    def draw_ball(self):
        cv.delete('all')    #バッファの削除
        cv.create_oval(self.x-self.w, self.y-self.w, self.x+self.w, self.y+self.w, fill = self.color, tag = "ball")
        cv.pack()

#action function
    def left(self, event):
        self.x -= self.dx
    def right(self, event):
        self.x += self.dx
    def up(self, event):
        self.y -= self.dy
    def down(self, event):
        self.y += self.dy

    def move(self):
        root.bind("<Key-a>", self.left)
        root.bind("<Key-d>", self.right)
        root.bind("<Key-w>", self.up)
        root.bind("<Key-s>", self.down)

    def delete(self):
        cv.delete("ball")

#main function　and set of window
root = tk.Tk()
root.title(u"Shuta-CIT")
root.geometry("600x400")
cv = tk.Canvas(root, width = win_width, height = win_height, bg = "white")
cv.place(x = 0, y = 0)

ball = ball()

#initial discribe
ball.draw_ball()
ball.move()

def gameloop():
    ball.draw_ball()
    ball.move()
    root.after(tick, gameloop)

gameloop()
root.mainloop()
