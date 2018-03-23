# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()
pygame.mixer.pre_init()


#Images
icon1 = pygame.image.load('icon1.png')
icon2 = pygame.image.load('icon2.png')
icons = [icon1, icon2]
pig_right = pygame.image.load('pig_right.png')
pig_left = pygame.image.load('pig_left.png')
pig_down = pygame.image.load('pig_down.png')
pig_up = pygame.image.load('pig_up.png')
corn = pygame.image.load('corn.png')
barn = pygame.image.load('barn.png')
mud = pygame.image.load('mud.png')
bacon = pygame.image.load('bacon.jpg')

#stages
START = 0
PLAYING = 1
PVP = 7
END = 2
WIN = 3
INS = 4
WIN1 = 5
WIN2 = 6

# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60
mud_timer1 = 0
mud_timer2 = 0
icon_timer = 0
frame = 0
ticks = 0


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)



# make walls
wall1 =  [300, 275, 200, 25]
wall2 =  [400, 450, 200, 25]
wall3 =  [150, 100, 25, 200]
wall4 =  [600, 100, 100, 100]

walls = [wall1, wall2, wall3, wall4]

#Enemy Wall


def draw_emeny():
    screen.blit(bacon, enemy)
    
    stage = START

#Make Mud
mud1 = [500, 100, 72, 70]
mud2 = [140, 400, 72, 70]
muds = [mud1, mud2]


# Sound Effects
pygame.mixer.music.load("Joy Ride.wav")
dead = pygame.mixer.Sound('squeal.wav')
squeal = pygame.mixer.Sound('dead.wav')
# SETUP
corn1 = [300, 100, 25, 55]
corn2 = [100, 500, 25, 55]
corn3 = [600, 30, 25, 55]
corn4 = [600, 500, 25, 55]
corn5 = [400, 500, 25, 55]
    
def setup():
    global player1, player2, stage, enemy, corns, win, win1, win2, vel1, vel2, player2_speed, player1_speed, score1, score2, dric1, dric2
    player1 = [50, 50, 90, 80]
    player2 =  [700, 500, 90, 80]
    enemy = [-900,0, 800, 600]
    corns = [corn1, corn2, corn3, corn4, corn5]
    stage = START
    vel1 = [0, 0]
    vel2 = [0, 0]
    player2_speed = 5
    score2 = 0
    dric2 =  2
    player1_speed = 5
    dric1 =  2
    score1 = 0
    
    win = False
    win1 = False
    win2 = False

    pygame.mixer.music.play(-1)

