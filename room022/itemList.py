# states: 0: not display, 1: display, 2: used
item_list = {
    "mainTheme": [
        {
        "name": "drawer",
        "sprite": None,
        "state": 0, # 0: small, 1: solved
        "display": False,
        "pathShow": "img/items/mainTheme/drawerShow.png",
        "pathEnd": "img/items/mainTheme/drawerEnd.png",
        "scale": 0.8,
        "place": "mainTheme",
        "x": 550,
        "y": 350
        },
        {
        "name": "rag",
        "sprite": None,
        "state": 0,
        "display": True,
        "pathSmall": "img/items/mainTheme/ragSmall.png",
        # "pathShow": "img/items/mainTheme/ragShow.png",
        "scale": 0.09,
        "place": "mainTheme",
        "x": 664,
        "y": 256
        },
    ],
    "doorRight": [
        {
        "name": "vase",
        "sprite": None,
        "state": 0, # 0: small, 1: break, 2: solved
        "display": True,
        "pathSmall": "img/items/doorRight/vaseSmall.png",
        "pathShow": "img/items/doorRight/vaseShow.png",
        "pathRes": "img/items/doorRight/vaseRes.png",
        "pathEnd": "img/items/doorRight/vaseEnd.png",
        "scale": 0.5,
        "place": "doorRight",
        "x": 185,
        "y": 170
        },
        {
        "name": "professorYen",
        "sprite": None,
        "state": 0,  # 0: small, 1: solved
        "display": True,
        "pathSmall": "img/items/doorRight/professorYenSmall.png",
        "pathEnd": "img/items/doorRight/professorYenEnd.png",
        "scale": 0.8,
        "place": "doorRight",
        "x": 286,
        "y": 370
        },
        {
        "name": "lock",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: decoded, 3: key used
        "display": True,
        "pathSmall": "img/items/doorRight/lockSmall.png",
        "pathRes": "img/items/doorRight/lockRes.png",
        "pathEnd": "img/items/doorRight/lockEnd.png",
        "scale": 0.35,
        "place": "doorRight",
        "x": 660,
        "y": 124
        }
    ],
    "doorLeft": [
        {
        "name": "box",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding 3: get hammer
        "display": True,
        "pathSmall": "img/items/doorLeft/boxSmall.png",
        "pathShow": "img/items/doorLeft/boxShow.png",
        "pathRes": "img/items/doorLeft/hammer.png",
        "pathEnd": "img/items/doorLeft/boxEnd.png",
        "scale": 0.35,
        "place": "doorLeft",
        "x": 280,
        "y": 200
        },
        {
        "name": "poster",
        "sprite": None,
        "state": 0,  # 0: poster, 1: safe, 2: decoding, 3: rec key, 4: decoded
        "display": True,
        "pathSmall": "img/items/doorLeft/posterSmall.jpg", #
        "pathShow": "img/items/doorLeft/safeShow.png", # decoding
        "pathRes": "img/items/doorLeft/safeRes.png", # safe under poster
        "pathIt": "img/items/doorLeft/key.png", # key
        "pathEnd": "img/items/doorLeft/safeEnd.png", # end
        "scale": 0.5,
        "place": "doorLeft",
        "x": 260,
        "y": 450
        },
        
    ],
    "back": [
        {
        "name": "lighter",
        "sprite": None,
        "state": 0,  # 0: small, 1: took
        "display": True,
        "pathSmall": "img/items/back/lighter.png",
        "scale": 0.3,
        "place": "back",
        "x": 870,
        "y": 301
        },
        {
        "name": "shell",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding
        "display": True,
        "pathSmall": "img/items/back/shellSmall.png",
        "pathShow": "img/items/back/shellShow.png",
        "pathEnd": "img/items/back/shellEnd.png",
        "scale": 0.6,
        "place": "doorLeft",
        "x": 340,
        "y": 330
        }        
    ],
    "front": [
        {
        "name": "computer",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding
        "display": True,
        "pathSmall": "img/items/front/computerSmall.png",
        "pathShow": "img/items/front/computerShow.png",
        "pathEnd": "img/items/front/computerEnd.png",
        "scale": 0.4,
        "place": "front",
        "x": 820,
        "y": 224
        },
        {
        "name": "notebook",
        "sprite": None,
        "state": 0,  # 0: small, 1: decoding, 2: finished decoding, 3: code reveal
        "display": True,
        "pathSmall": "img/items/front/notebookSmall.png",
        "pathRes": "img/items/front/notebookRes.png",
        "pathEnd": "img/items/front/notebookEnd.png",
        "scale": 0.5,
        "place": "front",
        "x": 206,
        "y": 55
        },
        {
        "name": "screen",
        "sprite": None,
        "state": 0,  # 0: small, 1: show
        "display": True,
        "pathSmall": "img/items/front/screenSmall.png",
        "pathShow": "img/items/front/screenShow.png",
        "pathEnd": "img/items/front/screenEnd.png",
        "scale": 1,
        "place": "front",
        "x": 560,
        "y": 510
        },
        {
        "name": "drawer",
        "sprite": None,
        "state": 0,  # 0: small, 1: show, 2: end
        "display": True,
        "pathSmall": "img/items/front/drawerSmall.png",
        "pathShow": "img/items/front/drawerShow.png",
        "pathEnd": "img/items/front/drawerEnd.png",
        "scale": 0.5,
        "place": "front",
        "x": 280,
        "y": 44
        }
        
    ]
}

