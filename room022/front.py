import arcade
import sceneUtil
import os
from inputUtil import FInputBox
from itemList import item_list, backpack_list

class Front(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["None", "None", "None", "MainTheme"]
        self.scene_name = "front"
        self.input_computer = None
        self.input_drawer = None
        self.input_notebook = None
            
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/front.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
    
    def setup(self):
        super().setup()
        self.input_computer = FInputBox(375, 6, "STRQND")
        self.input_drawer = FInputBox(239, 4, "2984")
        self.input_notebook = FInputBox(315, 5, "ASBZY")
    
    def on_draw(self):
        super().on_draw()
        # decoding computer
        if item_list["front"][0]["state"] == 1:
            self.input_computer.on_draw()
        elif item_list["front"][3]["state"] == 1:
            self.input_drawer.on_draw()
        elif item_list["front"][1]["state"] == 1:
            self.input_notebook.on_draw()
                    
        arcade.finish_render()
     
    def on_key_press(self, key, modifiers: int):
        super().on_key_press(key, modifiers)
        # decoding computer
        if item_list["front"][0]["state"] == 1:
            self.input_computer.on_key_press(key, modifiers)
            if self.input_computer.result:
                item_list["front"][0]["state"] = 2
                item_list["front"][2]["state"] = 1 # show on screen
                computer = self.items["computer"]["sprite"]
                path = os.path.join(self.current_path, '..', item_list["front"][0]["pathEnd"])
                self.load_sp(computer, item_list["front"][0]["scale"] * 2.3, 540, 325, path)
                self.pre_action = "click computer"
        # decoding drawer
        elif item_list["front"][3]["state"] == 1:
            self.input_drawer.on_key_press(key, modifiers)
            if self.input_drawer.result:
                item_list["front"][3]["state"] = 2
                drawer = self.items["drawer"]["sprite"]
                path = os.path.join(self.current_path, '..', item_list["front"][3]["pathEnd"])
                self.load_sp(drawer, 1.2, 550, 325, path)
                self.pre_action = "click front drawer"
        # decoding notebook
        elif item_list["front"][1]["state"] == 1:
            self.input_notebook.on_key_press(key, modifiers)
            if self.input_notebook.result:
                item_list["front"][1]["state"] = 2
                notebook = self.items["notebook"]["sprite"]
                path = os.path.join(self.current_path, '..', item_list["front"][1]["pathRes"])
                self.load_sp(notebook, item_list["front"][1]["scale"] * 1.5, 550, 325, path)
                self.pre_action = "click notebook"
                
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        
        # click notebook
        notebook = self.items["notebook"]["sprite"]
        if(notebook.collides_with_point((x, y))):
            if item_list["front"][1]["state"] == 0:
                item_list["front"][1]["state"] = 1
                self.load_sp(notebook, item_list["front"][1]["scale"] * 2.8, 555, 325)
                self.pre_action = "click notebook"
            # notebook decoded
            elif item_list["front"][1]["state"] == 2:
                if self.pre_action == "click lighter":
                    item_list["front"][1]["state"] = 3
                    path = os.path.join(self.current_path, '..', item_list["front"][1]["pathEnd"])
                    backpack_list[3]["display"] = False # lighter used
                    self.scene.get_sprite_list("Backpack").clear()
                    self.hand_item = None
                    self.set_backpack()
                    self.on_draw()
                else:
                    path = os.path.join(self.current_path, '..', item_list["front"][1]["pathRes"])
                self.load_sp(notebook, item_list["front"][1]["scale"] * 1.5, 550, 325, path)
                self.pre_action = "click notebook"
            # code revealed
            elif item_list["front"][1]["state"] == 3:
                path = os.path.join(self.current_path, '..', item_list["front"][1]["pathEnd"])
                notebook.texture = arcade.load_texture(path)
                notebook.hit_box = notebook.texture.hit_box_points
                notebook.scale = 0.4
                notebook.position = (550, 325)
                self.pre_action = "click notebook"
        # exist notebook
        elif(self.pre_action == "click notebook" and not notebook.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["front"][1]["pathSmall"])
            self.load_sp(notebook, item_list["front"][1]["scale"], item_list["front"][1]["x"], item_list["front"][1]["y"], path)
            self.pre_action = "click notebook"
            if item_list["front"][1]["state"] == 1:
                item_list["fornt"][1]["state"] = 0
                
        # click computer
        computer = self.items["computer"]["sprite"]
        if(computer.collides_with_point((x, y))):
            # small -> show
            if(item_list["front"][0]["state"] == 0):
                item_list["front"][0]["state"] = 1
                path = os.path.join(self.current_path, '..', item_list["front"][0]["pathShow"])
            # decoded
            elif(item_list["front"][0]["state"] == 2):
                path = os.path.join(self.current_path, '..', item_list["front"][0]["pathEnd"])
            else:
                path = None
            self.load_sp(computer, item_list["front"][0]["scale"] * 2.3, 540, 325, path)
            self.pre_action = "click computer"
                
        # exist computer
        elif(self.pre_action == "click computer" and not computer.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["front"][0]["pathSmall"])
            self.load_sp(computer, item_list["front"][0]["scale"], item_list["front"][0]["x"], item_list["front"][0]["y"], path)
            self.pre_action = "click computer"
            if item_list["front"][0]["state"] != 2:
                item_list["front"][0]["state"] = 0

        # click screen
        screen = self.items["screen"]["sprite"]
        if(screen.collides_with_point((x, y))):
            # when computer is decoded
            if item_list["front"][2]["state"] == 1:
                path = os.path.join(self.current_path, '..', item_list["front"][2]["pathEnd"])
            else:
                path = os.path.join(self.current_path, '..', item_list["front"][2]["pathShow"])
            self.load_sp(screen, 1, 560, 375, path)
            self.pre_action = "click screen"
            
        # exist screen
        elif(self.pre_action == "click screen" and not screen.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["front"][2]["pathSmall"])
            self.load_sp(screen, item_list["front"][2]["scale"], item_list["front"][2]["x"], item_list["front"][2]["y"], path)
            self.pre_action = None
        
        # click drawer
        drawer = self.items["drawer"]["sprite"]
        if (drawer.collides_with_point((x, y))):
            if item_list["front"][3]["state"] == 0:
                path = os.path.join(self.current_path, '..', item_list["front"][3]["pathShow"])
                item_list["front"][3]["state"] = 1
                self.load_sp(drawer, item_list["front"][3]["scale"] * 1.5, 550, 325, path)
            elif item_list["front"][3]["state"] == 2:
                path = os.path.join(self.current_path, '..', item_list["front"][3]["pathEnd"])
                self.load_sp(drawer, 1.2, 550, 325, path)
            self.pre_action = "click front drawer"
        
        # exist drawer
        elif(self.pre_action == "click front drawer" and not drawer.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["front"][3]["pathSmall"])
            self.load_sp(drawer, item_list["front"][3]["scale"], item_list["front"][3]["x"], item_list["front"][3]["y"], path)
            self.pre_action = None
            if item_list["front"][3]["state"] != 2:
                item_list["front"][3]["state"] = 0
        
        # at click event end
        for item in self.backpack:
            sp = item["sprite"]
            if(self.pre_action == ("click " + item["name"]) and not sp.collides_with_point((x, y))):
                sp.scale = item["scale"]
                self.pre_action = None
 