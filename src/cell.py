import pygame

from src.config import Options
from src.util import Colors


class Cell:
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        self.screen = screen
        self.x = x  # col
        self.y = y  # row

    def draw(self) -> None:
        pygame.draw.rect(
            self.screen, Colors.WHITE,
            (
                self.x * Options.cell_width,
                self.y * Options.cell_width,
                Options.cell_width,
                Options.cell_width,
            ),
            1
        )
