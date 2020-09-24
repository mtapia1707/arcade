
import arcade

def main():
    arcade.open_window(700, 700, "smile demo")
    arcade.set_background_color(arcade.color.BRIGHT_TURQUOISE)
    face = arcade.create_ellipse(350, 350, 300, 300, arcade.color.YELLOW)
    nose_points = [(250, 350), (450, 350), (350, 425)]
    nose = arcade.create_polygon(nose_points, arcade.color.SILVER)
    eye1 = arcade.create_ellipse(250, 550, 100, arcade.color.RED)
    eye2 = arcade.create_ellipse(450, 550, 100, arcade.color.ARMY_GREEN)
    arcade.start_render()

    face.draw()
    eye1.draw()
    eye2.draw()
    nose.draw()
    arcade.draw_arc_outline(350, 200, 300, 200, arcade.color.RED_PURPLE,
                            180, 360, 3)

    arcade.finish_render()

    arcade.run()
    