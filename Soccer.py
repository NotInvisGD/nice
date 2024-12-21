import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

PLAYERS_VELOCITY = 7

MID_BORDER = pygame.Rect(WIDTH//2 - 25, 0, 10, HEIGHT)
GOAL_FRANCE = pygame.Rect(0, HEIGHT//2 - 100, 50, 200)
GOAL_INDIA = pygame.Rect(WIDTH - 50, HEIGHT//2 - 100, 50, 200)
PLAYER_FRANCE = pygame.Rect(200, 275, 50, 50)
PLAYER_INDIA = pygame.Rect(600, 275, 50, 50)

INITIAL_PLAYER_FRANCE_X, INITIAL_PLAYER_INDIA_X = 200, 600
INITIAL_PLAYER_FRANCE_Y= 275
INITIAL_PLAYER_INDIA_Y = INITIAL_PLAYER_FRANCE_Y

BALL_radius = 25
BALL_x = WIDTH//2 - 20
BALL_y = HEIGHT//2
BALL_speed_x = PLAYERS_VELOCITY
BALL_speed_y = PLAYERS_VELOCITY

INITIAL_BALL_X = WIDTH//2 - 20
INITIAL_BALL_Y = HEIGHT//2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invis Soccer- France vs India!")

font = pygame.font.SysFont(None, 35)
font_winner = pygame.font.SysFont(None, 60)
french_score = 0
indian_score = 0
time = 0
UPDATE_TIME = pygame.USEREVENT +1
pygame.time.set_timer(UPDATE_TIME, 111)

france_winner = font_winner.render("France wins!", True, BLACK)
india_winner = font_winner.render("India Wins!", True, BLACK)
draw = font_winner.render("Its a draw!", True, BLACK)

run = True
clock = pygame.time.Clock()

while run:
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, MID_BORDER)
    pygame.draw.rect(screen, WHITE, GOAL_FRANCE)
    pygame.draw.rect(screen, WHITE, GOAL_INDIA)
    pygame.draw.rect(screen, BLUE, PLAYER_FRANCE)
    pygame.draw.rect(screen, ORANGE, PLAYER_INDIA)
    pygame.draw.circle(screen, GOLD, (BALL_x, BALL_y), BALL_radius)
    
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and PLAYER_FRANCE.y > 0: #Move up
        PLAYER_FRANCE.y -= PLAYERS_VELOCITY
    if keys_pressed[pygame.K_s] and PLAYER_FRANCE.y < HEIGHT - PLAYER_FRANCE.height: #Move down
        PLAYER_FRANCE.y += PLAYERS_VELOCITY
    if keys_pressed[pygame.K_a] and PLAYER_FRANCE.x > 0: #Move left
        PLAYER_FRANCE.x -= PLAYERS_VELOCITY
    if keys_pressed[pygame.K_d] and PLAYER_FRANCE.x < WIDTH - PLAYER_FRANCE.width: #Move right
        PLAYER_FRANCE.x += PLAYERS_VELOCITY
    if keys_pressed[pygame.K_l] and PLAYER_INDIA.x < WIDTH - PLAYER_INDIA.width:
        PLAYER_INDIA.x += PLAYERS_VELOCITY
    if keys_pressed[pygame.K_j] and PLAYER_INDIA.x > 0:
        PLAYER_INDIA.x -= PLAYERS_VELOCITY
    if keys_pressed[pygame.K_i] and PLAYER_INDIA.y > 0:
        PLAYER_INDIA.y -= PLAYERS_VELOCITY
    if keys_pressed[pygame.K_k] and PLAYER_INDIA.y < HEIGHT - PLAYER_INDIA.height:
        PLAYER_INDIA.y += PLAYERS_VELOCITY
    
    if PLAYER_FRANCE.colliderect(GOAL_FRANCE) or PLAYER_FRANCE.colliderect(GOAL_INDIA):
        PLAYER_FRANCE.x = INITIAL_PLAYER_FRANCE_X
        PLAYER_FRANCE.y = INITIAL_PLAYER_FRANCE_Y
    if PLAYER_INDIA.colliderect(GOAL_INDIA) or PLAYER_INDIA.colliderect(GOAL_FRANCE):
        PLAYER_INDIA.x = INITIAL_PLAYER_INDIA_X
        PLAYER_INDIA.y = INITIAL_PLAYER_INDIA_Y
        
    BALL_x += BALL_speed_x
    BALL_y += BALL_speed_y
    
    BALL = pygame.Rect(BALL_x - BALL_radius, BALL_y - BALL_radius, BALL_radius * 2, BALL_radius * 2)
    
    if BALL_x - BALL_radius <= 0 or BALL_x + BALL_radius >= WIDTH:
        BALL_speed_x *= -1
    if BALL_y - BALL_radius <= 0 or BALL_y + BALL_radius >= HEIGHT:
        BALL_speed_y *= -1
        
    if PLAYER_FRANCE.colliderect(BALL):
        BALL_speed_x *= -1
        BALL_speed_y *= -1
    if PLAYER_INDIA.colliderect(BALL):
        BALL_speed_x *= -1
        BALL_speed_y *= -1
    
    if BALL.colliderect(GOAL_INDIA):
        french_score += 1
        BALL_x = INITIAL_BALL_X
        BALL_y = INITIAL_BALL_Y
        BALL_speed_x *= -1
        BALL_speed_y *= -1
    elif BALL.colliderect(GOAL_FRANCE):
        indian_score += 1
        BALL_x = INITIAL_BALL_X
        BALL_y = INITIAL_BALL_Y
        BALL_speed_x *= -1
        BALL_speed_y *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == UPDATE_TIME:
            time += 1
    
    if time >= 5400:
        if french_score > indian_score:
            screen.blit(france_winner, (WIDTH//2 - 100, HEIGHT//2 - 60))
        elif indian_score > french_score:
            screen.blit(india_winner, (WIDTH//2 - 100, HEIGHT//2 - 60))
        else:
            screen.blit(draw, (WIDTH//2 - 100, HEIGHT//2 - 60))
        pygame.display.flip()
        pygame.time.wait(2000)
        break
            
    french_score_display = font.render(f"France: {french_score}", True, BLACK)
    indian_score_display = font.render(f"India: {indian_score}", True, BLACK)
    time_display = font.render(f"Time: {time}s", True, BLACK)
    
    screen.blit(french_score_display, (10, 10))
    screen.blit(indian_score_display, (540, 10))
    screen.blit(time_display, (335, 10))
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()