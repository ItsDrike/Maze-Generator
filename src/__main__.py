from contextlib import suppress
from math import floor

import pygame
from loguru import logger

from src.cell import Cell
from src.config import Options, Window
from src.util import Colors


class Game:
    def __init__(self, width: int, height: int, fps: int) -> None:
        self.size = self.width, self.height = width, height

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.fps_clock = pygame.time.Clock()
        self.tick_rate = fps

        self.running = True

    def handle_user_event(self) -> None:
        """Handle pygame events (f.e.: quit, click)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False

    def redraw_screen(self) -> None:
        """
        Redraw all cells on the screen.

        This does not update the screen, it only redraws it.
        """
        self.screen.fill(Colors.GREY)

        for cell in self.cells:
            cell.draw()

    def update_screen(self, tick: bool = True) -> None:
        """
        Update the screen accordingly to `redraw_screen`
        also check for user event and tick (if not specified otherwise)
        """

        self.handle_user_event()

        if not self.running:
            return

        self.redraw_screen()
        pygame.display.update()
        if tick:
            self.fps_clock.tick(self.tick_rate)

    def main(self, cell_width: int) -> None:
        # Initial setup
        logger.info("Starting game")

        self.cols = floor(self.width / cell_width)
        self.rows = floor(self.height / cell_width)

        self.cells = []
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells.append(Cell(self.screen, row, col))

        self.current_cell = self.cells[0]

        # Main game loop
        while self.running:
            self.update_screen()

            self.current_cell.visited = True
            neighbor = self.current_cell.check_neighbors(self.cells)
            if neighbor:
                neighbor.visited = True
                neighbor.remove_wall(self.current_cell)
                self.current_cell = neighbor


game = Game(Window.width, Window.height, Window.tick_rate)

with suppress(KeyboardInterrupt):
    game.main(Options.cell_width)

logger.info("Game Stopped")
pygame.quit()
