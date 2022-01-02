import time
import tkinter
from tkinter import *
from tkinter import messagebox
import numpy as np
import Winner
from alpha_beta import searcher

global chess_b

global flag


class chess_borad():

    def __init__(self):
        # 创建并添加 canvas
        # 创建窗口
        self.root = Tk()
        self.root.title("五子棋")
        self.root.iconphoto(False, PhotoImage(file='picture/black.png'))

        self.menubar = Menu(self.root)  # 创建菜单栏

        # 创建“文件”下拉菜单
        filemenu1 = Menu(self.menubar, tearoff=0)
        filemenu2 = Menu(self.menubar, tearoff=0)
        filemenu1.add_command(label="人机对弈（机器先手）", command=self.AI_first)
        filemenu1.add_command(label="人机对弈（玩家先手）", command=self.person_first)
        filemenu2.add_command(label="双人模式（白子先）", command=self.player_W)
        filemenu2.add_command(label="双人模式（黑子先）", command=self.player_B)
        filemenu1.add_separator()
        filemenu1.add_command(label="退出", command=self.root.quit)
        filemenu2.add_separator()
        filemenu2.add_command(label="退出", command=self.root.quit)

        # 创建“编辑”下拉菜单
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="第一关", command=self.game_Chanllnenge1)
        editmenu.add_command(label="第二关", command=self.game_Chanllnenge2)
        editmenu.add_command(label="第三关", command=self.game_Chanllnenge3)
        editmenu.add_command(label="第四关", command=self.game_Chanllnenge4)
        editmenu.add_command(label="第五关", command=self.game_Chanllnenge5)

        # 创建“帮助”下拉菜单
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="关于", command=self.about_us)

        # 将前面三个菜单加到菜单栏
        self.menubar.add_cascade(label="人机对弈", menu=filemenu1)
        self.menubar.add_cascade(label="双人对弈", menu=filemenu2)
        self.menubar.add_cascade(label="残局挑战", menu=editmenu)
        self.menubar.add_cascade(label="关于我", menu=helpmenu)

        # 最后再将菜单栏整个加到窗口 root
        self.root.config(menu=self.menubar)

        self.gaird_width = 40
        self.gaird_count = 16

        self.widths = self.gaird_width * self.gaird_count + 20

        self.root.maxsize(self.widths, self.widths)
        self.root.minsize(self.widths, self.widths)
        self.cv = Canvas(self.root, background='white')
        self.black=PhotoImage(file='picture/black.png')
        self.white = PhotoImage(file="picture/white.png")
        self.message = Label(self.root, text="开始游戏请先在菜单栏选择模式！")
        self.message.pack(side=BOTTOM)

        self.reset()



    # 清空并重置棋盘函数
    def reset(self):

        self.cv.destroy()
        self.message.destroy()
        # 创建并添加Canvas
        self.cv = Canvas(self.root, background='white',cursor="star")
        self.cv.pack(fill=BOTH, expand=YES)

        # 画一个外边框为白的 , 填充棋盘颜色
        self.cv.create_rectangle(10, 10, self.gaird_width * self.gaird_count + 10,
                                 self.gaird_width * self.gaird_count + 10, outline="white",
                                 fill="Teal")  #水鸭色

        # 在棋盘里面画 画格子
        for num in range(1, self.gaird_count):
            self.cv.create_line(num * self.gaird_width + 10,
                                self.gaird_width + 10,
                                num * self.gaird_width + 10,
                                self.gaird_width * (self.gaird_count - 1) + 10,
                                width=2,
                                fill="#595959")
        for num in range(1, self.gaird_count):
            self.cv.create_line(self.gaird_width + 10,
                                num * self.gaird_width + 10,
                                (self.gaird_count - 1) * self.gaird_width + 10,
                                num * self.gaird_width + 10,
                                width=2,
                                fill="#595959"
                                )
        self.message = Label(self.root, text="开始游戏请先在菜单栏选择模式！")
        self.message.pack(side=BOTTOM)

        # 初始化
        # self.cv.bind("<Button-1>", self.paint2)      # 左击鼠标是黑子
        self.flag = ''  # flag记录到谁，w代表白棋,b代表黑子
        self.chess_b = np.zeros((15, 15), dtype=int)
        self.xx= self.cv.create_line(- 10, - 10, 0, 0, arrow=tkinter.LAST)


