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

FONT = 'fonts/ARCADECLASSIC.TTF'

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
