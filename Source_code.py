import pygame,sys,os
os.chdir(os.path.dirname(sys.argv[0]))
from random import randint
pygame.init()
pygame.display.set_caption("Tik Tac Toe")
pygame.display.set_icon(pygame.image.load("image/icon.ico"))
width = 450
height = 500
screen = pygame.display.set_mode((width,height))

fps = 60
clock = pygame.time.Clock()
turn = randint(0,1)
maingame  = False
counter = 0
l = []
win_list = [0,1,2,3,4,5,6,7,8]
win_timer= "no"
winner = "None"
mouseclick = True

def checkrestart():
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(yes_text,(yes_text_rect))
    screen.blit(no_text,(no_text_rect))
    if yes_text_rect.collidepoint(mouse_pos):
        screen.blit(yes_text_with_BG,yes_text_with_BG_rect)
    if no_text_rect.collidepoint(mouse_pos):
        screen.blit(no_text_with_BG,no_text_with_BG_rect)
    
def checkturn():
    counter = len(l)
    return counter
def checkwin():
    global win_timer
    global winner
        
    def win_text(who):
        global win_timer
        global winner
        global mouseclick
        if who == "O":
            winner_text = win_font.render("Winner is O" ,False,"blue",(117, 116, 110))
            winner_text_rect = winner_text.get_rect(center =(225,100))
            screen.blit(winner_text,winner_text_rect)
            screen.blit(Black_surface,Black_surface_rect)
            screen.blit(winner_chicken_dinner_text,winner_chicken_dinner_text_rect)
        elif who == "X":
            winner_text = win_font.render("Winner is X" ,False,"red",(117, 116, 110))
            winner_text_rect = winner_text.get_rect(center =(225,100))
            screen.blit(winner_text,winner_text_rect)
            screen.blit(Black_surface,Black_surface_rect)
            screen.blit(winner_chicken_dinner_text,winner_chicken_dinner_text_rect)
        elif who == "Draw":
            draw_text = win_font.render("It's a Draw!",False,"black",(117, 116, 110))
            draw_text_rect = draw_text.get_rect(center =(225,100))
            screen.blit(draw_text,draw_text_rect)
            screen.blit(Black_surface,Black_surface_rect)
            
        mouseclick = False
        win_timer = "yes"
        winner = who
        
        
    #0 1 2
    #3 4 5 
    #6 7 8       
    def check(obj):
        if obj == "O":
            winner = "O"
        else:
            winner = "X"
        return winner
    if win_list[0] == win_list[3] == win_list[6]:
        obj = win_list[0]
        who = check(obj)
        win_text(who)
    elif win_list[1] == win_list[4] == win_list[7]:
        obj = win_list[1]
        who = check(obj)
        win_text(who)
    elif win_list[2] == win_list[5] == win_list[8]:
        obj = win_list[2]
        who = check(obj)
        win_text(who)
    elif win_list[0] == win_list[1] == win_list[2]:
        obj = win_list[0]
        who = check(obj)
        win_text(who)
    elif win_list[3] == win_list[4] == win_list[5]:
        obj = win_list[3]
        who = check(obj)
        win_text(who)
    elif win_list[6] == win_list[7] == win_list[8]:
        obj = win_list[6]
        who = check(obj)
        win_text(who)
    elif win_list[0] == win_list[4] == win_list[8]:
        obj = win_list[0]
        who = check(obj)
        win_text(who)
    elif win_list[2] == win_list[4] == win_list[6]:
        obj = win_list[2]
        who = check(obj)
        win_text(who)
    elif counter == 9 and winner == "None":   
        winner = "Draw"
        win_text(winner)    
def reload_game():
    if reload_cursor == "touch":
        reload_image_bg = pygame.surface.Surface((35,35))
        reload_image_bg.fill((117, 116, 110))
    else:
        reload_image_bg = pygame.surface.Surface((35,35))
        
    reload_image_bg_rect = reload_image_bg.get_rect(center = (425,470))
    screen.blit(reload_image_bg,reload_image_bg_rect)
    screen.blit(reload_image,reload_image_rect)
    return reload_image_bg_rect
def starting_stage_setup():
    global maingame
    space_press_sound.play()
    maingame = True
    for i in square_rect_list:
        screen.blit(square,i)
        screen.blit(Black_surface,Black_surface_rect)
