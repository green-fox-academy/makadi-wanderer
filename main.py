from tkinter import *
from map import Map

size = 720

root = Tk()
root.configure(background ='black')
canvas = Canvas(root, width=size, height=size,bd=0)
canvas.pack()


class App():
    def __init__(self):
        self.rect = None
        self.floor_image = PhotoImage(file='elements/floor.gif')
        self.wall_image = PhotoImage(file='elements/wall.gif')
        self.map = Map()
        self.draw_map(self.map.tiles)

    def draw_map(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    image = self.floor_image
                else:
                    image = self.wall_image
                canvas.create_image(j * 72, i * 72, anchor=NW, image=image)


class Entity():
    def __init__(self):
        self.hero_down = PhotoImage(file='elements/hero-down.gif')
        self.hero_up = PhotoImage(file='elements/hero-up.gif')
        self.hero_left = PhotoImage(file='elements/hero-left.gif')
        self.hero_right = PhotoImage(file='elements/hero-right.gif')
        self.skeleton_image = PhotoImage(file='elements/skeleton.gif')
        self.boss_image = PhotoImage(file='elements/boss.gif')
        self.pos_x = 0
        self.pos_y = 0

    def hero_shape(self):
        self.hero = canvas.create_image(36, 36, image=self.hero_down)

    def move(self, dx, dy):
        canvas.move(self.hero, dx * 72, dy * 72)

    def enemy_one_shape(self):
        self.enemy_one = canvas.create_image(9 * 72 + 36, 9 * 72 + 36, image=self.skeleton_image)

    def enemy_two_shape(self):
        self.enemy_one = canvas.create_image(2 * 72 + 36, 8 * 72 + 36, image=self.skeleton_image)

    def enemy_three_shape(self):
        self.enemy_one = canvas.create_image(4 * 72 + 36, 9 * 72 + 36, image=self.skeleton_image)


def on_key_press(e):
    if ( e.keysym == 'Up' ):
        if not myapp.map.is_wall(hero.pos_x, hero.pos_y - 1) and hero.pos_y > 0:
            hero.move(0, -1)
            canvas.itemconfig(hero.hero, image=hero.hero_up)
            hero.pos_y -= 1
    elif ( e.keysym == 'Down' ):
        if not myapp.map.is_wall(hero.pos_x, hero.pos_y + 1) and hero.pos_y < 9:
            hero.move(0, 1)
            canvas.itemconfig(hero.hero, image=hero.hero_down)
            hero.pos_y += 1
    elif ( e.keysym == 'Left' ):
        if not myapp.map.is_wall(hero.pos_x - 1, hero.pos_y) and hero.pos_x > 0:
            hero.move(-1, 0)
            canvas.itemconfig(hero.hero, image=hero.hero_left)
            hero.pos_x -= 1
    elif ( e.keysym == 'Right' ):
        if not myapp.map.is_wall(hero.pos_x + 1, hero.pos_y) and hero.pos_x < 9:
            hero.move(1, 0)
            canvas.itemconfig(hero.hero, image=hero.hero_right)
            hero.pos_x += 1


myapp = App()
hero = Entity()
hero.hero_shape()
enemy_one = Entity()
enemy_one.enemy_one_shape()
enemy_two = Entity()
enemy_two.enemy_two_shape()
enemy_three = Entity()
enemy_three.enemy_three_shape()


root.bind("<KeyPress>", on_key_press)
canvas.pack()

canvas.focus_set()

root.mainloop()