# states: 0: not display, 1: display, 2: used
item_list = {
    "mainTheme": [
    ],
    "doorRight": [
        {
        "name": "vase",
        "sprite": None,
        "state": 1,
        "pathSmall": "img/items/vaseSmall.png",
        "pathShow": "img/items/vaseShow.png",
        "scale": 0.05,
        "place": "doorRight",
        "x": 185,
        "y": 170
        },
        {
        "name": "professorYen",
        "sprite": None,
        "state": 1,
        "pathSmall": "img/items/professorYenSmall.png",
        "pathShow": "img/items/professorYenShow.jpg",
        "scale": 0.2,
        "place": "doorRight",
        "x": 286,
        "y": 352}
    ],
    "doorLeft": [
        {
        "name": "box",
        "sprite": None,
        "state": 1,  # 1: small, 2: decoding, 3: finished decoding
        "pathSmall": "img/items/boxSmall.png",
        "pathShow": "img/items/boxShow.png",
        "scale": 0.1,
        "place": "doorLeft",
        "x": 250,
        "y": 200
        }
    ],
    "back": [
    ],
    "front": [
    ]
}

backpack_list = [
    {
        "name": "key",
        "sprite": None,
        "state": 0,
        "display": None,
        "path": "img/items/key.png"
    }
]

control_list = [
    {
        "dir": "left",
        "path": "img/control/left.png",
        "x": 160,
        "y": 30
    },
    {
        "dir": "right",
        "path": "img/control/right.png",
        "x": 960,
        "y": 30
    },
    {
        "dir": "up",
        "path": "img/control/up.png",
        "x": 560,
        "y": 625
    },
    {
        "dir": "down",
        "path": "img/control/down.png",
        "x": 560,
        "y": 30
    }    
]
