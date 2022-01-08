import random
import pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)

screen_width = 700
screen_height = 350

# Creating Window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Boy')


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,35)

def display_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color,snk_lst , snake_size):
    for x,y in snk_lst:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])




def game_loop():
    # Game specific variables
    global event
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_size = 20
    fps = 60
    score = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    with open('highScore.txt', 'r') as f:
        highScore = f.read()

    # Game loop
    while not exit_game:
        if game_over:
            with open('highScore.txt', 'w') as f:
                f.write(str(highScore))
            gameWindow.fill(white)
            display_score('Game Over! Press Enter to Continue', red, 120, screen_height / 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity
                    velocity_y = 0
                elif event.key == pygame.K_LEFT:
                    velocity_x = -init_velocity
                    velocity_y = 0
                elif event.key == pygame.K_UP:
                    velocity_y = -init_velocity
                    velocity_x = 0
                elif event.key == pygame.K_DOWN:
                    velocity_y = init_velocity
                    velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length+=5
                if score > int(highScore):
                    highScore = score

            gameWindow.fill(white)
            display_score('Score: ' + str(score) + '; High Score: '+ str(highScore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, (food_x, food_y, snake_size, snake_size))

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x> screen_width or snake_y<0 or snake_y> screen_height:
                game_over = True

            plot_snake(gameWindow, black,snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

game_loop()
