import sys

import pygame
import random
import time

# Инициализация pygame
pygame.init()
# Переменная для отображения окна меню
menu_open = True  #Пока не придумал, что выводить в главное меню
# Создание объекта Clock
clock = pygame.time.Clock()
game_continue = True


# Функция для отображения окна меню
def show_menu():
    # Рисование окна меню на экране
    # Обработка событий мыши и клавиатуры
    # Рисование кнопки "старт" на экране

    screen = pygame.display.set_mode((300, 300))
    pygame.draw.rect(screen, (0, 255, 0), (10, 100, 280, 50))
    font = pygame.font.Font(None, 42)
    text = font.render("Старт", True, (0, 0, 0))
    screen.blit(text, (100, 110))
    pygame.display.flip()
    clock.tick(10)


# Рисование окна меню на экране
# Обработка событий мыши и клавиатуры

# Основная функция игры
def game():
    global menu_open
    global game_continue
    while game_continue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Обработка событий мыши
                if menu_open:
                    mx, my = pygame.mouse.get_pos()
                    if 10 < mx < 290 and 100 < my < 150:
                        menu_open = False

                        game()
        if menu_open:
            show_menu()
        else:
            # Создание окна
            screen = pygame.display.set_mode((400, 400))

            # Цвета
            BLACK = (0, 0, 0)
            GREEN = (0, 255, 0)
            RED = (255, 0, 0)

            # Координаты круга
            x = 150
            y = 150

            # Радиус круга
            radius = 10

            # Координаты красных кругов
            red_circles = []
            for _ in range(10):
                while True:
                    rx = random.randint(radius, 300 - radius)
                    ry = random.randint(radius, 300 - radius)
                    if ((rx - x) ** 2 + (ry - y) ** 2) ** 0.5 > radius + 5:
                        red_circles.append((rx, ry, random.choice([-1, 1]), random.choice([-1, 1])))
                        break

            # Счет
            score = 0

            # Основной цикл программы
            running = True
            while running:
                # Обработка событий

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_continue = False

                # Очистка экрана
                screen.fill(BLACK)

                # Рисование кругов
                pygame.draw.circle(screen, GREEN, (x, y), radius)
                for i, (rx, ry, dx, dy) in enumerate(red_circles):
                    pygame.draw.circle(screen, RED, (rx, ry), 5)

                # Отображение счета
                font = pygame.font.Font(None, 36)
                text = font.render("Счет: " + str(score), True, GREEN)
                screen.blit(text, (10, 10))

                # Обновление экрана
                pygame.display.flip()

                # Управление движением круга
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and y > radius:
                    y -= 2
                if keys[pygame.K_DOWN] and y < 300 - radius:
                    y += 2
                if keys[pygame.K_LEFT] and x > radius:
                    x -= 2
                if keys[pygame.K_RIGHT] and x < 300 - radius:
                    x += 2

                # Обработка столкновений
                for i, (rx, ry, dx, dy) in enumerate(red_circles):
                    if ((rx - x) ** 2 + (ry - y) ** 2) ** 0.5 <= radius + 5:
                        del red_circles[i]
                        score += 1

                # Обработка столкновений красных кругов с границами экрана
                for i, (rx, ry, dx, dy) in enumerate(red_circles):
                    if rx < radius or rx > 300 - radius:
                        dx *= -1
                    if ry < radius or ry > 300 - radius:
                        dy *= -1
                    red_circles[i] = (rx + dx, ry + dy, dx, dy)

                # Изменение направления движения красных кругов
                for i, (rx, ry, dx, dy) in enumerate(red_circles):
                    if ((rx - x) ** 2 + (ry - y) ** 2) ** 0.5 < 70:
                        if rx < x:
                            dx = -1
                        else:
                            dx = 1
                        if ry < y:
                            dy = -1
                        else:
                            dy = 1
                        red_circles[i] = (rx, ry, dx, dy)

                # Проверка победы
                if not red_circles:
                    running = False
                    screen.fill(BLACK)
                    font = pygame.font.Font(None, 36)
                    text = font.render("Победа! У вас " + str(score) + " очков", True, GREEN)
                    screen.blit(text, (50, 150))
                    pygame.display.flip()
                    time.sleep(3)
                    pygame.quit()
                # Задержка в 0,5 секунды
                time.sleep(0.01)

            # Завершение pygame
            # pygame.quit()
            game_continue = False


# Запуск игры
game()
# Завершение pygame
pygame.quit()
