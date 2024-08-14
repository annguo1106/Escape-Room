import arcade
import sceneUtil
import os
from itemList import item_list, backpack_list, code_list


class DoorRight(sceneUtil.Scenes):
    def __init__(self):
        super().__init__()
        self.direction = ["MainTheme", "Back", "None", "None"]
        self.scene_name = "doorRight"
        self.door_code = []
        self.door_ans = [6, 2, 3, 4, 0]
        self.input_ans = [0] * 5
        
    def setBackground(self):
        path = os.path.join(self.current_path, '..', "img/background/doorRight.jpg")
        background = arcade.Sprite(path, 1.02)
        background.center_x = 561
        background.center_y = 325
        self.scene.add_sprite("Background", background)
   
    def set_code(self):
        self.door_code.clear()
        self.input_ans = [0] * 5
        x = 428
        y = 295
        path = os.path.join(self.current_path, '..', code_list["doorCode"][0]["path"])
        for _ in range(5):
            sp = arcade.Sprite(path, 0.45)
            sp.set_position(x, y)
            x += 60
            self.code.add_sprite("doorCode", sp)
            self.door_code.append({
                "sprite": sp,
                "num": 0
            })
        
    def on_draw(self):
        super().on_draw()
        if item_list["doorRight"][1]["state"] == 1:
            self.code.draw()
        arcade.finish_render()
    
    def on_mouse_press(self, x: int, y: int, button: int, modifires: int):
        super().on_mouse_press(x, y, button, modifires)
        
        # init
        professorYen = self.items["professorYen"]["sprite"]
        vase = self.items["vase"]["sprite"]
        lock = self.items["lock"]["sprite"]
        
        # handle exist first
        # exist vase
        if(self.pre_action == "click vase" and not vase.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathSmall"])
            self.load_sp(vase, item_list["doorRight"][0]["scale"], item_list["doorRight"][0]["x"], item_list["doorRight"][0]["y"], path)
            self.pre_action = None
        
        # exist professor Yen
        elif(self.pre_action == "click professorYen" and not professorYen.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["doorRight"][1]["pathSmall"])
            self.load_sp(professorYen, item_list["doorRight"][1]["scale"], item_list["doorRight"][1]["x"], item_list["doorRight"][1]["y"], path)
            self.pre_action = None
        
        # exist lock
        elif(self.pre_action == "click lock" and not lock.collides_with_point((x, y))):
            path = os.path.join(self.current_path, '..', item_list["doorRight"][2]["pathSmall"])
            self.load_sp(lock, item_list["doorRight"][2]["scale"], item_list["doorRight"][2]["x"], item_list["doorRight"][2]["y"], path)
            for c in self.door_code:
                c["sprite"].remove_from_sprite_lists()
            if item_list["doorRight"][1]["state"] == 1:
                item_list["doorRight"][1]["state"] = 0
            self.pre_action = None
                
        # click on professorYen
        elif(professorYen.collides_with_point((x, y))):
            if item_list["doorRight"][1]["state"] == 0:
                # use flashlight
                if self.pre_action == "click flashlight":
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][1]["pathEnd"])
                    item_list["doorRight"][1]["state"] = 1
                    backpack_list[0]["display"] = False # flashlight used
                    self.hand_item = None
                    self.set_backpack()
                # didn't use flashlight
                else:
                    path = None
            elif item_list["doorRight"][1]["state"] == 1:
                path = os.path.join(self.current_path, '..', item_list["doorRight"][1]["pathEnd"])
            self.load_sp(professorYen, 1, 550, 325, path)
            self.pre_action = "click professorYen"
            
            
        # click on vase
        elif(vase.collides_with_point((x, y))):
            # vase
            if item_list["doorRight"][0]["state"] == 0:
                if self.pre_action == "click hammer":
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathRes"])
                    item_list["doorRight"][0]["state"] = 1 # vase broke
                    backpack_list[1]["display"] = False # hammer used
                    # reset backpack
                    self.hand_item = None
                    self.set_backpack()
                    self.pre_action = None
                else:
                    path = None
                    self.pre_action = "click vase"
                self.load_sp(vase, item_list["doorRight"][0]["scale"] * 1.5, 550, 325, path)
            # reveal flashlight       
            elif item_list["doorRight"][0]["state"] == 1:
                item_list["doorRight"][0]["state"] = 2
                vase.remove_from_sprite_lists()
                backpack_list[0]["display"] = True # receive flashlight
                self.set_backpack()
                self.pre_action = None
            # vase end    
            elif item_list["doorRight"][0]["state"] == 2:
                path = os.path.join(self.current_path, '..', item_list["doorRight"][0]["pathEnd"])
                self.load_sp(vase, item_list["doorRight"][0]["scale"] * 1.5, 550, 325, path)
                self.pre_action = "click vase"
        
        
        
        # click lock
        elif(lock.collides_with_point((x, y))):
            if item_list["doorRight"][1]["state"] == 0:
                item_list["doorRight"][1]["state"] = 1
                self.load_sp(lock, item_list["doorRight"][2]["scale"] * 3, 550, 325)
                self.set_code()
            # decoding
            elif item_list["doorRight"][1]["state"] == 1:
                i = 0
                for c in self.door_code:
                    if(c["sprite"].collides_with_point((x, y))):
                        c["num"] = (c["num"] + 1) % 10
                        path = os.path.join(self.current_path, '..', code_list["doorCode"][c["num"]]["path"])
                        c["sprite"].texture = arcade.load_texture(path)
                        self.input_ans[i] = c["num"]
                    i += 1
                # ans correct
                if self.input_ans == self.door_ans:
                    item_list["doorRight"][1]["state"] = 2
                    print("correct!")
                    # for c in self.door_code:
                    #     c["sprite"].remove_from_sprite_lists()
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][2]["pathRes"])
                    self.load_sp(lock, item_list["doorRight"][2]["scale"] * 1.7, 550, 325, path)
            # decoded
            elif item_list["doorRight"][1]["state"] == 2:
                # if use key
                if self.pre_action == "click key":
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][2]["pathEnd"])
                    backpack_list[4]["display"] = False # key used
                    # reset backpack
                    self.hand_item = None
                    self.set_backpack()
                else:
                    path = os.path.join(self.current_path, '..', item_list["doorRight"][2]["pathRes"])
                self.load_sp(lock, item_list["doorRight"][2]["scale"] * 1.5, 550, 325, path)    
            # if all end
            elif item_list["doorRight"][1]["state"] == 3:
                path = os.path.join(self.current_path, '..', item_list["doorRight"][2]["pathEnd"])
                self.load_sp(lock, item_list["doorRight"][2]["scale"] * 1.5, 550, 325, path)
                print("you already exist this door!")
            self.pre_action = "click lock"
            
        # at the click event end
        if self.hand_item:
            # print("hand item:", self.hand_item["name"])
            if(self.hand_item["sprite"].scale != self.hand_item["scale"] and not self.hand_item["sprite"].collides_with_point((x, y))):
                self.hand_item["sprite"].scale = self.hand_item["scale"]
                if(self.pre_action == ("click " + self.hand_item["name"])):
                    self.hand_item = None
                    self.pre_action = None