backpack_list = [
    {
        "name": "flashlight",  # need to be changed into flashlight
        "sprite": None,
        "state": 0,
        "scale": 0.5,
        "display": False,
        "path": "img/items/doorRight/flashlight.png"
    },
    {
        "name": "hammer",
        "sprite": None,
        "state": 0,  # 0: not used, 1: used CURRENTLY NO USE
        "scale": 0.5,
        "display": False,
        "path": "img/items/doorLeft/hammer.png"
    },
    {
        "name": "rag",
        "sprite": None,
        "state": 0,
        "scale": 0.11,
        "display": False,
        "path": "img/items/mainTheme/ragSmall.png"
    },
    {
        "name": "lighter",
        "sprite": None,
        "state": 0,  # 0: small, 1: took
        "scale": 0.4,
        "display": False,
        "path": "img/items/back/lighter.png"
    },
    {
        "name": "key",
        "sprite": None,
        "state": 0,  # 0: small, 1: took
        "scale": 0.4,
        "display": False,
        "path": "img/items/doorLeft/key.png"
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
            "scale": 0.8
        },
        {
            "name": "book2",
            "path": "img/items/back/book2.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book3",
            "path": "img/items/back/book3.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book4",
            "path": "img/items/back/book4.png",
            "sp": None,
            "scale": 0.8
        },
        {
            "name": "book5",
            "path": "img/items/back/book5.png",
            "sp": None,
            "scale": 0.8
        },
    ],
    "doorCode": [
        {
            "name": "c0",
            "path": "img/items/doorRight/c0.png",
        },
        {
            "name": "c1",
            "path": "img/items/doorRight/c1.png",
        },
        {
            "name": "c2",
            "path": "img/items/doorRight/c2.png",
        },
        {
            "name": "c3",
            "path": "img/items/doorRight/c3.png",
        },
        {
            "name": "c4",
            "path": "img/items/doorRight/c4.png",
        },
        {
            "name": "c5",
            "path": "img/items/doorRight/c5.png",
        },
        {
            "name": "c6",
            "path": "img/items/doorRight/c6.png",
        },
        {
            "name": "c7",
            "path": "img/items/doorRight/c7.png",
        },
        {
            "name": "c8",
            "path": "img/items/doorRight/c8.png",
        },
        {
            "name": "c9",
            "path": "img/items/doorRight/c9.png",
        }
    ]
}
