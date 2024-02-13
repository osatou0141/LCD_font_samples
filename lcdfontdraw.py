import lcdfont

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


class LcdFontDraw():
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
        i = 0
        for y in range(7):
            for x in range(5):
                if lcdfont.LCD_font_styles[int(code)][i] == 1:
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
                i += 1


    def draw_dot(self, org1, org2, color):
        pass