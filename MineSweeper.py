import pygame
import random
import math


class MineSweeper(object):
    def __init__(self):
        # 扫雷宽
        self.mine_width = 15
        # 扫雷高
        self.mine_height = 15
        # 扫雷数
        self.mines = 20
        # 扫雷矩阵
        self.block_list = []
        for i in range(self.mine_width):
            temp_list = []
            for j in range(self.mine_height):
                temp_list.append(int(0))
            self.block_list.append(temp_list)
        # 布雷
        self.boom_list = []
        n = 0
        while n <= self.mines:
            i = random.randint(0, 15 - 1)
            j = random.randint(0, 15 - 1)
            data = (i, j)
            while data in self.boom_list:
                i = random.randint(0, 15 - 1)
                j = random.randint(0, 15 - 1)
                data = (i, j)
            self.boom_list.append(data)
            self.block_list[i][j] = 9
            n = n + 1
        # 计算矩阵的分布
        self.compute_awtrix()
        # 计算显示矩阵
        self.show_list = []
        self.show_awtrix()
        # 颜色表
        # 颜色表
        self.color_list = [
            [187, 255, 200],
            [106, 90, 205],
            [205, 92, 92],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
            [139, 58, 58],
        ]

    # 计算生成矩阵数据
    def compute_awtrix(self):
        for i in range(self.mine_width):
            for j in range(self.mine_height):
                block_list = self.block_list
                if block_list[i][j] == 9:
                    # 上
                    if i - 1 >= 0 and block_list[i - 1][j] != 9:
                        block_list[i - 1][j] = int(int(block_list[i - 1][j]) + 1)
                    # 下
                    if i + 1 < 15 and block_list[i + 1][j] != 9:
                        block_list[i + 1][j] = int(int(block_list[i + 1][j]) + 1)
                    # 左
                    if j - 1 >= 0 and block_list[i][j - 1] != 9:
                        block_list[i][j - 1] = int(int(block_list[i][j - 1]) + 1)
                    # 右
                    if j + 1 < 15 and block_list[i][j + 1] != 9:
                        block_list[i][j + 1] = int(int(block_list[i][j + 1]) + 1)

                    # 左上
                    if i - 1 >= 0 and j - 1 >= 0 and block_list[i - 1][j - 1] != 9:
                        block_list[i - 1][j - 1] = int(int(block_list[i - 1][j - 1]) + 1)
                    # 右上
                    if i + 1 < 15 and j - 1 >= 0 and block_list[i + 1][j - 1] != 9:
                        block_list[i + 1][j - 1] = int(int(block_list[i + 1][j - 1]) + 1)
                    # 左下
                    if i - 1 >= 0 and j + 1 < 15 and block_list[i - 1][j + 1] != 9:
                        block_list[i - 1][j + 1] = int(int(block_list[i - 1][j + 1]) + 1)
                    # 右下
                    if i + 1 < 15 and j + 1 < 15 and block_list[i + 1][j + 1] != 9:
                        block_list[i + 1][j + 1] = int(int(block_list[i + 1][j + 1]) + 1)
                    self.block_list = block_list

    # 计算显示矩阵
    def show_awtrix(self):
        # 位置是否显示
        # 0 为未知
        # 1 为已知
        # 初始化都为未知
        for i in range(15):
            temp_list = []
            for j in range(15):
                temp_list.append(int(0))
            self.show_list.append(temp_list)

    # 单机左键
    def click_compute(self, now_i, now_j):
        if self.block_list[now_i][now_j] == 9:
            self.show_list[now_i][now_j] = 1
            return 0
        # print("点击鼠标")
        self.to_show(now_i, now_j)
        self.show_list[now_i][now_j] = 1
        return 1

    # 递归函数 游戏逻辑
    def to_show(self, now_i, now_j):
        if self.block_list[now_i][now_j] == 0:
            self.show_list[now_i][now_j] = 1
            dx = [-1, 0, 1, 0, -1, 1, -1, 1]
            dy = [0, -1, 0, 1, -1, -1, 1, 1]
            for k in range(8):
                now_x = now_i + dx[k]
                now_y = now_j + dy[k]
                if 0 <= now_x < 15 and 0 <= now_y < 15 and show_list[now_x][now_y] != 1:
                    self.show_list[now_x][now_y] = 1
                    self.to_show(now_x, now_y)


screen_width = 400
screen_height = 400
pygame.init()
screencaption = pygame.display.set_caption('MineSweeper')
screen = pygame.display.set_mode([screen_width, screen_height])
myfont = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
flag = 0


move_x = 0
move_y = 0
close_i = 0
close_j = 0

# 游戏状态
flag = 0

# Object
mine = MineSweeper()

while True:
    if flag == -1:
        break
    clock.tick(30)
    screen.fill([200, 200, 200])
    # 矩阵替换
    show_list = mine.show_list
    block_list = mine.block_list
    # 读取鼠标位置
    move_x, move_y = pygame.mouse.get_pos()
    # 绘制
    for i in range(15):
        for j in range(15):
            x = i * 26 + 10
            y = j * 26 + 10
            # 靠近哪个位置
            # print("x: " + str(move_x / 26) + " -> " + "y: " + str(move_y / 26))
            close_i = math.floor(move_x / 26)
            close_j = math.floor(move_y / 26)
            # print("x: " + str(close_i) + " -> " + "y: " + str(close_j))
            position = (x, y, 20, 20)
            if close_i == i and close_j == j:
                pygame.draw.rect(screen, [125, 125, 125], position, 5)
            else:
                if show_list[i][j] == 1:
                    pygame.draw.rect(screen, [125, 125, 125], position, 2)
                else:
                    pygame.draw.rect(screen, [105, 105, 105], position, 0)
            # 这里要判断是否要显示数值
            if show_list[i][j] == 1 and block_list[i][j] != 0:
                textImage = myfont.render(str(block_list[i][j]), True, mine.color_list[block_list[i][j]])
                screen.blit(textImage, (x + 2, y + 2))
            # textImage = myfont.render(str(block_list[i][j]), True, [0, 0, 0])
            # screen.blit(textImage, (x + 2, y + 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move_x < 0 or move_x > screen_width or move_y < 0 or move_y > screen_height:
                pass
            result = mine.click_compute(close_i, close_j)
            if result == 0:
                flag = -1
    mine.show_list = show_list
    mine.block_list = block_list
    pygame.display.flip()
