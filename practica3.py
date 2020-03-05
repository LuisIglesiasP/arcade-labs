import arcade



def draw_puerta():
    arcade.draw_rectangle_filled(300, 320, 175, 350, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(360, 290, 10, arcade.csscolor.GOLD)
def draw_suelo():
    arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.csscolor.PERU)
def draw_ventana():
    arcade.draw_rectangle_filled(275, 440, 45, 45, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(275, 385, 45, 45, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(328, 440, 45, 45, arcade.csscolor.LIGHT_BLUE)
    arcade.draw_rectangle_filled(328, 385, 45, 45, arcade.csscolor.LIGHT_BLUE)


def draw_cuadro():
    arcade.draw_rectangle_filled(500, 450, 150, 100, arcade.csscolor.AQUA)
    #colgandero del cuadro
    arcade.draw_triangle_outline(425, 500, 575, 500, 500, 525, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(500, 523, 3, arcade.csscolor.DARK_KHAKI)
    # relleno cuadro
    arcade.draw_rectangle_filled(500, 450, 75, 75, arcade.csscolor.GREEN)
    arcade.draw_rectangle_filled(482, 464, 20, 20, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(518, 464, 20, 20, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(500, 443, 18, 27, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(510, 433, 10, 27, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(490, 433, 10, 27, arcade.csscolor.BLACK)
    # cuadro marco
    arcade.draw_rectangle_filled(500, 400, 158, 5, arcade.csscolor.DARK_ORANGE)
    arcade.draw_rectangle_filled(500, 500, 158, 5, arcade.csscolor.DARK_ORANGE)
    arcade.draw_rectangle_filled(577, 450, 5, 105, arcade.csscolor.DARK_ORANGE)
    arcade.draw_rectangle_filled(423, 450, 5, 105, arcade.csscolor.DARK_ORANGE)

def ball(x,y):
    arcade.draw_circle_filled(x, y, 50, arcade.csscolor.CRIMSON)

def on_draw(delta_time):
    arcade.start_render()
    draw_suelo()
    draw_puerta()
    draw_ventana()
    draw_cuadro()
    ball(on_draw.ball, 140)
    on_draw.ball += -25
on_draw.ball = 599
def main():
    arcade.open_window(600, 600, 'Drawing example')
    arcade.set_background_color(arcade.csscolor.BEIGE)
    arcade.schedule(on_draw, 1/400)
    arcade.run()
main()