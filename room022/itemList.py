# states: 0: not display, 1: display, 2: used
item_list = {
    "mainTheme": [
    ],
    "doorRight": [
        {
        "name": "vase",
        "sprite": None,
        "state": 0, # 0: small, 1: break, 2: solved
        "display": True,
        "pathSmall": "img/items/doorRight/vaseSmall.png",
        "pathShow": "img/items/doorRight/vaseShow.png",
        "pathRes": "img/items/doorRight/vaseShow.png",
        "pathEnd": "img/items/doorRight/vaseShow.png",
        "scale": 0.2,
        "place": "doorRight",
        "x": 185,
        "y": 170
        },
        {
        "name": "professorYen",
        "sprite": None,
        "state": 1,
        "display": True,
        "pathSmall": "img/items/doorRight/professorYenSmall.png",
        "pathShow": "img/items/doorRight/professorYenShow.jpg",
        "scale": 0.2,
        "place": "doorRight",
        "x": 286,
        "y": 352}
    ],
    "doorLeft": [
        {
        "name": "box",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding 3: get hammer
        "display": True,
        "pathSmall": "img/items/doorLeft/boxSmall.png",
        "pathShow": "img/items/doorLeft/boxShow.jpg",
        "pathRes": "img/items/doorLeft/hammer.png",
        "pathEnd": "img/items/doorLeft/boxShow.png",
        "scale": 0.1,
        "place": "doorLeft",
        "x": 250,
        "y": 200
        }
    ],
    "back": [
        {
        "name": "bookShell",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding
        "display": True,
        "pathSmall": "img/items/back/bookShellSmall.png",
        "pathShow": "img/items/back/bookShellShow.png",
        "scale": 1.02,
        "place": "doorLeft",
        "x": 565,
        "y": 350
        }
    ],
    "front": [
    ]
}

backpack_list = [
    {
        "name": "key",  # need to be changed into flashlight
        "sprite": None,
        "state": 0,
        "scale": 0.3,
        "display": False,
        "path": "img/items/key.png"
    },
    {
        "name": "hammer",
        "sprite": None,
        "state": 0,  # 0: not used, 1: used CURRENTLY NO USE
        "scale": 0.18,
        "display": False,
        "path": "img/items/doorLeft/hammer.png"
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

code_list = {
    "bookCode": [
        {
            "name": "book1",
            "path": "img/items/back/book1.png",
            "sp": None,
            "x": 250,
            "y": 250
        },
        {
            "name": "book2",
            "path": "img/items/back/book2.png",
            "sp": None,
            "x": 250,
            "y": 250
        },
        {
            "name": "book3",
            "path": "img/items/back/book3.png",
            "sp": None,
            "x": 250,
            "y": 250
        },
        {
            "name": "book4",
            "path": "img/items/back/book4.png",
            "sp": None,
            "x": 250,
            "y": 250
        },
        {
            "name": "book5",
            "path": "img/items/back/book5.png",
            "sp": None,
            "x": 250,
            "y": 250
        },
    ],
}
