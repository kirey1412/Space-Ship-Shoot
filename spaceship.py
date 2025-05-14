import pygame, os
pygame.font.init()
pygame.mixer.init()
pygame.init()
WIDTH, HEIGHT = 700, 650
SW, SH = 50, 50
TX, TY = 50, 50
screen=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("Shooting Ships")

space=pygame.image.load("spacebg.png")
yellowship=pygame.image.load("yellowship.png")
redship=pygame.image.load("redship.png")

space=pygame.transform.scale(space, (WIDTH, HEIGHT))
yellowship=pygame.transform.scale(yellowship, (SW, SH))
yellowship=pygame.transform.rotate(yellowship, (90))
redship=pygame.transform.rotate(pygame.transform.scale(redship, (SW, SH)),-90)

yellowhit=pygame.USEREVENT+1
redhit=pygame.USEREVENT+2

speed=5
# print("hello")
border=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)
def handlered(key_pressed, red):
    # print("red")
    if key_pressed [pygame.K_LEFT] and red.x>border.x+border.width:
        red.x-=speed
    if key_pressed [pygame.K_UP] and red.y>0:
        red.y-=speed
    if key_pressed [pygame.K_RIGHT] and red.x<WIDTH-red.width:
        red.x+=speed
    if key_pressed [pygame.K_DOWN] and red.y<HEIGHT-red.height:
        red.y+=speed
    

def handleyellow(key_pressed, yellow):
    # print("yellow")
    if key_pressed [pygame.K_a] and yellow.x>0:
        yellow.x-=speed
    if key_pressed [pygame.K_w] and yellow.y>0:
        yellow.y-=speed
    if key_pressed [pygame.K_d] and yellow.x<border.x-yellow.width:
        yellow.x+=speed
    if key_pressed [pygame.K_s] and yellow.y<HEIGHT-yellow.height:
        yellow.y+=speed



def handlebullets(yellowbullets, redbullets, yellow, red):
    for bullet in yellowbullets:
        bullet.x+=3
        if red.colliderect(bullet):
            yellowbullets.remove(bullet)
            pygame.events.post(pygame.event.Event(redhit))
        elif bullet.x>WIDTH:
            yellowbullets.remove(bullet)
    for bullet in redbullets:
        bullet.x-=3
        if yellow.colliderect(bullet):
            redbullets.remove(bullet)
            pygame.events.post(pygame.event.Event(yellowhit))
        elif bullet.x<0:
            redbullets.remove(bullet)


def draw(yellow,red, yellowbullets, redbullets, yellowscore, redscore):
    # print("draw")
    screen.blit(space, (0,0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(yellowship, (yellow.x, yellow.y))
    screen.blit(redship, (red.x, red.y))
    # print("hello")
    for i in yellowbullets:
        pygame.draw.rect(screen, "white", i)
    for x in redbullets:
        pygame.draw.rect(screen, "red", x)
    pygame.display.update()

def main():
    yellow=pygame.Rect(50,HEIGHT/2,SW,SH)
    red=pygame.Rect(WIDTH-50, HEIGHT/2, SW, SH)
    run = True
    redbullets=[]
    yellowbullets=[]

    redscore=0
    yellowscore=0
    while run :       
        for events in pygame.event.get():
            print(events)
            if events.type==pygame.QUIT:
                pygame.quit()
                break
            if events.type==pygame.KEYDOWN:
                if events.key==pygame.K_LCTRL:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2,10,5)
                    yellowbullets.append(bullet)
                if events.key==pygame.K_RCTRL:
                    bullet=pygame.Rect(red.x,red.y+red.height//2,10,5)
                    redbullets.append(bullet)
        key_pressed=pygame.key.get_pressed()
        handlered(key_pressed, red)
        handleyellow(key_pressed, yellow)
        handlebullets(yellowbullets, redbullets, yellow, red)
        draw(yellow, red, yellowbullets, redbullets, yellowscore, redscore)
    # main()
main()