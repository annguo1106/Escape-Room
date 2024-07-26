import arcade
import utils

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "room 114"

CONTROL_SCALING = 0.8
CONTROL_ALPHA = 140     # the transparency of the img, range(0, 255)

CONTROL_COR = [[-100, -100], [540, 10], [140, 10], [940, 10]]

backpack = {
    'rag': False,
    'phone': False,
    'charger': False,
    'ladder': False,
    'eraser': False,
    'red pen': False
}

class MyGame(arcade.Window):
    def __init__(self):
        # set up window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # go to the starting view: classroom
        current_view = Classroom()
        self.show_view(current_view)

    def setup(self):
        pass


class Classroom(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [True, False, True, True]  # 紀錄前後左右是否可以到達別的場景

    def setup(self):
        arrow_left = arcade.Sprite("img/control/arrow_left.png", CONTROL_SCALING)
        arrow_left.center_x = 160
        arrow_left.center_y = 30
        arrow_left.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_left)

        arrow_right = arcade.Sprite("img/control/arrow_right.png", CONTROL_SCALING)
        arrow_right.center_x = 960
        arrow_right.center_y = 30
        arrow_right.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_right)

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("classroom", 500, 325)
        # background
        utils.draw_background()
        # control
        self.scene.draw()
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go left
            if(is_ctl == 2):
                nxt_view = Table()
                self.window.show_view(nxt_view)
            # go right
            elif(is_ctl == 3):
                nxt_view = Door()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Blackboard(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, True, True]  # 紀錄前後左右是否可以到達別的場景
        if(backpack['ladder']):
            self.direction[0] = True

    def setup(self):
        arrow_left = arcade.Sprite("img/control/arrow_left.png", CONTROL_SCALING)
        arrow_left.center_x = 160
        arrow_left.center_y = 30
        arrow_left.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_left)

        arrow_right = arcade.Sprite("img/control/arrow_right.png", CONTROL_SCALING)
        arrow_right.center_x = 960
        arrow_right.center_y = 30
        arrow_right.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_right)

        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)

    def on_show(self):
        self.setup()
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("blackboard", 500, 325)
        # background
        utils.draw_background()
        # control
        self.scene.draw()
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go left
            if(is_ctl == 2):
                nxt_view = Stage()
                self.window.show_view(nxt_view)
            # go right
            elif(is_ctl == 3):
                nxt_view = Corner()
                self.window.show_view(nxt_view)
            # go back
            elif(is_ctl == 1):
                nxt_view = Classroom()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Door(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景

    def setup(self):
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("door", 500, 325)
        # background
        utils.draw_background()
        # control
        self.scene.draw()
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                nxt_view = Classroom()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Stage(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景

    def setup(self):
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("stage", 500, 325)
        # background
        utils.draw_background()
        # control
        self.scene.draw()
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                nxt_view = Blackboard()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Corner(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景

    def setup(self):
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("corner", 500, 325)
        # background
        utils.draw_background()
        # control
        self.scene.draw()
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                nxt_view = Blackboard()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)

class Table(arcade.View):
    def __init__(self):
        super().__init__()
        self.scene = arcade.Scene()
        self.direction = [False, True, False, False]  # 紀錄前後左右是否可以到達別的場景

    def setup(self):
        arrow_down = arcade.Sprite("img/control/arrow_down.png", CONTROL_SCALING)
        arrow_down.center_x = 560
        arrow_down.center_y = 30
        arrow_down.alpha = CONTROL_ALPHA
        self.scene.add_sprite("Control", arrow_down)

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("table", 500, 325)
        # background
        utils.draw_background()
        # control
        self.scene.draw()
        arcade.finish_render()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # press control?
        is_ctl = utils.press_control(x, y, self.direction)
        if(is_ctl != -1):
            # go back
            if(is_ctl == 1):
                nxt_view = Classroom()
                self.window.show_view(nxt_view)
            # default, should not happend
            else:
                print(f"in function on_mouse_press, x = {x}, y = {y}, dir = {is_ctl}")

    def on_key_press(self, key: int, modifiers: int):
        if(key == arcade.key.A):
            nxt_view = Classroom()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.B):
            nxt_view = Blackboard()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.C):
            nxt_view = Door()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.D):
            nxt_view = Stage()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.E):
            nxt_view = Corner()
            self.window.show_view(nxt_view)
        elif(key == arcade.key.F):
            nxt_view = Table()
            self.window.show_view(nxt_view)



def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()