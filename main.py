import pygame
import random

pygame.init()

screen = pygame.display.set_mode([500,600])
screenSize = [500,600]

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

class Snake(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Snake, self).__init__()
        self.square = pygame.Surface((20,20))
        self.square.fill((255,255,255))
        self.rect = self.square.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.turn = 0
        self.cooldown = 500
        self.lenght = 1
        self.body = []
        self.body.append((self.rect.x, self.rect.y))
        self.highscore = 1

    def death(self):
        if self.highscore < self.lenght:
            self.highscore = self.lenght
        self.lenght = 1
        self.rect.x = 240
        self.rect.y = 240
        self.turn = 0
        self.body = []
        self.body = [(240,240)]

    def update(self):

        for i in range(self.lenght):
            screen.blit(self.square, self.body[i])

        key = pygame.key.get_pressed()
        self.cooldown -= 2
        if self.cooldown <= 0:
            if self.turn == "e":
                if self.rect.right > screenSize[0]:  # przechodzenie przez prawa sciane
                    self.rect.x -= 520
                self.body.insert(0, (self.rect.x + 20, self.rect.y))
                self.rect.x += 20
                if len(self.body) > self.lenght:
                    self.body.pop()
                self.cooldown = 250
                if (self.rect.x, self.rect.y) in mainSnake.body[1:]:
                    Snake.death(self)
            if self.turn == "w":
                if self.rect.left < 0:  # lewo
                    self.rect.x += 520
                self.body.insert(0, (self.rect.x - 20, self.rect.y))
                self.rect.x -= 20
                if len(self.body) > self.lenght:
                    self.body.pop()
                self.cooldown = 250
                if (self.rect.x, self.rect.y) in mainSnake.body[1:]:
                    Snake.death(self)
            if self.turn == "s":
                if self.rect.bottom > screenSize[1] - 120:  # dol
                    self.rect.y -= 520
                self.body.insert(0, (self.rect.x, self.rect.y + 20))
                self.rect.y += 20
                if len(self.body) > self.lenght:
                    self.body.pop()
                self.cooldown = 250
                if (self.rect.x, self.rect.y) in mainSnake.body[1:]:
                    Snake.death(self)
            if self.turn == "n":
                if self.rect.top < 0:  # gora
                    self.rect.y += 520
                    print("gora")
                self.body.insert(0, (self.rect.x, self.rect.y - 20))
                self.rect.y -= 20
                if len(self.body) > self.lenght:
                    self.body.pop()
                self.cooldown = 250
                if (self.rect.x, self.rect.y) in mainSnake.body[1:]:
                    Snake.death(self)

        if key[pygame.K_UP] and self.turn != "s":
            self.turn = "n"
        if key[pygame.K_DOWN] and self.turn != "n":
            self.turn = "s"
        if key[pygame.K_LEFT] and self.turn != "e":
            self.turn = "w"
        if key[pygame.K_RIGHT] and self.turn != "w":
            self.turn = "e"

        # if key[pygame.K_UP] and self.turn == "n":
        #     self.cooldown -= 4
        # if key[pygame.K_DOWN] and self.turn == "s":
        #     self.cooldown -= 4
        # if key[pygame.K_LEFT] and self.turn == "w":
        #     self.cooldown -= 4
        # if key[pygame.K_RIGHT] and self.turn == "e":
        #     self.cooldown -= 4


        # Jak chcesz zrobic przyspieszenie tylko na klawisze strzałek to odkomentuj góre i zakomentuj to na dole:

        if key[pygame.K_SPACE]:
            self.cooldown -= 4



        # if self.rect.right > screenSize[0] or self.rect.left < 0 or self.rect.bottom > screenSize[1] - 100 or self.rect.top < 0:
        #     Snake.death(self)
        # śmierc snejka gdy dotknie ściany /\




        #oczy węża \/
        if self.turn == "e":
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 15, self.rect.y + 5), 2)
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 15, self.rect.y + 15), 2)
        if self.turn == "w":
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 5, self.rect.y + 5), 2)
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 5, self.rect.y + 15), 2)
        if self.turn == "n":
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 5, self.rect.y + 5), 2)
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 15, self.rect.y + 5), 2)
        if self.turn == "s":
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 15, self.rect.y + 15), 2)
            pygame.draw.circle(screen, (255,0,0), (self.rect.x + 5, self.rect.y + 15), 2)

        # TO NA DOLE ZOSTALO WRZUCONE DO STEROWANIA
        # if self.rect.right > screenSize[0]: #przechodzenie przez prawa sciane
        # #     self.rect.x -= 480
        # #     print("prawo")
        #
        # if self.rect.left < 0:#lewo
        #     self.rect.x += 480
        #     print("lewo")
        #
        # if self.rect.bottom > screenSize[1] - 100:#dol
        #     self.rect.y -= 500
        #     print("dol")
        #
        # if self.rect.top < 0: #gora
        #     self.rect.y += 500
        #     print("gora")

class Food(pygame.sprite.Sprite):
    def __init__(self):
        random1 = random.randint(0, 24)
        random2 = random.randint(0, 24)
        super(Food, self).__init__()
        self.square = pygame.Surface((20,20))
        self.square.fill((155,0,0))
        self.rect = self.square.get_rect()
        self.rect.x = random1 * 20
        self.rect.y = random2 * 20
    def update(self):
        screen.blit(self.square, (self.rect.x, self.rect.y))
        if pygame.sprite.spritecollide(mainSnake, foodGroup, False):
            self.kill()
            mainSnake.lenght += 1
            mainSnake.body.append((mainSnake.rect.x, mainSnake.rect.y))
        if (self.rect.x, self.rect.y) in mainSnake.body:
            self.kill()

foodGroup = pygame.sprite.Group()
snakeGroup = pygame.sprite.Group()

mainSnake = Snake(240,240)

font = pygame.font.SysFont('Courier Regular', 30)

running = True
while running:

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if len(foodGroup) == 0:
        food = Food()
        foodGroup.add(food)

    mainSnake.update()
    food.update()

    draw_text(f"Twój wynik: {mainSnake.lenght}", font, (255,0,255), 40, 540)
    draw_text(f"Najwyższy: {mainSnake.highscore}", font, (255, 0, 255), 290, 540)

    for i in range(25):
        pygame.draw.line(screen, (25, 155, 155), (i * 20-1, 0), (i * 20-1, 500), 1)
    for i in range(26):
        pygame.draw.line(screen, (25, 155, 155), (0, i * 20-1), (500, i * 20-1), 1)

    pygame.display.flip()
pygame.quit()