import pygame

WALL    = 1 << 0

PELLET  = 1 << 0
SPELLET = 1 << 1

DOWN    = 1 << 3
UP      = 1 << 2
RIGHT   = 1 << 1
LEFT    = 1 << 0

Y_DIRECTION = 1
PLUS_WAY    = 1

pygame.font.init()
FONT = pygame.font.Font('fonts/ARCADECLASSIC.TTF', 20)

WALL_SPRITES = [
    pygame.image.load('images/wall_0000.png'),
    pygame.image.load('images/wall_0001.png'),
    pygame.image.load('images/wall_0002.png'),
    pygame.image.load('images/wall_0003.png'),
    pygame.image.load('images/wall_0004.png'),
    pygame.image.load('images/wall_0005.png'),
    pygame.image.load('images/wall_0006.png')
]

PELLET_SPRITES = [
    pygame.image.load('images/pellet_0000.png'),
    pygame.image.load('images/pellet_0001.png')
]

# GHOSTS

GHOSTS_SPRITES = [
    [ # blinky
        [
            [
                pygame.image.load('images/blinky/left_0000.png'),
                pygame.image.load('images/blinky/left_0001.png')
            ],
            [
                pygame.image.load('images/blinky/right_0000.png'),
                pygame.image.load('images/blinky/right_0001.png')
            ]
        ],

        [
            [
                pygame.image.load('images/blinky/up_0000.png'),
                pygame.image.load('images/blinky/up_0001.png')
            ],
            [
                pygame.image.load('images/blinky/down_0000.png'),
                pygame.image.load('images/blinky/down_0001.png')
            ]
        ]
    ],

    [ # pinky
        [
            [
                pygame.image.load('images/pinky/left_0000.png'),
                pygame.image.load('images/pinky/left_0001.png')
            ],
            [
                pygame.image.load('images/pinky/right_0000.png'),
                pygame.image.load('images/pinky/right_0001.png')
            ]
        ],

        [
            [
                pygame.image.load('images/pinky/up_0000.png'),
                pygame.image.load('images/pinky/up_0001.png')
            ],
            [
                pygame.image.load('images/pinky/down_0000.png'),
                pygame.image.load('images/pinky/down_0001.png')
            ]
        ]
    ],

    [ # inky
        [
            [
                pygame.image.load('images/inky/left_0000.png'),
                pygame.image.load('images/inky/left_0001.png')
            ],
            [
                pygame.image.load('images/inky/right_0000.png'),
                pygame.image.load('images/inky/right_0001.png')
            ]
        ],

        [
            [
                pygame.image.load('images/inky/up_0000.png'),
                pygame.image.load('images/inky/up_0001.png')
            ],
            [
                pygame.image.load('images/inky/down_0000.png'),
                pygame.image.load('images/inky/down_0001.png')
            ]
        ]
    ],

    [ # clyde
        [
            [
                pygame.image.load('images/clyde/left_0000.png'),
                pygame.image.load('images/clyde/left_0001.png')
            ],
            [
                pygame.image.load('images/clyde/right_0000.png'),
                pygame.image.load('images/clyde/right_0001.png')
            ]
        ],

        [
            [
                pygame.image.load('images/clyde/up_0000.png'),
                pygame.image.load('images/clyde/up_0001.png')
            ],
            [
                pygame.image.load('images/clyde/down_0000.png'),
                pygame.image.load('images/clyde/down_0001.png')
            ]
        ]
    ],

    [ # frightened
        pygame.image.load('images/ghost_frightened_0000.png'),
        pygame.image.load('images/ghost_frightened_0001.png')
    ]
]


_pac = pygame.image.load('images/pacman_0000.png')

PACMAN_SPRITES = [
    [
        [
            pygame.image.load('images/pacman_left_0000.png'),
            pygame.image.load('images/pacman_left_0001.png'),
            _pac
        ],
        [
            pygame.image.load('images/pacman_right_0000.png'),
            pygame.image.load('images/pacman_right_0001.png'),
            _pac
        ]
    ],

    [
        [
            pygame.image.load('images/pacman_up_0000.png'),
            pygame.image.load('images/pacman_up_0001.png'),
            _pac
        ],
        [
            pygame.image.load('images/pacman_down_0000.png'),
            pygame.image.load('images/pacman_down_0001.png'),
            _pac
        ]
    ]
]
