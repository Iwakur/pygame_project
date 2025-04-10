import pygame
from tkinter import *
import random
import sys
pygame.init()   
pygame.mixer.init()
pygame.joystick.init()
Tk().wm_withdraw() #to hide the main window
largeur_e=1000  
hauteur_e=900
screen = pygame.display.set_mode((largeur_e,hauteur_e))
pygame.display.set_caption("Beebebe")
player = pygame.image.load("perso_red.png")
player1 = pygame.image.load("perso_teal.png")
font = pygame.font.SysFont(None, 36)
score = 0
pygame.mixer.music.load("Boss.mp3")
pygame.mixer.music.play(-1)
player_x=(largeur_e-player.get_width())//2
player_y=(hauteur_e-player.get_height())//2
player1_x=(largeur_e-player1.get_width())//1
player1_y=(hauteur_e-player1.get_height())//1
bg_m=pygame.image.load("sol_herbe.png")
bg_s=pygame.image.load("mur.png")
v=5
running = True
old_player_x = player_x
old_player_y = player_y
quotes = {
    5: "Counted my enemies on one hand. Lost two fingers. – Lincoln",
    6: "Shared 6 donuts. FBI raided me anyway. – MLK, sugar flagged",
    7: "7 days no tweet. Constitution started crying. – Trump",
    8: "Walked 8 miles in snow. Vetoed a sandwich. – Biden",
    9: "9’s humble. 10’s how many drones I sent. – Obama, drone operator in chief",
    10: "WE HAVE GREAT TEN HERE! – Trump",
    11: "Two ones walked into Congress. Nothing changed. – Ghost of Washington",
    12: "12 agents told me no. I ate the pie AND them. – Trump, stress eating secrets",
    13: "Turkey lived. Nation didn't. – Biden, post-pardon",
    14: "One hat per scandal. Ran out by Wednesday. – Nixon, sweating",
    15: "15 mins? I filibustered for 4 years. – Trump, still talking",
    16: "Freed the slaves. Got shot. Worth it? – Honest Abe, brutally honest",
    17: "Dreamt of rock. Woke up signing debt. – Obama, strumming softly",
    18: "18 holes, 0 laws. I call that balance. – Trump, golf-over-governance",
    19: "They said don’t say it. I said it louder. – Biden, smiling",
    20: "Signed with 20 pens. Forgot what. – Bush, probably"
}


def over(a):
    quote = quotes.get(a, "meh")
    return font.render(quote, True, (255, 255, 255))

while running:

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    player_rect = player.get_rect(topleft=(player_x, player_y))
    enemy_rect = player1.get_rect(topleft=(player1_x, player1_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    for x in range(0,largeur_e, bg_m.get_width()):
        for y in range(0,hauteur_e,bg_m.get_height()):
                if (y<=hauteur_e):
                    screen.blit(bg_m,(x,y))
    for x in range(0,largeur_e, bg_s.get_width()):
        for y in range(int(hauteur_e/3*2),hauteur_e,bg_s.get_height()):
                screen.blit(bg_s,(x,y))
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_a]:
        player_x-=v
        if player_x<0:
            player_x=0
    if keys[pygame.K_d]:
        player_x+=v
        if player_x> largeur_e-player.get_width():
            player_x= largeur_e-player.get_width()
    if keys[pygame.K_w]:
        player_y-=v
        if player_y<0:
            player_y=0
    if keys[pygame.K_s]:
        player_y+=v
        if player_y> hauteur_e-player.get_height():
            player_y= hauteur_e-player.get_height()
    
    


    if keys[pygame.K_LEFT]:
        player1_x-=v
        if player1_x<0:
            player1_x=0
    if keys[pygame.K_RIGHT]:
        player1_x+=v
        if player1_x> largeur_e-player1.get_width():
            player1_x= largeur_e-player1.get_width()
    if keys[pygame.K_UP]:
        player1_y-=v
        if player1_y<0:
            player1_y=0
    if keys[pygame.K_DOWN]:
        player1_y+=v
        if player1_y> hauteur_e-player1.get_height():
            player1_y= hauteur_e-player1.get_height()
    if keys[pygame.K_LSHIFT]:
        v+=3
    if keys[pygame.K_RSHIFT]:
        v-=3
    if ( keys[pygame.K_SPACE] ) :
        print("player1_x : ",player1_x)
        print("player_x : ",player_x)
        print("player1_y : ",player1_y)
        print("player_y : ",player_y)



    if player_rect.colliderect(enemy_rect):
        score+=1
        player_rect = player.get_rect(topleft=(player_x, player_y))
        enemy_rect = player1.get_rect(topleft=(player1_x, player1_y))
        player_x = player_y =0
        player1_x = random.randint(0,largeur_e - player1.get_width())
        player1_y = random.randint(0,hauteur_e - player1.get_width())
    if score==20:
        running=False
    screen.blit(over(score), (10, 50))
    screen.blit(player,(player_x,player_y))
    screen.blit(player1,(player1_x,player1_y))
    screen.blit(score_text, (10, 10))  
    pygame.display.flip()

pygame.quit()
sys.exit()