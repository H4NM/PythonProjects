import pygame as pg
import sys
from random import random

### COLORS ##
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (165, 165, 165)
LIGHTGREY = (135, 135, 135)
DARKGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
DARKRED = (200, 0, 0)


FPS = 60
#HAS TO BE DIVIDEABLE WITH 20
WIDTH = 420
#HAS TO BE DIVIDEABLE WITH 20
HEIGHT = 420
TILESIZE = 20


class TileButton(pg.sprite.Sprite):
    def __init__(self, game, x, y, mine):
        self.groups = game.all_sprites, game.tiles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.font = pg.font.SysFont('Consolas', 5)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self._index = 0
        self.mine = mine
        if self.mine == False:
            self.game.valid_tiles += 1
        self.flagged = False
        self.activated = False
        self.adjacent_mines = 0

        

    def event_handler(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos) and self.flagged == False and self.activated == False:
                    if self.mine == True:
                        self.triggered_mines()
                    else:
                        if not self.game.status == 'initiated':
                            self.game.start_game_clock()
                        self.activated_tile()
                        
            if event.button == 3:
                if self.rect.collidepoint(event.pos):
                    self.flag_mine()
                    
                
    def flag_mine(self):
        if self.activated == False:
            self.flagged = not self.flagged
            if self.flagged == True:
                self.image.fill(RED)
            else:
                self.image.fill(DARKGREY)
            pg.display.flip()

    def triggered_mines(self):
        for tile in self.game.tiles:
            if tile.mine == True:
                tile.image.fill(BLACK)
                self.game.paused = True
                self.game.status = 'Lost'
                
                pg.display.flip()

    def activated_tile(self):
        self.activated = True
        self.game.triggered_tiles += 1
        self.image.fill(GREY)
        
        if not self.check_for_mines():
            self.check_adjacent()
            

    def update(self):
        
        pg.display.update()



    def draw_adjacent_number(self):
        (x,k,y,j) = self.rect
        self._recttemp = ((x+6), (k+3), y,j)
        
        if self.adjacent_mines == 1:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, BLUE)
            self.game.screen.blit(text_surface, self._recttemp)
            
        elif self.adjacent_mines == 2:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, GREEN)
            self.game.screen.blit(text_surface, self._recttemp)
            
        elif self.adjacent_mines == 3:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, RED)
            self.game.screen.blit(text_surface, self._recttemp)

        elif self.adjacent_mines == 4:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, PURPLE)
            self.game.screen.blit(text_surface, self._recttemp)

        elif self.adjacent_mines == 5:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, DARKRED)
            self.game.screen.blit(text_surface, self._recttemp)

        elif self.adjacent_mines == 6:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, DARKRED)
            self.game.screen.blit(text_surface, self._recttemp)

        #Most likely never going to happen, but due to the random
        #function it may still occur
        elif self.adjacent_mines == 7:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, DARKRED)
            self.game.screen.blit(text_surface, self._recttemp)

        elif self.adjacent_mines == 8:
            font = pg.font.SysFont('Consolas', 15)
            text_surface = font.render(str(self.adjacent_mines), True, DARKRED)
            self.game.screen.blit(text_surface, self._recttemp)
        


    def check_for_mines(self):
        
        self.count_adjacent_mines()
        
        for tile in self.game.tiles:
            if tile.x == (self.x + 1) and tile.y == self.y:
                if tile.mine == True:
                    return True
            if tile.x == (self.x - 1) and tile.y == self.y:
                if tile.mine == True:
                    return True
            if tile.y == (self.y + 1) and tile.x == self.x:
                if tile.mine == True:
                    return True   
            if tile.y == (self.y - 1) and tile.x == self.x:
                if tile.mine == True:
                    return True
            if tile.y == (self.y - 1) and tile.x == (self.x - 1):
                if tile.mine == True:
                    return True
            if tile.y == (self.y - 1) and tile.x == (self.x + 1):
                if tile.mine == True:
                    return True
            if tile.y == (self.y + 1) and tile.x == (self.x - 1):
                if tile.mine == True:
                    return True
            if tile.y == (self.y + 1) and tile.x == (self.x + 1):
                if tile.mine == True:
                    return True
        return False

    def count_adjacent_mines(self):
        
        self.adjacent_mines = 0

        for tile in self.game.tiles:
            if tile.x == (self.x + 1) and tile.y == self.y:
                if tile.mine == True:
                    self.adjacent_mines += 1
            if tile.x == (self.x - 1) and tile.y == self.y:
                if tile.mine == True:
                    self.adjacent_mines += 1                    
            if tile.y == (self.y + 1) and tile.x == self.x:
                if tile.mine == True:
                    self.adjacent_mines += 1  
            if tile.y == (self.y - 1) and tile.x == self.x:
                if tile.mine == True:
                    self.adjacent_mines += 1
            if tile.y == (self.y - 1) and tile.x == (self.x - 1):
                if tile.mine == True:
                    self.adjacent_mines += 1
            if tile.y == (self.y - 1) and tile.x == (self.x + 1):
                if tile.mine == True:
                    self.adjacent_mines += 1
            if tile.y == (self.y + 1) and tile.x == (self.x - 1):
                if tile.mine == True:
                    self.adjacent_mines += 1
            if tile.y == (self.y + 1) and tile.x == (self.x + 1):
                if tile.mine == True:
                    self.adjacent_mines += 1
                


    def check_adjacent(self):
        
        for tile in self.game.tiles:
            
            tile_condition = (tile.activated == False and tile.mine == False and tile.flagged == False)

            if tile.x == (self.x + 1) and tile.y == self.y:
                if tile_condition:
                    tile.activated_tile()
            elif tile.x == (self.x - 1) and tile.y == self.y:
                if tile_condition:
                    tile.activated_tile()
            elif tile.y == (self.y + 1) and tile.x == self.x:
                if tile_condition:
                    tile.activated_tile()
            elif tile.y == (self.y - 1) and tile.x == self.x:
                if tile_condition:
                    tile.activated_tile()
            elif tile.y == (self.y - 1) and tile.x == (self.x - 1):
                if tile_condition:
                    tile.activated_tile()
            elif tile.y == (self.y - 1) and tile.x == (self.x + 1):
                if tile_condition:
                    tile.activated_tile()
            elif tile.y == (self.y + 1) and tile.x == (self.x - 1):
                if tile_condition:
                    tile.activated_tile()
            elif tile.y == (self.y + 1) and tile.x == (self.x + 1):
                if tile_condition:
                    tile.activated_tile()

            

            
          
                    






