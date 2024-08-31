import arcade
from room114 import Classroom, is_exist
from room022.room022.room022 import Game

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "room 114"

class Root(arcade.Window):
    def __init__(self):
        # set up window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # go to the starting view: classroom
        current_view = Start_screen()
        self.show_view(current_view)

    def setup(self):
        pass 

class Start_screen(arcade.View):
    def __init__(self):
        super().__init__()
        self.current_room = None

    def setup(self):
        pass

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("click here to start", 250, 325, arcade.color.BLACK, 50)
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        nxt_view = Classroom()
        self.window.show_view(nxt_view)

if __name__ == "__main__":
    # main114()
    window = Root()
    window.setup()
    arcade.run()