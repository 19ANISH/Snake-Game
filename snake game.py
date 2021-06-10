import pygame
import time
import random

#here we are initializing pygame
pygame.init()

#here we will be defining colours of our own as per our requirement
white = (255,255,255)
black = (0,0,0)         #snake
red = (255,0,0)         #food

blue = (50,153,213)     #background
yellow = (255,255,102)  #score

#setting the display size
dis_width, dis_height= 700, 500
#this will be our display
display=pygame.display.set_mode((dis_width,dis_height))
#giving a title
pygame.display.set_caption("Snake Game")

#we set clock for the game for smooth running
clock = pygame.time.Clock()
#we set the size of snake
snake_size=10
#now we set the speed of snake
snake_speed=15

#now we are going to set the fonts for the messages displayed in game
message_font=pygame.font.SysFont('bold',30)

#now we set font for score of game
score_font=pygame.font.SysFont('bahnschrift',25)


#we define the 2 function for printing scores of the game and also for the snake which means making of snake

def print_score(score):
    text=score_font.render("Score: "+ str(score), True, yellow)
    display.blit(text, [0,0])

def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display,black,[x[0], x[1], snake_size, snake_size])
        #basically as we know that when snake eats the food it's size increases so we draw a extra rectangle to increase the length of snake
#def message(msg, color):
#    mesg = font_style.render(msg, True, color)
#    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#now we create 3rd function that is run game or run function
def run_game():
    #game_over is defined for the condition when the snake hits itself or it hits the border of the display/screen until then we can play the game so it false in start
    game_over = False
    game_close = False
    #game_close is defined to terminate the game, as the game is going to start in the first place when we run the program so it is false in the start

    x1 = dis_width/2
    y1 = dis_height/2
    #these 2 are the coordinates of the snake when we start the game

    x1_speed = 0
    y1_speed = 0
    #this is going to be our default speed as the game has just started
    #unless we press keys the game won't start

    #as the game is being played the snake size will increase so we define a list of pixels which is empty for now
    snake_List = []
    snake_length = 1

    #now we have to set the target for food in the display it can be randomly situtated anywhere in the display

    target_x = round(random.randrange(0, dis_width - snake_size)/10.0) * 10.0   #width-snake_size gives space to fit the snake
    target_y = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0    #hegith-snake_size gives space to fit the snake

    #we write the main loops of game from here

    while not game_over:

        while game_close == True:

            display.fill(blue)
            game_over_message = message_font.render("Game Over! "
                                                    "Press 1-Restart "
                                                    "Press 2-Quit" , True, yellow)
            display.blit(game_over_message, [dis_width / 4, dis_height / 2])
            print_score(snake_length - 1)
            #message("You Lost! Press 1-Play Again or 2-Quit", red)
            print_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_1:
                        run_game()

                #if event.type == pygame.QUIT:
                    #game_over = True
                    #game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_speed = -snake_size
                    y1_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x1_speed = snake_size
                    y1_speed = 0
                elif event.key == pygame.K_UP:
                    y1_speed = -snake_size
                    x1_speed = 0
                elif event.key == pygame.K_DOWN:
                    y1_speed = snake_size
                    x1_speed = 0

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close = True
                #this is true because game is over not quit

        x1 += x1_speed
        y1 += y1_speed

        #we are going to change the speed by each iteration and change the position

        display.fill(blue)    #this will be our background which is black colour
        pygame.draw.rect(display,red,[target_x,target_y,snake_size,snake_size])
        #this is our food/points which is to be displayed on the game screen
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        #this is done when snake eats the food so its size should increase that is its tail should increase

        #checking the case
        if len(snake_List) > snake_length:
            del snake_List[0]
            #here we delete the tail
            #we start with snake_pixel 0 and snake_length 1 so when we add pixel it's not going to delete anything
            #it's just going to move around that pixel & if we have more pixels it's going to move the head and also whole snake
            #it deletes the last pixel which makes it move and not grow automatically
            #when the food is found and it's eaten then the length is increased

        for x in snake_List[:-1]:
            if x == snake_head:
                #this is the logic when the snake hit itself
                game_close = True
        draw_snake(snake_size, snake_List)
        print_score(snake_length - 1)
            #as the default length so final length is

        pygame.display.update()

            #now we have to check that if the snake has ate the food that is food and snake face are at same position then we have to show/present new food randomly
            #and also increase the size of snake by 1

        if x1 == target_x and y1 == target_y:
            target_x = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0
                #this make new position of food
                #now increasing the snake length
            snake_length += 1
                #increasing the time that is ticking the clock

        clock.tick(snake_speed)
            #this increases the speed

    pygame.quit()
    quit()

run_game()