import pygame
import pygame.freetype
from pygame.locals import Rect
from lcdfontdraw import LcdFontDraw
from datetime import datetime

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200

FONT_COLOR = GREEN
BACK_COLOR = GRAY

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LCD font")
clock = pygame.time.Clock()
font1 = pygame.freetype.Font("fonts/natumemozi.ttf", 48)


class LcdFontDrawPG(LcdFontDraw):
    def draw_dot(self, org1, org2, color):
        pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], self.BLOCK_SIZE, self.BLOCK_SIZE))


lcd = LcdFontDrawPG(screen)
lcd.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=FONT_COLOR, COLOR_OFF=BACK_COLOR)
lcd.init_row(X_ORG=8, Y_ORG=8, Z_ORG=0, COL_INTV=6)


running = True
while running:
    dt_now = datetime.now()
    screen.fill(BACK_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    lcd.update_col(col=0, code=dt_now.hour // 10)
    lcd.update_col(col=1, code=dt_now.hour % 10)
    lcd.update_col(col=2, code=10)
    lcd.update_col(col=3, code=dt_now.minute // 10)
    lcd.update_col(col=4, code=dt_now.minute % 10)
    lcd.update_col(col=5, code=10)
    lcd.update_col(col=6, code=dt_now.second // 10)
    lcd.update_col(col=7, code=dt_now.second % 10)
    pygame.display.update()
    clock.tick(60)