# --------------------------------------菜单函数----------------------------------
    def about_us(self):
        about = Tk()
        about.title('about us')
        #about.iconphoto(True, PhotoImage(file='white.png'))
        about.maxsize(400, 200)
        about.minsize(400, 200)
        label=Label(about,text='开  发  者：            hymei\n\n联系我：hymei0@126.com',bg='Teal')

        label.place(x=0, y=0,width='400',height='200')
        about.mainloop()

    def file_open(self):
        pass

    def player_W(self):

        self.reset()

        self.message.destroy()
        self.flag = 'w'                       # flag记录到谁，w代表白棋,b代表黑子
        # 事件绑定
        self.cv.bind("<Button-1>", self.paint)  # 左击鼠标是黑子
        self.cv.bind("<Button-3>", self.paint)  # 右击鼠标是白子
        self.message = Label(self.root, text="Turn to white player")
        self.message.pack(side=BOTTOM)

    # 双人对弈 黑子先
    def player_B(self):
        self.reset()
        self.message.destroy()
        self.flag = 'b'  # flag记录到谁，w代表白棋,b代表黑子
        # 事件绑定
        self.cv.bind("<Button-1>", self.paint)  # 左击鼠标是黑子
        self.cv.bind("<Button-3>", self.paint)  # 右击鼠标是白子
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)


    # 人机对弈，Ai先手
    def person_first(self):

        self.reset()

        self.cv.bind("<Button-1>", self.paint_x)  # 左击鼠标是黑子

  #人机对弈，Ai先手
    def AI_first(self):



        self.reset()

        self.AI_start()


    def AI_start(self):
        # self.chess_b = np.zeros((16, 16), dtype=int)
        self.message.destroy()
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)

        self.flag = 'w'

        ai = searcher(self.chess_b)
        ai.board = self.chess_b
        score, x, y = ai.search(2, 2)
        #print('white（{0},{1}）'.format(x, y))

        if self.chess_b[x][y] == 2 or self.chess_b[x][y] == 1:
            pass
        else:
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)

            self.chess_b[x][y] = 2

            self.flag = 'b'
            flag1 = Winner.winner(self.chess_b)
            if flag1 == 1:
                self.message.destroy()
                self.message = Label(self.root, text="Game over")
                self.message.pack(side=BOTTOM)
                self.cv.update()

                messagebox.showinfo(title='victory', message='你赢啦！')
                self.reset()
                return 1

            elif flag1 == 2:
                self.message.destroy()
                self.message = Label(self.root, text="Game over")
                self.message.pack(side=BOTTOM)
                self.cv.update()

                messagebox.showinfo(title='defeat', message='AI胜利！😔')
                self.reset()
                return 2
            else:
                self.cv.bind("<Button-1>", self.paint_x)  # 左击鼠标是黑子


    def paint_x(self,event):

        self.message.destroy()
        self.message = Label(self.root, text="Turn to white player")
        self.message.pack(side=BOTTOM)


        flag1 = Winner.winner(self.chess_b)
        if self.flag == 'w' or flag1 == 1 or flag1 == 2:
            pass
        else:

            x: int = int((event.x + 0.5 * self.gaird_width - 10) / self.gaird_width)
            y: int = int((event.y + 0.5 * self.gaird_width - 10) / self.gaird_width)

            #print('bule({0},{1})'.format(x, y))

            if x == 0 or y == 0 or y > 15 or x > 15:
                messagebox.showinfo(title='错误', message='该位置不允许放棋子！')
            else:
                if self.chess_b[x-1][y-1] == 2 or self.chess_b[x-1][y-1 ] == 1:
                    pass
                else:
                    x1, y1 = (x * self.gaird_width), (y * self.gaird_width)
                    x2, y2 = (x * self.gaird_width + 20), (y * self.gaird_width + 20)
                    self.cv.create_image(int((x1+x2)/2), int((y1+y2)/2),image=self.black)
                    self.cv.update()

                    self.chess_b[x-1][y-1 ] = 1


                    flag1 = Winner.winner(self.chess_b)
                    if flag1 == 1:
                        self.message.destroy()
                        self.message = Label(self.root, text="Game over")
                        self.message.pack(side=BOTTOM)
                        self.cv.update()

                        messagebox.showinfo(title='恭喜', message='你赢啦！')
                        self.reset()

                        return 1

                    elif flag1 == 2:
                        self.message.destroy()
                        self.message = Label(self.root, text="Game over")
                        self.message.pack(side=BOTTOM)
                        self.cv.update()

                        messagebox.showinfo(title='sad', message='AI胜利！😔')
                        self.reset()

                        return 2
                    else:
                        #print('棋盘状态：', self.chess_b)
                        self.AI_start()

    #双人对弈时，玩家画棋子
    def paint(self, event):

        flag1 = Winner.winner(self.chess_b)

        if  flag1 == 1 or flag1 == 2:
            pass
        else:

            x: int = int((event.x + 0.5 * self.gaird_width - 10) / self.gaird_width)
            y: int = int((event.y + 0.5 * self.gaird_width - 10) / self.gaird_width)

            print('white({0},{1})'.format(x, y))

            if x == 0 or y == 0 or y > 15 or x > 15:
                messagebox.showinfo(title='错误', message='该位置不允许放棋子！')
            else:
                if self.chess_b[y-1 ][x-1 ] == 2 or self.chess_b[y-1 ][x-1 ] == 1:
                    pass
                else:
                    x1, y1 = (x * self.gaird_width), (y * self.gaird_width)
                    x2, y2 = (x * self.gaird_width + 20), (y * self.gaird_width + 20)
                    #self.cv.create_oval(x1, y1, x2, y2, fill=python_green)
                    if self.flag=='b':
                        self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.black)
                    else:
                        self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)
                    self.chess_b[y-1][x-1] = 2  if self.flag=='w' else 1
                    self.flag = 'b' if self.flag=='w' else 'w'
                    self.message.destroy()
                    self.message = Label(self.root, text="Turn to white player") if  self.flag=='w' else Label(self.root, text="Turn to bule player")
                    self.message.pack(side=BOTTOM)
                    flag1 = Winner.winner(self.chess_b)
                    if flag1 == 1:
                        messagebox.showinfo(title='恭喜', message='黑子胜利！')

                        self.message.destroy()
                        self.message = Label(self.root, text="Game over")
                        self.message.pack(side=BOTTOM)
                        self.cv.update()
                        return

                    elif flag1 == 2:
                        self.message.destroy()
                        self.message = Label(self.root, text="Game over")
                        self.message.pack(side=BOTTOM)
                        self.cv.update()
                        messagebox.showinfo(title='恭喜', message='白子胜利！')

                        self.reset()
                        return

                    else:
                        pass

    def game_Chanllnenge1(self):

        self.reset()
        self.message.destroy()
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)
        self.cv.update()

        list_w = [(6, 6), (6, 7), (8, 6), (9, 6), (10, 5), (12, 5), (7, 8), (10, 9)]
        list_b = [(5, 8), (7, 6), (8, 5), (8, 7), (9, 8), (10, 7), (10, 8), (11, 6)]
        for li1 in list_w:
            x = int(li1[0])
            y = int(li1[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)

            self.chess_b[x][y] = 2
        for li2 in list_b:
            x = int(li2[0])
            y = int(li2[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.black)

            self.chess_b[x][y] = 1
        self.cv.bind("<Button-1>", self.paint_x)

    def game_Chanllnenge2(self):
        self.reset()
        self.message.destroy()
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)
        self.cv.update()
        list_w = [(3, 7), (5, 7), (6, 6), (10, 6), (8, 8), (8, 9), (9, 10), (7, 11), (6, 11), (4, 10), (10, 12), (7, 8)]
        list_b = [(4, 8), (5, 9), (6, 10), (6, 9), (6, 8), (6, 7), (7, 7), (7, 9), (8, 10), (9, 11), (10, 8), (10, 7)]
        for li1 in list_w:
            x = int(li1[0])
            y = int(li1[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)

            self.chess_b[x][y] = 2
        for li2 in list_b:
            x = int(li2[0])
            y = int(li2[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.black)
            self.chess_b[x][y] = 1
        self.cv.bind("<Button-1>", self.paint_x)

    def game_Chanllnenge3(self):
        self.reset()
        self.message.destroy()
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)
        self.cv.update()
        list_w = [(5, 6), (7, 6), (8, 6), (6, 7), (8, 7), (10, 6), (11, 6), (10, 7), (10, 4), (7, 9)]
        list_b = [(4, 7), (6, 8), (6, 5), (9, 5), (10, 5), (9, 6), (11, 7), (6, 8), (7, 8), (7, 7), (8, 9)]
        for li1 in list_w:
            x = int(li1[0])
            y = int(li1[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)

            self.chess_b[x][y] = 2
        for li2 in list_b:
            x = int(li2[0])
            y = int(li2[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.black)
            self.chess_b[x][y] = 1
        self.cv.bind("<Button-1>", self.paint_x)

    def game_Chanllnenge4(self):
        self.reset()
        self.message.destroy()
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)
        self.cv.update()
        list_w = [(6, 5), (7, 6), (6, 7), (9, 8), (9, 3), (10, 4), (10, 6), (6, 5)]
        list_b = [(7, 5), (8, 5), (9, 5), (9, 4), (8, 6), (7, 7), (9, 6)]
        for li1 in list_w:
            x = int(li1[0])
            y = int(li1[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)

            self.chess_b[x][y] = 2
        for li2 in list_b:
            x = int(li2[0])
            y = int(li2[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.black)
            self.chess_b[x][y] = 1
        self.cv.bind("<Button-1>", self.paint_x)

    def game_Chanllnenge5(self):
        self.reset()
        self.message.destroy()
        self.message = Label(self.root, text="Turn to black player")
        self.message.pack(side=BOTTOM)
        self.cv.update()
        list_w = [(3, 7), (8, 6), (8, 7), (8, 8), (7, 8), (6, 9), (8, 10), (5, 11)]
        list_b = [(5, 7), (4, 8), (7, 7), (6, 8), (5, 9), (7, 9), (8, 9), (5, 10)]
        for li1 in list_w:
            x = int(li1[0])
            y = int(li1[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.white)

            self.chess_b[x][y] = 2
        for li2 in list_b:
            x = int(li2[0])
            y = int(li2[1])
            x1, y1 = ((x + 1) * self.gaird_width), ((y + 1) * self.gaird_width)
            x2, y2 = ((x + 1) * self.gaird_width + 20), ((y + 1) * self.gaird_width + 20)
            self.cv.create_image(int((x1 + x2) / 2), int((y1 + y2) / 2), image=self.black)
            self.chess_b[x][y] = 1
        self.cv.bind("<Button-1>", self.paint_x)

# <Button-1>：鼠标左击事件
# <Button-2>：鼠标中击事件
# <Button-3>：鼠标右击事件
# <Double-Button-1>：双击事件
# <Triple-Button-1>：三击事件
def main():
    chess_Borad = chess_borad()
    chess_Borad.root.mainloop()

main()
