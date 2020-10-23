import pygame
import random


pygame.init()
screencaption = pygame.display.set_caption('MineSweeper')
screen = pygame.display.set_mode([400, 400])
myfont = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
flag = 0

block_list = []
for i in range(15):
    temp_list = []
    for j in range(15):
        temp_list.append(0)
    block_list.append(temp_list)

# 雷
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
s = ""
for i in range(15):
    for j in range(15):
        if j % 15 == 0:
            print(s)
            s = ""
        s = s + str(block_list[i][j])


while True:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for i in range(15):
        for j in range(15):
            x = i * 26 + 10
            y = j * 26 + 10
            textImage = myfont.render(str(block_list[i][j]), True, [0, 0, 0])
            screen.blit(textImage, (x + 2, y + 2))
            if block_list[i][j] == 0:
                position = (x, y, 20, 20)
                pygame.draw.rect(screen, [100, 200, 50], position, 2)
            elif block_list[i][j] == 9:
                position = (x, y, 20, 20)
                pygame.draw.rect(screen, [50, 100, 200], position, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.flip()
