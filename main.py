#arcade project

#import pygame library
import pygame
import sys

#imports enemy class from the enemies file
from enemies import Enemy

#initialize pygames internal variables
pygame.init()

#set up variables for thw screen size
screen_width = 640
screen_height = 480

#initialize a window with the screen size set
screen = pygame.display.set_mode((screen_width, screen_height))

#clock frame rate
clock = pygame.time.Clock()
fps = 24

#title
pygame.display.set_caption("WIZArd guy")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#images
player_image = pygame.image.load("images/player.png")
enemy_image = pygame.image.load("images/enemy.png")
coin_image = pygame.image.load("images/coin.png")
goal_image = pygame.image.load("images/goal.png")
background_image = pygame.image.load("images/background.png")

#player
player_x = 10
player_y = 40
player_width = 64
player_height = 64
player_speed = 15
score = 0
game_scene = "title"

#objects
player = pygame.Rect(player_x, player_y, player_width, player_height)
enemy = pygame.Rect(350, 300, 64, 64)
score_ui = pygame.Rect(0, 0, screen_width, 40)
goal = pygame.Rect(400, 300, goal_image.get_width(), goal_image.get_height())
background = pygame.Rect(0, 40, screen_width, screen_height)

#enemies
enemy_width = enemy_image.get_width() - 10
enemy_height = enemy_image.get_height() - 10
enemy_speed = 10

#enemy objects
enemy1 = Enemy(200, 190, enemy_width, enemy_height, enemy_speed, "h", 64, 300)
enemy2 = Enemy(200, 60, enemy_width, enemy_height, enemy_speed, "h", 200, 500)
enemy3 = Enemy(0, 120, enemy_width, enemy_height, enemy_speed, "v", 120, 300)
enemy4 = Enemy(450, 120, enemy_width, enemy_height, enemy_speed, "v", 120, 320)

enemies = [enemy1, enemy2, enemy3, enemy4]

#coins
coin_width = coin_image.get_width()
coin_height = coin_image.get_height()

coins = [
    pygame.Rect(300, 100, coin_width, coin_height),
    pygame.Rect(400, 100, coin_width, coin_height),
    pygame.Rect(400, 400, coin_width, coin_height),
    pygame.Rect(300, 300, coin_width, coin_height)
]
#colors
player_color = (95, 235, 128)
bg_color = (67, 89, 87) #weird
text_color = (255, 255, 255)
ui_color = (0, 0, 0)
title_color = (132, 12, 176)
game_over_color = (204, 0, 0)
you_win_color = (34, 133, 50)

#game font
game_font = pygame.font.SysFont("", 30)
title_font = pygame.font.SysFont("", 60)


#=======================
#      FUNCTIONS
#========================

def draw_sprites():
    global game_scene
    screen.blit(background_image, background)
    screen.blit(player_image, player)

    draw_enemies()

    draw_coins()

    screen.blit(goal_image, goal)

    pygame.draw.rect(screen, ui_color, score_ui)
    if player.colliderect(goal):
        #sys.exit()
        game_scene = "you_win"

    draw_text(("Score: " + str(score)), game_font, text_color, 10, 10)


def draw_enemies():
    global game_scene, enemy_speed
    for enemy in enemies:
        screen.blit(enemy_image, enemy.rect)
        e_move = enemy.speed
        #h direction
        if enemy.direction == "h":
            enemy.rect.x += e_move
            if enemy.rect.x <= enemy.start or enemy.rect.x >= enemy.end:
                enemy.speed = -e_move
        #vertical
        elif enemy.direction == "v":
            enemy.rect.y += e_move
            if enemy.rect.y <= enemy.start or enemy.rect.y >= enemy.end:
                enemy.speed = -e_move


    #collision
    for enemy in enemies:
        if player.colliderect(enemy.rect):
           # sys.exit()
            game_scene = "game_over"


def draw_coins():
    for coin in coins:
        screen.blit(coin_image, (coin[0], coin[1], coin[2], coin[3]))
        #screen.blit(coin_image, (coin[2], coin[3]))

    global score

    for coin in coins:
        if coin.colliderect(player):
            coins.remove(coin)
            score += 1
           # print(score)
        # if key[pygame.K_SPACE] and game_scene == "level":
        #     score = 0
        #     coins.append(coin)


def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

def game_setup():
    global player_x, player_y, player, score, coins
    player_x = 10
    player_y = 40
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    coins = [
        pygame.Rect(300, 100, coin_width, coin_height),
        pygame.Rect(400, 100, coin_width, coin_height),
        pygame.Rect(400, 400, coin_width, coin_height),
        pygame.Rect(300, 300, coin_width, coin_height)
    ]
    score = 0

#==========================
#===== MAIN GAME LOOP =====
#==========================
while True:
    #tick at 24 fps
    clock.tick(fps)


    #this loop gets any keyboard mouse or other events that happaen from user input
    for event in pygame.event.get():
        #the pygame quit event happens when you close the window
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_scene == "title":
                    game_scene = "level"
                elif game_scene == "game_over" or game_scene == "you_win":
                    game_scene = "title"

            #press key
        key = pygame.key.get_pressed()

            #d key
        if key[pygame.K_d]:
            player.move_ip(player_speed, 0)
            if player.x >= screen_width - player_width:
                player.x = screen_width - player_width
        elif key[pygame.K_a]:
            player.move_ip(-player_speed, 0)
            if player.x <= 0:
                player.x = 0
        elif key[pygame.K_w]:
            player.move_ip(0, -player_speed)
            if player.y <= player_height / 2:
                player.y = player_height / 2
        elif key[pygame.K_s]:
            player.move_ip(0, player_speed)
            if player.y >= screen_height - player_height:
                player.y = screen_height - player_height

    if game_scene == "level":

    #fill the screen with a solid color
        #screen.fill(bg_color)

    #draw the player rect
    # pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        screen.fill(bg_color)
        draw_sprites()

    elif game_scene == "title":
        game_setup()
        screen.fill(title_color)
        draw_text("WIZard guy", title_font, text_color, 120, 175)
        draw_text("Press Space to play", game_font, text_color, 220, 250)

    elif game_scene == "game_over":
        screen.fill(game_over_color)
        draw_text("GAME OVER", title_font, text_color, 120, 175)
        draw_text("Press Space to restart", game_font, text_color, 220, 250)
        draw_text(("Final Score: " + str(score)), game_font, text_color, 240, 300)

    elif game_scene == "you_win":
        screen.fill(you_win_color)
        draw_text("YOU WIN", title_font, text_color, 120, 175)
        draw_text("Press Space to restart", game_font, text_color, 220, 250)

    #at the end of each game loop, call pygame.display.flip() to update the screen
    pygame.display.flip()