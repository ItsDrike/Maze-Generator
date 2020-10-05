import typing as t
from dataclasses import dataclass

import pygame

from src.config import Options
from src.util import Colors


@dataclass
class Walls:
    top: bool
    right: bool
    bottom: bool
    left: bool


class Cell:
    def __init__(self, screen: pygame.Surface, col: int, row: int):
        self.screen = screen
        self.col = col
        self.row = row

        self.x = self.col * Options.cell_width
        self.y = self.row * Options.cell_width

        self.walls = Walls(True, True, True, True)

        self.visited = False

    @property
    def lines(self) -> t.Tuple[(t.Tuple[t.Tuple[int, int]], ) * 4]:
        """
        Get all lines which should be drawn to make up the cell.

        You can ignore certain lines by specifying them in `ignore` list
        for example:
        ignore=["top", "right"]
        will ignore both top and right lines on the cell.
        """
        top_line = (self.x, self.y), (self.x + Options.cell_width, self.y)
        right_line = (self.x + Options.cell_width, self.y), (self.x + Options.cell_width, self.y + Options.cell_width)
        bottom_line = (self.x, self.y + Options.cell_width), (self.x + Options.cell_width, self.y + Options.cell_width)
        left_line = (self.x, self.y), (self.x, self.y + Options.cell_width)

        ret = [top_line, right_line, bottom_line, left_line]

        if not self.walls.top:
            ret.remove(top_line)
        if not self.walls.right:
            ret.remove(right_line)
        if not self.walls.bottom:
            ret.remove(bottom_line)
        if not self.walls.left:
            ret.remove(left_line)
        return tuple(ret)

    def draw(self) -> None:
        """Draw individual cell."""
        for line in self.lines:
            pygame.draw.line(
                self.screen, Colors.WHITE,
                *line
            )
        if self.visited:
            pygame.draw.rect(
                self.screen, Colors.PURPLE,
                (self.x + 1, self.y + 1, Options.cell_width - 1, Options.cell_width - 1)
            )