class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Minesweeper')
        self.clock = pg.time.Clock()

    def start_game_clock(self):
        self.start_ticks=pg.time.get_ticks()
        self.status = 'initiated'
        

                           
    def run(self):
        self.playing = True

        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            
            self.update()
            self.draw()
            self.events()

            if self.triggered_tiles == self.valid_tiles:
                self.status = 'Won'
                self.paused = True
                

               

    def start_screen(self):
        pass

    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        self.paused = False
        self.triggered_tiles = 0
        self.valid_tiles = 0
        self.status = ''
        self.seconds = 0
    
        self.add_tiles()
        


    def add_tiles(self):

        for x in range(1, int((WIDTH/TILESIZE)-1)):
            for y in range(2, int((HEIGHT/TILESIZE)-1)):
                if random()>0.9:
                    TileButton(self, x, y, True)
                else:
                    TileButton(self, x, y, False)
        
    def draw_text(self, text, size, color, x,y):
        font = pg.font.SysFont('Consolas', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

        

    def update(self):
        self.all_sprites.update()
        


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    pass
            for tile in self.tiles:
                if self.paused == False:
                    tile.event_handler(event)

    
    def game_clock(self):

        if self.status == 'initiated' or self.status == 'Won' or self.status == 'Lost':
            seconds=(pg.time.get_ticks()- self.start_ticks)/1000
            self.draw_text('Time: {}'.format(str(int(round(self.seconds, 0)))), 10, WHITE, (WIDTH * 4/5), 20)
        else:
            self.draw_text('Time: {}'.format(str(int(round(self.seconds, 0)))), 10, WHITE, (WIDTH * 4/5), 20)
            

    def draw(self):
        pg.Surface.fill(self.screen, BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_tiles()

        if self.paused == False and self.status == 'initiated':
            self.seconds=(pg.time.get_ticks()- self.start_ticks)/1000

        self.game_clock()

        for sprite in self.all_sprites:
            if isinstance(sprite, TileButton):
                sprite.draw_adjacent_number()
                
        
        if self.paused == True and self.status == 'Lost':
            self.draw_text('Game Over', 20, RED, (WIDTH/2), 20)
        elif self.paused == True and self.status == 'Won':
            self.draw_text('You Won', 20, GREEN, (WIDTH/2), 20)
            

            
        
        pg.display.flip()

    def draw_tiles(self):
        for x in range(20, (WIDTH), TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x,40),(x, HEIGHT-20))
        for y in range(40, (HEIGHT), TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (20,y),(WIDTH-20, y))
        
    
    def quit(self):
        pg.quit()
        sys.exit()



g = Game()
g.start_screen()

while True:
    g.new()
    g.run()
