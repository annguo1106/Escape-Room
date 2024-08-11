import arcade
import arcade.gui
import sceneUtil
import os
from itemList import item_list, backpack_list
from inputUtil import FInputBox

class DoorLeft(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["Back", "MainTheme", "None", "None"]
        self.scene_name = "doorLeft"
        self.code = arcade.Scene()
        self.input_box = None
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/doorLeft.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)

    def setup(self):
        super().setup()
        self.input_box = FInputBox(325, 5, "MGANS")
    
    def on_draw(self):
        super().on_draw()
        
        if item_list["doorLeft"][0]["state"] == 1:
            self.input_box.on_draw()
            
        arcade.finish_render()
    
    def on_key_press(self, key, modifiers: int):
        super().on_key_press(key, modifiers)
        
        if item_list["doorLeft"][0]["state"] == 1:
            self.input_box.on_key_press(key, modifiers)
            if self.input_box.result:
                item_list["doorLeft"][0]["state"] = 2
                # print("right answer")
                box = self.items["box"]["sprite"]
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathRes"])
                box.texture = arcade.load_texture(path)
                box.scale = 0.2
                box.position = (550, 325)
                # box.position = (item_list["doorLeft"][0]["x"], item_list["doorLeft"][0]["y"])
                self.pre_action = None
    
                
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        
        # init
        box = self.items["box"]["sprite"]
        
        # click on box
        if(box.collides_with_point((x, y))):
            
            # before decoding
            if item_list["doorLeft"][0]["state"] == 0:    
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathShow"])
                box.texture = arcade.load_texture(path)
                box.scale = 0.4
                box.position = (550, 325)
                self.pre_action = "click box"
                item_list["doorLeft"][0]["state"] = 1

            
            # decoding
            # elif item_list["doorLeft"][0]["state"] == 1:
            #     if self.input_box.result:
            #         item_list["doorLeft"][0]["state"] = 2
            #         print("right answer")
            #     else:
            #         print("worng password, try again")
            elif item_list["doorLeft"][0]["state"] == 2: # click on hammer -> in to backpack
                # item_list["doorLeft"][0]["display"] = False
                item_list["doorLeft"][0]["state"] = 3
                # path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathSmall"])
                # box.texture = arcade.load_texture(path)
                # box.scale = item_list["doorLeft"][0]["scale"]
                # box.position = (item_list["doorLeft"][0]["x"], item_list["doorLeft"][0]["y"])
                box.remove_from_sprite_lists()
                backpack_list[1]["display"] = True
                self.set_backpack()
                self.pre_action = None
                
            
            elif item_list["doorLeft"][0]["state"] == 3:
                # print("load result")
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathShow"])
                box.texture = arcade.load_texture(path)
                box.scale = 0.4
                box.position = (550, 325)
                self.pre_action = "click box"
                
                
        # exist box
        elif(self.pre_action == "click box" and (x <= 193 or x >= 907 or y <= 191 or y >= 459)):
            path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathSmall"])
            box.texture = arcade.load_texture(path)
            box.scale = item_list["doorLeft"][0]["scale"]
            box.position = (item_list["doorLeft"][0]["x"], item_list["doorLeft"][0]["y"])
            self.pre_action = None
            if item_list["doorLeft"][0]["state"] != 2:
                item_list["doorLeft"][0]["state"] = 0
            
            
        # at the click event end
        for item in self.backpack:    
            sp = item["sprite"]
            if(self.pre_action == ("click " + item["name"]) and not sp.collides_with_point((x, y))):
                sp.scale = item["scale"]
                self.pre_action = None
 
        
