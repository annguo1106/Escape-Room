import arcade
import sceneUtil
import os
from itemList import item_list, backpack_list

class DoorRight(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["MainTheme", "Back", "None", "None"]
        self.scene_name = "doorRight"
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/doorRight.png")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
        
    def on_draw(self):
        super().on_draw()
        arcade.finish_render()
    
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        
        # init
        professorYen = self.items["professorYen"]["sprite"]
        vase = self.items["vase"]["sprite"]
        # click on professorYen
        # print("in doorRight -> check professor sprite", professorYen["name"])
        if(professorYen.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["doorRight"][1]["pathShow"])
            professorYen.texture = arcade.load_texture(path)
            professorYen.scale = 0.5
            professorYen.position = (550, 325)
            self.pre_action = "click professorYen"
        # exist professor Yen
        elif(self.pre_action == "click professorYen" and not professorYen.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["doorRight"][1]["pathSmall"])
            professorYen.texture = arcade.load_texture(path)
            professorYen.scale = item_list["doorRight"][1]["scale"]
            professorYen.position = (item_list["doorRight"][1]["x"], item_list["doorRight"][1]["y"])
            self.pre_action = None
        # click on vase
        elif(vase.collides_with_point((x, y))):
            if item_list["doorRight"][0]["state"] == 0:
                if self.pre_action == "click hammer":
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathRes"])
                    vase.texture = arcade.load_texture(path)
                    vase.scale = item_list["doorRight"][0]["scale"] * 1.2
                    vase.position = (550, 325)
                    item_list["doorRight"][0]["state"] = 1
                    backpack_list[1]["display"] = False # hammer used
                    self.scene.get_sprite_list("Backpack").clear()
                    self.hand_item = None
                    print("self hand", self.hand_item)
                    self.set_backpack()
                    print("hammer used")
                    self.pre_action = None
                else:
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathShow"])
                    vase.texture = arcade.load_texture(path)
                    vase.scale = item_list["doorRight"][0]["scale"] * 1.2
                    vase.position = (550, 325)
                    self.pre_action = "click vase"
                    
            elif item_list["doorRight"][0]["state"] == 1:
                item_list["doorRight"][0]["state"] = 2
                vase.remove_from_sprite_lists()
                backpack_list[0]["display"] = True # receive key
                self.set_backpack()
                self.pre_action = None
                
            elif item_list["doorRight"][0]["state"] == 2:
                path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathEnd"])
                vase.texture = arcade.load_texture(path)
                vase.scale = item_list["doorRight"][0]["scale"] * 1.2
                vase.position = (550, 325)
                item_list["doorRight"][0]["state"] = 1
                self.pre_action = "click vase"
                print("this vase is solved")
        
        # exist vase
        elif(self.pre_action == "click vase" and not vase.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathSmall"])
            vase.texture = arcade.load_texture(path)
            vase.scale = item_list["doorRight"][0]["scale"]
            vase.position = (item_list["doorRight"][0]["x"], item_list["doorRight"][0]["y"])
            self.pre_action = None
        
        # at the click event end
        if self.hand_item:
            print("hand item:", self.hand_item["name"])
            if(self.hand_item["sprite"].scale != self.hand_item["scale"] and not self.hand_item["sprite"].collides_with_point((x, y))):
                self.hand_item["sprite"].scale = self.hand_item["scale"]
                if(self.pre_action == ("click " + self.hand_item["name"])):
                    self.pre_action = None