#starting page
title_font = pygame.font.Font(None,150)
text_2_font = pygame.font.Font(None,30)
text_font = pygame.font.Font(None,50)
answer_font = pygame.font.Font(None,70)
win_font = pygame.font.Font(None,90)
Title_1_1 = title_font.render("Tik",False,"red")
Title_1_1_rect = Title_1_1.get_rect(center =(116,125))
Title_1_2 = title_font.render("Tac",False,"blue")
Title_1_2_rect = Title_1_2.get_rect(center =(216,225))
Title_1_3 = title_font.render("Toe",False,"black")
Title_1_3_rect = Title_1_3.get_rect(center =(316,325))
text_2 = text_2_font.render("Press Space To Start!",False,"white")
text_2_rect = text_2.get_rect(center =(225,470))
Black_surface = pygame.surface.Surface((450,60))
Black_surface_rect = Black_surface.get_rect(center = (225,470))
Grey_surface = pygame.surface.Surface((450,500))
Grey_surface.fill("grey")
Grey_surface_rect = Grey_surface.get_rect(center = (225,250))
text_3 = text_2_font.render("X Red Turns!",False,"red")
text_3_rect = text_3.get_rect(center =(225,470))
text_4 = text_2_font.render("O Blue Turns!",False,"blue")
text_4_rect = text_4.get_rect(center =(225,470))
winner_chicken_dinner_text = text_2_font.render("Winner Winner Chicken Dinner!" ,False,"gold")
winner_chicken_dinner_text_rect = winner_chicken_dinner_text.get_rect(center =(225,470))

#restart page
text_5 = text_font.render("Wanna Play Again?",False,"red")
text_5_rect = text_5.get_rect(center =(225,200))
text_6 = text_font.render("Wanna Play Again?",False,"blue")
text_6_rect = text_5.get_rect(center =(225,200))
yes_text = answer_font.render("YES",False,"red")
yes_text_rect = yes_text.get_rect(center = (132.5,300))
yes_text_with_BG = answer_font.render("YES",False,"red","blue")
yes_text_with_BG_rect = yes_text_with_BG.get_rect(center = (132.5,300))
no_text = answer_font.render("NO",False,"blue")
no_text_rect = no_text.get_rect(center = (317.5,300))
no_text_with_BG = answer_font.render("NO",False,"blue","red")
no_text_with_BG_rect = no_text_with_BG.get_rect(center = (317.5,300))
text = [text_5,text_6]
text_index = 0

#images
reload_image = pygame.transform.scale(pygame.image.load("image/reload.png").convert_alpha(),(35,35))
reload_image_rect = reload_image.get_rect(center = (425,470))
reload_cursor = "not_touch"
#music
BG_music = pygame.mixer.Sound("music/bg_music.mp3")
BG_music.set_volume(0.5)
BG_music.play(-1)
Click_sound = pygame.mixer.Sound("music/click_sound.WAV")
space_press_sound = pygame.mixer.Sound("music/start_click_sound.WAV")
#Timers
winner_timer = pygame.USEREVENT + 1 


class objects(pygame.sprite.Sprite):
    def __init__(self,shape,coordinates):
        super().__init__()
        if shape == "circle":
            self.image = pygame.transform.scale(pygame.image.load("image/Blue circle png.png").convert_alpha(),(90,90))    
            self.rect = self.image.get_rect(center = coordinates)
        else:
            self.image = pygame.transform.scale(pygame.image.load("image/red cross.png").convert_alpha(),(90,90))
            self.rect = self.image.get_rect(center = coordinates)
            
            
square = pygame.surface.Surface((150,150))
square.fill("grey")
square_rect_list = []
square_coordinates = [(75,75),(225,75),(375,75),(75,225),(225,225),(375,225),(75,375),(225,375),(375,375)]
for i in range(0,9):
    square_rect_list.append(square.get_rect(center = (square_coordinates[i])))
for i in square_rect_list:
        screen.blit(square,i)
# object = pygame.sprite.Group()
# object.add(objects(choice(["circle","cross"]),coordinates))

