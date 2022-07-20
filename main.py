# import random
import pygame
import sys

# width of the box is 354 and heigth of the box in 378 

pygame.init()

darkwhite = (225, 217, 209)

# width and height of the screen

width = 450
height = 500


display = pygame.display.set_mode((width,height))

pygame.display.set_caption("Tic Tac Toe")

icon = pygame.image.load("assets/images/icon.png")
pygame.display.set_icon(icon)

def gameloop():
    try:
        # space between updown down right and left of the box played in the center :- this is the bigger on box played place at the center
        boxwidthspace = 96
        boxheightspace = 122

        # defining the width and height of the box for making the the 9 box
        boxwidth = abs(width-boxwidthspace)
        boxheight = abs(height-boxheightspace)

        #defining the first box co-ordinates and size of the box
        boxx = boxwidthspace/2
        boxy = boxheightspace/2
        boxsizex = boxwidth/3
        boxsizey = boxheight/3

        # creating the boxlist means this list will contain the co-ordinates of all the boxes
        boxlist = []
        for i in range(3):
            for j in range(3):
                boxlist.append({
                    "x":boxx,
                    "y":boxy,
                    # value is nothing but the x and 0 which will later displayed on the screen
                    "value":""
                })
                boxx+=boxsizex
            boxy+=boxsizey
            boxx=boxwidthspace/2
        
        # player1 and player2 to store the user events  means:- in the box the user has placed the x or 0
        player1 = []
        player2 = []

        # all the conditions to win
        wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        # details of both the player whether they have won or not
        infos = [{"player1":False,"selected":player1},{"player2":False,"selected":player2}]

        exit_game = False
        turn = "x"
        occupied = []
        game_over = False

        # playing the song


    # creating the game loop here
        while not exit_game:
            # result of the game over here

            if game_over:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_SPACE:
                            gameloop()
                display.fill(darkwhite)

                # changing the text according to the player who won the match
                text = "Match-Draw"
                if infos[0]["player1"]:
                    text = "Player 1 won - X"
                if infos[1]["player2"]:
                    text = "Player 2 won - 0"
                
                # write function description in the function
                write(display,text,60,"blue",70,70)
                write(display,"Press Space Bar To Restart",40,"black",70,140)
                write(display,"The Game!",40,"black",70,200)
                display.blit(pygame.transform.scale(icon,(200,200)),(70,270))
                    
            else:
                # working with the events
                for e in pygame.event.get():
                    if not pygame.mixer.music.get_busy():
                        playmusic("assets/audio/music.mp3")
                    if e.type == pygame.QUIT:
                        sys.exit()
                    if e.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        for i in range(len(boxlist)):
                            if pos[0]>boxlist[i]["x"] and pos[0]<boxlist[i]["x"]+boxsizex and pos[1]>boxlist[i]["y"] and pos[1]<boxlist[i]["y"]+boxsizey:
                                playmusic("assets/audio/ting.mp3")
                                if not occupied.__contains__(i):
                                    boxlist[i].update({
                                        "value":turn
                                    })
                                    if turn=="x":
                                        turn = "0"
                                        player1.append(i)
                                        
                                    else:
                                        turn = "x"
                                        player2.append(i)
                                    occupied.append(i)

                display.fill(darkwhite)
                pygame.draw.rect(display,darkwhite,(boxx,boxy,boxwidth,boxheight),2)

                # drawing all the boxes on the screen and display the x and 0 in it.
                for i in range(len(boxlist)):
                    pygame.draw.rect(display,"blue",(boxlist[i]["x"],boxlist[i]["y"],boxsizex,boxsizey),2)
                    write(display,boxlist[i]["value"],80,"red",boxlist[i]["x"]+40,boxlist[i]["y"]+40)

                # checking the user input and decalring whether the user has won or not
                for k in range(len(infos)):
                    for i in range(len(wins)):
                        count = 0
                        for j in range(len(infos[k]["selected"])):
                            if wins[i].__contains__(infos[k]["selected"][j]):
                                count+=1
                            if count==len(wins[0]):
                                index = k+1
                                infos[k].update({
                                    f"player{index}":True
                                })
                                break

                for i in range(len(infos)):
                    index = i+1
                    if infos[i][f"player{index}"]:
                        game_over=True
                        playmusic("assets/audio/gameover.mp3")
                        
                    
                # checking whether all the boxes are occupied or not if yes then the game is over
                if len(occupied)==len(boxlist):
                    if not infos[0]["player1"] and  not infos[1]["player2"]:
                        game_over=True
                        playmusic("assets/audio/gameover.mp3")

            # updating the display over here
            pygame.display.update()
    except Exception as e:
        print("Sorry some error occurred!")

# write function to display text on the screen
def write(display,text,size,color,textx,texty):
    # creating the font and text and rendering it
    font = pygame.font.SysFont(None,size)
    text = font.render(text,True,color)
    display.blit(text,(textx,texty))

# function to play the music 
def playmusic(name):
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()




# running game

gameloop()


