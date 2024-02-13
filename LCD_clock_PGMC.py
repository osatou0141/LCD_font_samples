import pygame
import pygame.freetype
from pygame.locals import Rect
from lcdfontdraw import LcdFontDraw
import param_MCJE as param
from mcje.minecraft import Minecraft
from datetime import datetime

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("LCD font")

clock = pygame.time.Clock()

font1 = pygame.freetype.Font("fonts/natumemozi.ttf", 48)

mc = Minecraft.create(port=param.PORT_MC)


class LcdFontDrawPG(LcdFontDraw):
    def draw_dot(self, org1, org2, color):
        pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], self.BLOCK_SIZE, self.BLOCK_SIZE))


lcd1 = LcdFontDrawPG(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=8, Y_ORG=8, Z_ORG=0, COL_INTV=6)


class LcdFontDrawMC(LcdFontDraw):
    def draw_dot(self, org1, org2, color):
        mc.setBlock(org2[0], org2[1], org2[2], color)


lcd2 = LcdFontDrawMC(mc)
lcd2.init_col(BLOCK_SIZE=1, BLOCK_INTV=1, COLOR_ON=param.DIAMOND_BLOCK, COLOR_OFF=param.AIR)
lcd2.init_row(X_ORG=0, Y_ORG=100, Z_ORG=0, COL_INTV=6)

running = True
while running:
    dt_now = datetime.now()
    screen.fill(GRAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    lcd1.update_col(col=0, code=dt_now.hour // 10)
    lcd1.update_col(col=1, code=dt_now.hour % 10)
    lcd1.update_col(col=2, code=10)
    lcd1.update_col(col=3, code=dt_now.minute // 10)
    lcd1.update_col(col=4, code=dt_now.minute % 10)
    lcd1.update_col(col=5, code=10)
    lcd1.update_col(col=6, code=dt_now.second // 10)
    lcd1.update_col(col=7, code=dt_now.second % 10)

    lcd2.update_col(col=0, code=dt_now.hour // 10)
    lcd2.update_col(col=1, code=dt_now.hour % 10)
    lcd2.update_col(col=2, code=10)
    lcd2.update_col(col=3, code=dt_now.minute // 10)
    lcd2.update_col(col=4, code=dt_now.minute % 10)
    lcd2.update_col(col=5, code=10)
    lcd2.update_col(col=6, code=dt_now.second // 10)
    lcd2.update_col(col=7, code=dt_now.second % 10)
    pygame.display.update()
    clock.tick(60)