while True :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if maingame:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                for i in square_rect_list:
                    mouse = pygame.mouse.get_pos()
                    
                    if i not in l:  
                        if mouseclick:
                            if i.collidepoint(mouse):
                                
                                coordinates = (i.x+75,i.y+75)
                                object = pygame.sprite.Group()
                                if turn:  
                                    object.add(objects(("circle"),coordinates))
                                else:   
                                    object.add(objects(("cross"),coordinates))
                                object.draw(screen)
                                l.append(i)
                                Click_sound.play()
                                counter += 1
                                win_list_index = square_rect_list.index(i)
                                if turn:
                                    win_list.insert(win_list_index,"O")
                                    win_list.pop(win_list_index+1)
                                    turn = False       
                                else:
                                    win_list.insert(win_list_index,"X")
                                    win_list.pop(win_list_index+1)
                                    turn = True 
                checkturn()
            if winner != None :
                    timer = pygame.time.set_timer(winner_timer,1500)    
            
            if reload_game().collidepoint(pygame.mouse.get_pos()):
                reload_cursor = "touch"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouseclick:
                        l.clear()
                        space_press_sound.play()
                        win_list = [0,1,2,3,4,5,6,7,8]
                        win_timer = 0
                        maingame = True
                        for i in square_rect_list:
                            screen.blit(square,i)
                        counter = 0
                        winner = "None"
            else:
                reload_cursor = "no_touch"
        if win_timer == "yes":
            if event.type == winner_timer:
                timer = pygame.time.set_timer(winner_timer,0)    
                maingame = None        
        if maingame == None:
            l.clear()
            mouse_p = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and yes_text_with_BG_rect.collidepoint(mouse_p):
                l.clear() 
                space_press_sound.play()
                win_list = [0,1,2,3,4,5,6,7,8]
                win_timer = 0
                maingame = True
                for i in square_rect_list:
                    screen.blit(square,i)
                counter = 0
                winner = "None"
                mouseclick = True
            if event.type == pygame.MOUSEBUTTONDOWN and no_text_with_BG_rect.collidepoint(mouse_p):
                pygame.quit()
                sys.exit()
        if maingame == False:
            mouse_p = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            if Black_surface_rect.collidepoint(mouse_p):
                
                if event.type == pygame.MOUSEBUTTONDOWN :
                    starting_stage_setup()
            
    if maingame:                
        
        if turn:  
            
            screen.blit(Black_surface,Black_surface_rect)
            screen.blit(text_4,text_4_rect)
            reload_game()
              
        else:   
            
            screen.blit(Black_surface,Black_surface_rect)
            screen.blit(text_3,text_3_rect)
            reload_game()  
            
           
        line_1 = pygame.draw.line(screen,"black",(151,0),(151,459),3)
        line_2 = pygame.draw.line(screen,"black",(301,0),(301,459),3)
        line_3 = pygame.draw.line(screen,"black",(0,151),(459,151),3)
        line_4 = pygame.draw.line(screen,"black",(0,301),(459,301),3)
        checkwin()
        
        
    elif maingame == None:
        if text_index < 2:
            text_index += 0.04
        if text_index >= 2 :
            text_index = 0
        screen.blit(Grey_surface,Grey_surface_rect)
        screen.blit(text[int(text_index)],text_5_rect)
        screen.blit(Black_surface,Black_surface_rect)
        screen.blit(winner_chicken_dinner_text,winner_chicken_dinner_text_rect)
        if winner == "O":
            winner_text_blue = win_font.render("Winner is O" ,False,"blue")
            winner_text_rect = winner_text_blue.get_rect(center =(225,100))
            screen.blit(winner_text_blue,winner_text_rect)
        elif winner == "X":
            winner_text_red = win_font.render("Winner is X" ,False,"red")
            winner_text_rect = winner_text_red.get_rect(center =(225,100))  
            screen.blit(winner_text_red,winner_text_rect)
        elif winner == "Draw":
            draw_text = win_font.render("It's a Draw!",False,"black")
            draw_text_rect = draw_text.get_rect(center =(225,100))
            no_winner_chicken_dinner_text = text_2_font.render("No Winner No Chicken Dinner! :(" ,False,"gold")
            no_winner_chicken_dinner_text_rect = no_winner_chicken_dinner_text.get_rect(center =(225,470))
            screen.blit(draw_text,draw_text_rect)
            screen.blit(Black_surface,Black_surface_rect)
            screen.blit(no_winner_chicken_dinner_text,no_winner_chicken_dinner_text_rect)
        checkrestart()
        
        
        
    elif maingame == False:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and maingame != True:
            starting_stage_setup()
        else:
            screen.blit(Title_1_1,(Title_1_1_rect))       
            screen.blit(Title_1_2,(Title_1_2_rect))    
            screen.blit(Title_1_3,(Title_1_3_rect))  
            screen.blit(text_2,(text_2_rect))  

    
    pygame.display.update()
    clock.tick(fps)
