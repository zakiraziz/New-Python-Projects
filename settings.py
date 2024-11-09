import pygame as pg
from pygame.locals import *
import sys

# Initialize pygame
pg.init()

# Constants
vec = pg.math.Vector2
FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24, 89, 117)
SPRITE_DIR_PATH = 'assets/sprites'
FONT_PATH = 'assets/font/FREAKSOFNATUREMASSIVE.ttf'
ANIM_TIME_INTERVAL = 150  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15
TILE_SIZE = 50
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = int(FIELD_RES[0] * FIELD_SCALE_W), int(FIELD_RES[1] * FIELD_SCALE_H)
INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

# Set up display
screen = pg.display.set_mode(WIN_RES)
pg.display.set_caption("Tetris Clone")

# Load font (optional, make sure the font file exists at FONT_PATH)
try:
    font = pg.font.Font(FONT_PATH, 24)
except FileNotFoundError:
    font = pg.font.SysFont(None, 24)  # Fallback if font file is not found

# Clock to control FPS
clock = pg.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            # Additional controls for movement would go here

    # Clear screen
    screen.fill(BG_COLOR)

    # Render the field
    pg.draw.rect(screen, FIELD_COLOR, (0, 0, FIELD_RES[0], FIELD_RES[1]))

    # Draw a sample Tetromino for demonstration (optional)
    for pos in TETROMINOES['T']:  # Choose a Tetromino shape to draw, e.g., 'T'
        x, y = INIT_POS_OFFSET + vec(pos) * TILE_SIZE
        pg.draw.rect(screen, (200, 200, 200), (x, y, TILE_SIZE, TILE_SIZE))

    # Update the display
    pg.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit pygame
pg.quit()
sys.exit()
