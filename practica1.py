import arcade

arcade.open_window(600, 600, 'Drawing example')
arcade.set_background_color(arcade.csscolor.BEIGE)

arcade.start_render()
# puerta
arcade.draw_rectangle_filled(300, 320, 175, 350, arcade.csscolor.SIENNA)
# suelo
arcade.draw_lrtb_rectangle_filled(0, 599, 150, 0, arcade.csscolor.PERU)
# ventanal
arcade.draw_rectangle_filled(275, 440, 45, 45, arcade.csscolor.LIGHT_BLUE)
arcade.draw_rectangle_filled(275, 385, 45, 45, arcade.csscolor.LIGHT_BLUE)
arcade.draw_rectangle_filled(328, 440, 45, 45, arcade.csscolor.LIGHT_BLUE)
arcade.draw_rectangle_filled(328, 385, 45, 45, arcade.csscolor.LIGHT_BLUE)
# pomo de la puerta
arcade.draw_circle_filled(360, 290, 10, arcade.csscolor.GOLD)
# Cuadro fondo
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

#animacion
arcade.draw_circle_filled(70,  70, 70, arcade.csscolor.CRIMSON)

arcade.finish_render()

arcade.run()
