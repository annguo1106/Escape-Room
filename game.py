import arcade
from room114 import Classroom, is_exist
from room022.room022.mainTheme import MainTheme
from room022.room022.back import Back
from room022.room022.front import Front
from room022.room022.doorLeft import DoorLeft
from room022.room022.doorRight import DoorRight

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "room 114"

class Root(arcade.Window):
    def __init__(self):
        # set up window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # go to the starting view: classroom
        current_view = StartScreen()
        self.show_view(current_view)

    def setup(self):
        pass
	
    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_view.room == "022":
            # do control
            # left and right control position done
            CONTROL_COR = [[140, 10], [940, 10], [540, 605], [540, 10]]
            next = "-1"
            # print("check -> room022-on_mouse_press", "x", x, "y", y)
            for i in range(4):
                if(self.current_view.direction[i] != "None" and
                    x >= CONTROL_COR[i][0] and x <= CONTROL_COR[i][0] + 40 and
                    y >= CONTROL_COR[i][1] and y <= CONTROL_COR[i][1] + 40):
                    next = self.current_view.direction[i]
                    break

            if next != "-1":
                if next == "MainTheme":
                    next_view = MainTheme()
                elif next == "DoorLeft":
                    next_view = DoorLeft()
                elif next == "DoorRight":
                    next_view = DoorRight()
                elif next == "Back":
                    next_view = Back()
                elif next == "Front":
                    next_view = Front()
                self.show_view(next_view)
            
            # whether exist 022
            if self.current_view.scene_name == "doorRight" and self.current_view.exist:
                next_view = EndScreen()
                self.show_view(next_view)

class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.room = "114"

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

class EndScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.room = "End"

    def setup(self):
        pass

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("congratulations!", 250, 325, arcade.color.BLACK, 50)
        arcade.finish_render()


if __name__ == "__main__":
    # main114()
    window = Root()
    window.setup()
    arcade.run()