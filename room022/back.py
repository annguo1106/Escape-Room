import arcade
import sceneUtil
import os
from itemList import item_list, code_list

class Back(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["DoorRight", "DoorLeft", "None", "None"]
        self.scene_name = "back"
        self.books = []
        
    def setBackground(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_path, '..', "img/background/back.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
        
    def setup(self):
        super().setup()
        
        current_path = os.path.dirname(os.path.abspath(__file__))

        # code
        for book in code_list["bookCode"]:
            # print("setting book code")
            path = os.path.join(current_path, '..', book["path"])
            sp = arcade.Sprite(path, 0.5)
            sp.set_position(book["x"], book["y"])
            self.code.add_sprite("book", sp)

    def on_draw(self):
        super().on_draw()
        
        # decoding
        if item_list["back"][0]["state"] == 0 or 1:
            self.code["book"].draw()
            
        arcade.finish_render()
        
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        
        # init
        current_path = os.path.dirname(os.path.abspath(__file__))
        bookShell = self.items["bookShell"]["sprite"]
        
        # click on shell
        if(bookShell.collides_with_point((x, y))):
            # before decoding
            if item_list["back"][0]["state"] == 0:
                self.pre_action = "click bookShell"
                item_list["back"][0]["state"] = 1
                
            # decoding
            elif item_list["back"][0]["state"] == 1:
                
                pass
            
            # decoded
            elif item_list["back"][0]["state"] == 2:
                path = os.path.join(current_path, '..', "img/items/back/bookShellFin.png")
                bookShell.texture = arcade.load_texture(path)
                bookShell.scale = 0.5
                bookShell.position = (565, 350)
                self.pre_action = "click bookShell"