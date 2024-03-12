import pygame
import pygame.freetype
from lcdfontdraw import LcdFontDraw
import param_MCJE as param
from mcje.minecraft import Minecraft
from datetime import datetime

pygame.init()

mc = Minecraft.create(port=param.PORT_MC)


class LcdFontDrawMC(LcdFontDraw):
    def draw_dot(self, org1, org2, color):
        mc.setBlock(org2[0], org2[1], org2[2], color)


lcd = LcdFontDrawMC(mc)
lcd.init_col(BLOCK_SIZE=1, BLOCK_INTV=1, COLOR_ON=param.DIAMOND_BLOCK, COLOR_OFF=param.AIR)
lcd.init_row(X_ORG=0, Y_ORG=100, Z_ORG=0, COL_INTV=6)

running = True
while running:
    dt_now = datetime.now()
    lcd.update_col(col=0, code=dt_now.hour // 10)
    lcd.update_col(col=1, code=dt_now.hour % 10)
    lcd.update_col(col=2, code=10)
    lcd.update_col(col=3, code=dt_now.minute // 10)
    lcd.update_col(col=4, code=dt_now.minute % 10)
    lcd.update_col(col=5, code=10)
    lcd.update_col(col=6, code=dt_now.second // 10)
    lcd.update_col(col=7, code=dt_now.second % 10)
