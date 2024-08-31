import arcade
from room022.room022.room022 import Game

class Middle_screen(arcade.View):
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
        arcade.draw_text("click here to move to the next room", 30, 325, arcade.color.BLACK, 45)
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print("go to 022")
        self.current_room = self.room2
        self.current_room.setup()
        self.current_room.on_draw()
        # nxt_view = Game()
        # self.window.show_view(nxt_view)