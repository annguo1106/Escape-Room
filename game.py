import arcade
from room022.room022.room022 import Game
from room114.room114 import Classroom
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "ESCAPE ROOM"

class roomManager(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.current_room = None
        self.current_scene = None
        self.room1 = Classroom()
        self.room2 = Game()
    
    def setup(self):
        self.current_scene = "start screen"
    
    def show_start_screen(self):
        arcade.set_background_color((102, 102, 153))
        arcade.draw_text("click here to start", 250, 325, arcade.color.BLACK, 50)
    
    def show_middle_screen(self):
        arcade.set_background_color(arcade.csscolor.DARK_BLUE_GRAY)
        arcade.draw_rectangle_filled(60, 325, 120, 650, arcade.color.PINK_PEARL)
        arcade.draw_text("click here to move to the next room", 500, 325, arcade.color.BLACK, 50)
    
    def show_end_screen(self):
        arcade.set_background_color(arcade.csscolor.DARK_BLUE_GRAY)
        arcade.draw_rectangle_filled(60, 325, 120, 650, arcade.color.PINK_PEARL)
        arcade.draw_text("congratulations! you escape the rooms!", 500, 325, arcade.color.BLACK, 50)
    
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.current_scene == "start screen":
            self.current_scene = "room 022"
            self.current_room = self.room2
            self.current_room.setup()
            self.current_room.on_draw()
            
    def on_draw(self):
        arcade.start_render()
        if self.current_scene == "start screen":
            self.show_start_screen()
        if self.current_scene == "room 022":
            self.current_room = self.room2
            self.current_room.setup()
            self.current_room.on_draw()
    
if __name__ == "__main__":
    game = roomManager()
    game.setup()
    arcade.run()