import pygame
import random
import math


pygame.init()
screencaption = pygame.display.set_caption('MineSweeper')
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
myfont = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
flag = 0

# 二维数组
block_list = []
for i in range(15):
    temp_list = []
    for j in range(15):
        temp_list.append(0)
    block_list.append(temp_list)

# 布雷
boom_list = []
n = 0
while n < 15:
    i = random.randint(0, 15 - 1)
    j = random.randint(0, 15 - 1)
    data = (i, j)
    while data in boom_list:
        i = random.randint(0, 15 - 1)
        j = random.randint(0, 15 - 1)
        data = (i, j)
    boom_list.append(data)
    block_list[i][j] = 9
    n = n + 1

# 计算生成矩阵数据
for i in range(15):
    for j in range(15):
        if block_list[i][j] == 9:
            # 上
            if i - 1 >= 0 and block_list[i - 1][j] != 9:
                block_list[i - 1][j] = int(block_list[i - 1][j]) + 1
            # 下
            if i + 1 < 15 and block_list[i + 1][j] != 9:
                block_list[i + 1][j] = int(block_list[i + 1][j]) + 1
            # 左
            if j - 1 >= 0 and block_list[i][j - 1] != 9:
                block_list[i][j - 1] = int(block_list[i][j - 1]) + 1
            # 右
            if j + 1 < 15 and block_list[i][j + 1] != 9:
                block_list[i][j + 1] = int(block_list[i][j + 1]) + 1

            # 左上
            if i - 1 >= 0 and j - 1 >= 0 and block_list[i - 1][j - 1] != 9:
                block_list[i - 1][j - 1] = int(block_list[i - 1][j - 1]) + 1
            # 右上
            if i + 1 < 15 and j - 1 >= 0 and block_list[i + 1][j - 1] != 9:
                block_list[i + 1][j - 1] = int(block_list[i + 1][j - 1]) + 1
            # 左下
            if i - 1 >= 0 and j + 1 < 15 and block_list[i - 1][j + 1] != 9:
                block_list[i - 1][j + 1] = int(block_list[i - 1][j + 1]) + 1
            # 右下
            if i + 1 < 15 and j + 1 < 15 and block_list[i - 1][j + 1] != 9:
                block_list[i + 1][j + 1] = int(block_list[i + 1][j + 1]) + 1
'''
s = ""
for i in range(15):
    for j in range(15):
        if j % 15 == 0:
            print(s)
            s = ""
        s = s + str(block_list[i][j])
'''

# 位置是否显示
# 0 为未知
# 1 为已知
# 初始化都为未知
show_list = []
for i in range(15):
    temp_list = []
    for j in range(15):
        temp_list.append(0)
    show_list.append(temp_list)


def click_compute(now_i, now_j):
    if block_list[now_i][now_j] == 9:
        return 0
    print("点击鼠标")
    to_show(now_i, now_j)
    return 1


def to_show(now_i, now_j):
    if block_list[now_i][now_j] != 0:
        return
    show_list[now_i][now_j] = 1
    print("=== showlist->1 ===")
    # 左 上 右 下
    # 四个方向进行遍历
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for k in range(4):
        now_x = now_i + dx[k]
        now_y = now_j + dy[k]
        if 0 <= now_x < 15 and 0 <= now_y < 15:
            to_show(now_x, now_y)


move_x = 0
move_y = 0
close_i = 0
close_j = 0

while True:
    clock.tick(30)
    screen.fill([255, 255, 255])
    # 读取鼠标位置
    move_x, move_y = pygame.mouse.get_pos()
    # pygame.draw.circle(screen, [255, 0, 0], [move_x, move_y], 10)
    for i in range(15):
        for j in range(15):
            x = i * 26 + 10
            y = j * 26 + 10
            # 这里要判断是否要显示数值
            # if show_list[i][j] == 1:
            #    textImage = myfont.render(str(block_list[i][j]), True, [0, 0, 0])
            #    screen.blit(textImage, (x + 2, y + 2))
            textImage = myfont.render(str(block_list[i][j]), True, [0, 0, 0])
            screen.blit(textImage, (x + 2, y + 2))
            # 靠近哪个位置
            # print("x: " + str(move_x / 26) + " -> " + "y: " + str(move_y / 26))
            close_i = math.floor(move_x / 26)
            close_j = math.floor(move_y / 26)
            # print("x: " + str(close_i) + " -> " + "y: " + str(close_j))
            position = (x, y, 20, 20)
            if close_i == i and close_j == j:
                pygame.draw.rect(screen, [125, 125, 125], position, 8)
            else:
                pygame.draw.rect(screen, [125, 125, 125], position, 2)
            '''
            if block_list[i][j] == 0:
                position = (x, y, 20, 20)
                if close_i == i and close_j == j:
                    pygame.draw.rect(screen, [100, 200, 50], position, 5)
                else:
                    pygame.draw.rect(screen, [100, 200, 50], position, 2)
            elif block_list[i][j] == 9:
                position = (x, y, 20, 20)
                if close_i == i and close_j == j:
                    pygame.draw.rect(screen, [50, 100, 200], position, 5)
                else:
                    pygame.draw.rect(screen, [50, 100, 200], position, 2)
            '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move_x < 0 or move_x > screen_width or move_y < 0 or move_y > screen_height:
                pass
            result = click_compute(close_i, close_j)
            if result == 0:
                break
    pygame.display.flip()
