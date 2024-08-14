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
        self.input_safe = None
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/doorLeft.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)

    def setup(self):
        super().setup()
        self.input_box = FInputBox(277, 5, "MASGN")
        self.input_safe = FInputBox(345, 6, "NYCUCS")
    
    def on_draw(self):
        super().on_draw()
        
        if item_list["doorLeft"][0]["state"] == 1:
            self.input_box.on_draw()
        
        if item_list["doorLeft"][1]["state"] == 2:
            self.input_safe.on_draw()
            
        arcade.finish_render()
    
    def on_key_press(self, key, modifiers: int):
        super().on_key_press(key, modifiers)
        
        if item_list["doorLeft"][0]["state"] == 1:
            self.input_box.on_key_press(key, modifiers)
            if self.input_box.result:
                item_list["doorLeft"][0]["state"] = 2
                box = self.items["box"]["sprite"]
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathRes"])
                self.load_sp(box, 1, 550, 325, path)
                self.pre_action = None
        elif item_list["doorLeft"][1]["state"] == 2:
            self.input_safe.on_key_press(key, modifiers)
            if self.input_safe.result:
                item_list["doorLeft"][1]["state"] = 3
                safe = self.items["poster"]["sprite"]
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][1]["pathIt"])
                self.load_sp(safe, 1.1, 550, 325, path)
                self.pre_action = "click poster"
    
                
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        print("pre_action:", self.pre_action)
        super().on_mouse_press(x, y, button, modifires)
        
        # init
        box = self.items["box"]["sprite"]
        poster = self.items["poster"]["sprite"]
        
        # handle exist first
        # exist box
        if(self.pre_action == "click box" and (x <= 193 or x >= 907 or y <= 191 or y >= 459)):
            path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathSmall"])
            self.load_sp(box, item_list["doorLeft"][0]["scale"], item_list["doorLeft"][0]["x"], item_list["doorLeft"][0]["y"], path)
            self.pre_action = None
            if item_list["doorLeft"][0]["state"] == 1:
                item_list["doorLeft"][0]["state"] = 0
        
        # exist poster
        elif(self.pre_action == "click poster" and not poster.collides_with_point((x, y))):
            print("exist safe")
            path = os.path.join(self.current_path, '..', item_list["doorLeft"][1]["pathSmall"])
            self.load_sp(poster, 0.5, item_list["doorLeft"][1]["x"], item_list["doorLeft"][1]["y"], path)
            self.pre_action = None
            # decoding not finished
            if item_list["doorLeft"][1]["state"] == 2:
                item_list["doorLeft"][1]["state"] = 1
        
        # click on box
        elif(box.collides_with_point((x, y))):
            # before decoding
            if item_list["doorLeft"][0]["state"] == 0:
                self.load_sp(box, item_list["doorLeft"][0]["scale"] * 2.4, 550, 325)
                self.pre_action = "click box"
                item_list["doorLeft"][0]["state"] = 1
            
            # click on hammer -> in to backpack
            elif item_list["doorLeft"][0]["state"] == 2:
                item_list["doorLeft"][0]["state"] = 3
                box.remove_from_sprite_lists()
                backpack_list[1]["display"] = True
                self.set_backpack()
                self.pre_action = None
            
            # show solved box
            elif item_list["doorLeft"][0]["state"] == 3:
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][0]["pathEnd"])
                self.load_sp(box, item_list["doorLeft"][0]["scale"] * 2.4, 550, 325, path)
                self.pre_action = "click box" 
                
        # click poster
        elif(poster.collides_with_point((x, y))):
            # remove poster
            if item_list["doorLeft"][1]["state"] == 0:
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][1]["pathRes"])
                self.load_sp(poster, 0.5, item_list["doorLeft"][1]["x"], item_list["doorLeft"][1]["y"], path)
                item_list["doorLeft"][1]["pathSmall"] = item_list["doorLeft"][1]["pathRes"]
                item_list["doorLeft"][1]["state"] = 1
                self.pre_action = "click poster"
            # safe decoding
            elif item_list["doorLeft"][1]["state"] == 1:
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][1]["pathRes"])
                self.load_sp(poster, 1.1, 550, 325, path)
                item_list["doorLeft"][1]["state"] = 2
                self.pre_action = "click poster"
            # key reveal
            elif item_list["doorLeft"][1]["state"] == 3:
                item_list["doorLeft"][1]["state"] = 4
                poster.remove_from_sprite_lists()
                backpack_list[4]["display"] = True # receive key
                self.set_backpack()
                self.pre_action = None

            # key took    
            elif item_list["doorLeft"][1]["state"] == 4:
                path = os.path.join(self.current_path, '..', item_list["doorLeft"][1]["pathEnd"])
                self.load_sp(poster, 1.1, 550, 325, path)
                self.pre_action = "click poster"
        
            
        # at the click event end
        if self.hand_item:
            # print("hand item:", self.hand_item["name"])
            if(self.hand_item["sprite"].scale != self.hand_item["scale"] and not self.hand_item["sprite"].collides_with_point((x, y))):
                self.hand_item["sprite"].scale = self.hand_item["scale"]
                if(self.pre_action == ("click " + self.hand_item["name"])):
                    self.hand_item = None
                    self.pre_action = None
