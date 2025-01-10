import streamlit as st
import pygame
import numpy as np

# 게임 설정
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20

# 색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [WHITE, RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW]

# 블록 형태 정의
SHAPES = [
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1, 1]],          # I
    [[1, 1], [1, 1]],        # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

def create_grid():
    return np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

def draw_grid(screen, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = COLORS[grid[y, x]]
            pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
            pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def main():
    st.title("Tetris Game")
    st.write("Use the arrow keys to move the blocks. Press 'Q' to quit.")

    # Create a Pygame display
    screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE, GRID_HEIGHT * GRID_SIZE))
    clock = pygame.time.Clock()

    grid = create_grid()
    current_shape = np.array(SHAPES[0])
    current_pos = [0, GRID_WIDTH // 2 - len(current_shape[0]) // 2]

    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen, grid)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
