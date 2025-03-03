import sys
import pygame
from pygame.locals import *

img_basic_address = './img/'


class UNOGame():
def __init__(self):
    pygame.init()
    self.background = pygame.image.load(img_basic_address+'background.png')
    self.screen_width = 800
    self.screen_height = 600
    self.background_Color = (0,66,0)
    self.playernum = 2
    self.difficulty = 1
    self.font = 'Berlin Sans FB'
    self.clock = pygame.time.Clock()
    self.FPS = 30
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("UNO!")
    self.screen.fill(self.background_Color)
    self.screen.blit(self.background, (-30, -30))
    pygame.display.update()
    self.main_menu()

def text_format(self, message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, True, textColor)
    return newText

def main_menu(self):
    menu = True
    selected = 1

    start_rect = pygame.Rect(self.screen_width/2+70, 200, 200, 50)
    set_rect = pygame.Rect(self.screen_width/2+70, 260, 200, 50)
    quit_rect = pygame.Rect(self.screen_width/2+70, 320, 200, 50)

    while menu:
        pygame.init()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if selected <=1:
                        selected = 1
                    else:
                        selected = selected-1
                elif event.key == K_DOWN:
                    if selected >=3:
                        selected = 3
                    else:
                        selected = selected+1
                if event.key == K_RETURN:
                    if selected <= 1:
                        #실행할 내용
                        pass
                    if selected == 2:
                        #실행할 내용
                        pass
                    if selected >= 3:
                        #실행할 내용
                        pass
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    if selected == 1:
                        # 실행할 내용
                         pass
                elif set_rect.collidepoint(mouse_pos):
                    if selected == 2:
                         # 실행할 내용
                          pass
                elif quit_rect.collidepoint(mouse_pos):
                    if selected == 3:
                        pygame.quit()
                        sys.exit()

        if selected == 1:
            text_start = self.text_format("START", self.font, 50, (0,0,0))
        else:
            text_start = self.text_format("START", self.font, 50, (255, 255, 255))

        if selected == 2:
            text_setting = self.text_format("SETTING", self.font, 50, (0,0,0))
        else:
            text_setting = self.text_format("SETTING", self.font, 50, (255, 255, 255))

        if selected == 3:
            text_quit = self.text_format("QUIT", self.font, 50, (0,0,0))
        else:
            text_quit = self.text_format("QUIT", self.font, 50, (255, 255, 255))

        # 메뉴 아이템 표시
        start_rect = text_start.get_rect()
        set_rect = text_setting.get_rect()
        quit_rect = text_quit.get_rect()

        start_rect.center = (self.screen_width/2+70, 200)
        set_rect.center = (self.screen_width/2+70, 260)
        quit_rect.center = (self.screen_width/2+70, 320)
       


        self.screen.blit(text_start, start_rect)
        self.screen.blit(text_setting, set_rect)
        self.screen.blit(text_quit, quit_rect)
        pygame.display.update()
        self.clock.tick(self.FPS)
        pygame.display.set_caption("UNO!")
    def main():
        game = UNOGame() 
        game.main_menu()
  if name == 'main': main()