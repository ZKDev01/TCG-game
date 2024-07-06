import pygame as pg
from pygame import Surface

NAME = 'TCG GAME'

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

WIDTH  : int = 800
HEIGHT : int = 600

def init() -> None:
  pg.init()
  pg.display.set_caption(NAME)

  window : Surface = pg.display.set_mode( (WIDTH, HEIGHT) )

  running : bool = True
  while running:
    
    # EVENT HANDLE
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False
    
    # CLEAN WINDOW
    window.fill( WHITE )

    display_card( window=window )

    # UPDATE WINDOW
    pg.display.flip()

  pg.quit()

def display_card( window : Surface ):
  size = 100
  x = ( WIDTH - size ) // 2
  y = ( HEIGHT - size ) // 2

  pg.draw.rect( window, BLACK, [x, y, size, size], 2 )
  pg.display.flip()

