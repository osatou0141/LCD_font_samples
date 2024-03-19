import pygame
from pygame.locals import Rect
from datetime import datetime

with open("fonts/LCDfont_5x7.txt", encoding="utf-8") as f:
    LCD_font_styles = f.read().split('\n')

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


class LCD_font():
    def __init__(self, screen):
        self.screen = screen

    def init_col(self, BLOCK_SIZE, BLOCK_INTV, COLOR_ON, COLOR_OFF):
        self.BLOCK_SIZE = BLOCK_SIZE
        self.BLOCK_INTV = BLOCK_INTV
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG, Y_ORG, Z_ORG, COL_INTV):
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        self.Z_ORG = Z_ORG
        self.COL_INTV = COL_INTV * self.BLOCK_INTV

    def update_col(self, col, code):
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[code * 7 + y][x] == "1":
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                Z = self.Z_ORG
                X = x0 + x * self.BLOCK_INTV
                Yp = y0 + y * self.BLOCK_INTV
                Ym = y0 - y * self.BLOCK_INTV
                org1 = (X, Yp, Z)
                org2 = (X, Ym, Z)
                self.draw_dot(org1, org2, color)


    def draw_dot(self, org1, org2, color):
        pass


if __name__ == "__main__":
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    FONT_COLOR = GREEN
    BACK_COLOR = GRAY

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("LCD font")
    clock = pygame.time.Clock()

    class LCD_font_MC(LCD_font):
        def draw_dot(self, org1, org2, color):
            pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], self.BLOCK_SIZE, self.BLOCK_SIZE))


    lcd = LCD_font_MC(screen)
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
