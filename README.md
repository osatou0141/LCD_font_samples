# **LCD_font_samples**
Sample files for Python class inheritance used LCD_font.


## OverView
+ ### lcdfont
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
+ ### lcdfontdraw
  Basic code for writing one number.
  Specifically, Indicates movement when writing numbers by hand.
  By the following code, You can choose which pen to use later.
  ```
  def draw_dot(self, org1, org2, color):
      pass
  ```
+ ### ~~lcdclock_MC~~

+ ### ~~lcdclock_PG~~

+ ### LCD_clocks
  Code to output digital clocks to Pygame and Minecraft worlds simultaneously using lcdfontdraw.