# Game loop
setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = INS
            elif stage == INS:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                if event.key == pygame.K_RETURN:
                    stage = PVP
            elif stage == END or stage == WIN or stage == WIN1 or stage == WIN2:
                if event.key == pygame.K_SPACE:
                    setup()
            
                    
    if stage == PLAYING or stage == PVP:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        w = pressed[pygame.K_w]
        s = pressed[pygame.K_s]
        a = pressed[pygame.K_a]
        d = pressed[pygame.K_d]

        if left:
            vel1[0] = -player1_speed
            dric1 = 2
        elif right:
            vel1[0] = player1_speed
            dric1 = 0
        else:
            vel1[0] = 0

        if up:
            vel1[1] = -player1_speed
            dric1 = 3
        elif down:
            vel1[1] = player1_speed
            dric1 = 4
        else:
            vel1[1] = 0

        if a:
            vel2[0] = -player2_speed
            dric2 = 2
        elif d:
            vel2[0] = player2_speed
            dric2 = 0
        else:
            vel2[0] = 0

        if w:
            vel2[1] = -player2_speed
            dric2 = 3
        elif s:
            vel2[1] = player2_speed
            dric2 = 4
        else:
            vel2[1] = 0   
        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING or stage == PVP:
        ''' move the player in horizontal direction '''
        player1[0] += vel1[0]
        player2[0] += vel2[0]
        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player1, w):        
                if vel1[0] > 0:
                    player1[0] = w[0] - player1[2]
                elif vel1[0] < 0:
                    player1[0] = w[0] + w[2]
            if intersects.rect_rect(player2, w):        
                if vel2[0] > 0:
                    player2[0] = w[0] - player2[2]
                elif vel2[0] < 0:
                    player2[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player1[1] += vel1[1]
        player2[1] += vel2[1]           
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player1, w):                    
                if vel1[1] > 0:
                    player1[1] = w[1] - player1[3]
                if vel1[1]< 0:
                    player1[1] = w[1] + w[3]
            if intersects.rect_rect(player2, w):                    
                if vel2[1] > 0:
                    player2[1] = w[1] - player2[3]
                if vel2[1]< 0:
                    player2[1] = w[1] + w[3]

    '''image changing'''
    frames = pig_right
    if dric1 == 2:
        frames = pig_left
    elif dric1 ==3:
        frames = pig_up
    elif dric1 == 4:
        frames = pig_down
    else:
        pass

    frames1 = pig_right
    if dric2 == 2:
        frames1 = pig_left
    elif dric2 ==3:
        frames1 = pig_up
    elif dric2 == 4:
        frames1 = pig_down
    else:
        pass
    '''mud speed burst'''
    for m in muds:
        if intersects.rect_rect(player1, m):
             mud_timer1 = 2*refresh_rate
        elif intersects.rect_rect(player2, m):
            mud_timer2 = 2*refresh_rate

        if mud_timer1 > 0:
            mud_timer1 -= 1
            player1_speed = 1
        else:
            player1_speed = 5

        if mud_timer2 > 0:
            mud_timer2 -= 1
            player2_speed = 1
        else:
            player2_speed = 5
 
            
        
    
                
    ''' here is where you should resolve player collisions with screen edges '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] + player1[3]

    if left < 0:
        player1[0] = 0
    elif right > WIDTH:
        player1[0] = WIDTH - player1[2]

    if top < 0:
        player1[1] = 0
    elif bottom > HEIGHT:
        player1[1] = HEIGHT - player1[3]

    left2 = player2[0]
    right2 = player2[0] + player2[2]
    top2 = player2[1]
    bottom2 = player2[1] + player2[3]

    if left2 < 0:
        player2[0] = 0
    elif right2 > WIDTH:
        player2[0] = WIDTH - player2[2]

    if top2 < 0:
        player2[1] = 0
    elif bottom2 > HEIGHT:
        player2[1] = HEIGHT - player2[3]

    ''' get the coins '''
     
    hit_list1 = [c for c in corns if intersects.rect_rect(player1, c)] 
    hit_list2 = [c for c in corns if intersects.rect_rect(player2, c)]
    if stage == PLAYING or stage == PVP:
        for hit in hit_list1:
            corns.remove(hit)
            score1 += 1
            squeal.play()

        for hit in hit_list2:
            corns.remove(hit)
            score2 += 1
            squeal.play()
            
        if stage == PLAYING:
            if len(corns) == 0:
                win = True
                stage = WIN
            
        if stage == PVP:
            if len(corns) == 0:
                if score1 > score2:
                    win1 = True
                    stage = WIN1
                else:
                    win2 = True
                    stage = WIN2
                
    if stage == PLAYING:
        enemy[0] += 1
        if intersects.rect_rect(player1, enemy):
            stage = END
            score1 = 0
            dead.play(1)

    if stage == START:
        ticks += 1
        if ticks % 30 == 0:
            frame = (frame + 1) % len(icons)

    
            
    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(GREEN)
    screen.blit(barn, [700, 200])
    screen.blit(frames, [player1[0], player1[1]])
    print(stage)
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for m in muds:
        locm = m[:2]
        screen.blit(mud, locm)


    for c in corns:
        loc = c[:2]
        screen.blit(corn, loc)
        
    if stage == WIN:
        screen.fill(BLACK)
        font1 = pygame.font.Font(None, 48)
        text = font1.render("You Win!", 1, RED)
        screen.blit(text, [300, 200])
        text2 = font1.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text2, [210, 500])
        
    if stage == WIN1:
        screen.fill(BLACK)
        font1 = pygame.font.Font(None, 48)
        text = font1.render("Player 1 Wins!", 1, RED)
        screen.blit(text, [300, 200])
        text2 = font1.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text2, [210, 500])

    if stage == WIN2:
        screen.fill(BLACK)
        font1 = pygame.font.Font(None, 48)
        text = font1.render("Player 2 Wins!", 1, RED)
        screen.blit(text, [300, 200])
        text2 = font1.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text2, [210, 500])

    if stage == START:
        screen.fill(BLACK)
        font1 = pygame.font.Font(None, 48)
        text1 = font1.render("Piggy Playtime!", True, WHITE)
        text2 = font1.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [275, 150])
        screen.blit(text2, [225, 200])
        screen.blit(icons[frame], [250, 300])
        
    elif stage == END:
        screen.fill(BLACK)
        font1 = pygame.font.Font(None, 48)
        text1 = font1.render("Game Over", True, WHITE)
        text2 = font1.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])

    elif stage == PLAYING:
        font2 = pygame.font.Font(None, 48)
        score_text = font2.render(str(score1), 1, BLACK)
        screen.blit(score_text, [0, 0])
        draw_emeny()

    elif stage == INS:
        screen.fill(BLACK)
        screen.blit(pig_right, [50, 250])
        screen.blit(pig_left, [600, 250])
        
        font1 = pygame.font.Font(None, 48)
        font2 = pygame.font.Font(None, 25)
        
        text = font1.render("WALL GAME OR  PLAYER VS PLAYER", 1, RED)
        keyboard = font2.render("Race against the wall moving in on you from the left!", 1, RED)
        keyboard2 = font2.render("OR", 1, RED)
        keyboard3 = font2.render("Play againt your piggy friend!", 1, RED)
        press = font2.render("press space!", 1, RED)
        press2 = font2.render("press enter!", 1, RED)
        
        screen.blit(text, [100, 100])
        screen.blit(keyboard, [170, 200])
        screen.blit(keyboard2, [370, 300])
        screen.blit(keyboard3, [250, 400])
        screen.blit(press, [330, 220])
        screen.blit(press2, [330, 420])
        
    elif stage == PVP:
        screen.blit(frames1, [player2[0], player2[1]])
        font2 = pygame.font.Font(None, 25)
        score_text1 = font2.render("Player 1 Score: " + str(score1), 1, BLACK)
        screen.blit(score_text1, [0, 0])
        font2 = pygame.font.Font(None, 25)
        score_text2 = font2.render("Player 2 Score: " + str(score2), 1, BLACK)
        screen.blit(score_text2, [650, 0])
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
