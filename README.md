# **Class Inheritance by LCD_font_samples**
Sample files for Python class inheritance used LCD_font.

## About Class Inheritance
  If you write "pass" in the function's content...
  ```
  # in lcdfontdraw.py

  class LcdFontDraw():
      def draw_dot(self, org1, org2, color):
          pass
  ```
  The contents can be set for each file import destination.
  ```
  # in lcdclock_MC.py

  from lcdfontdraw import LcdFontDraw

  class LcdFontDrawMC(LcdFontDraw):
    def draw_dot(self, org1, org2, color):
        mc.setBlock(org2[0], org2[1], org2[2], color)
  ```

## Files OverView
+ #### lcdfont
  This determines the shape of the numbers.
  ```
  LCD_1 = (0, 0, 1, 0, 0,
           0, 1, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 0, 1, 0, 0,
           0, 1, 1, 1, 0)
  ```
+ #### lcdfontdraw
  Basic code for writing one number.
  Specifically, it shows the movements for writing a number by hand.
+ #### lcdclock_MC
  Code to output a digital clock to the Minecraft world using lcdfontdraw.
+ #### lcdclock_PG
  Code to output a digital clock to Pygame using lcdfontdraw.
+ #### LCD_clocks
  Code to output a digital clocks to the Pygame and Minecraft worlds simultaneously using lcdfontdraw.