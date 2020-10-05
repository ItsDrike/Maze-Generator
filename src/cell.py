import math
import random
import typing as t
from dataclasses import dataclass

import pygame

from src.config import Options, Window
from src.util import Colors


@dataclass
class Walls:
    top: bool
    right: bool
    bottom: bool
    left: bool


class Cell:
    total_cols = math.floor(Window.width / Options.cell_width)
    total_rows = math.floor(Window.height / Options.cell_width)

    def __init__(self, screen: pygame.Surface, row: int, col: int):
        self.screen = screen
        self.row = row
        self.col = col

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
                self.screen, Colors.BLACK,
                *line, 5
            )
        if self.visited:
            pygame.draw.rect(
                self.screen, Colors.WHITE,
                (self.x + 1, self.y + 1, Options.cell_width - 1, Options.cell_width - 1)
            )

    def highlight(self) -> None:
        pygame.draw.rect(
            self.screen, Colors.RED,
            (self.x + 1, self.y + 1, Options.cell_width - 1, Options.cell_width - 1)
        )

    @classmethod
    def get_2d(cls, cells: t.List["Cell"], row: int, col: int) -> t.Optional["Cell"]:
        if row < 0 or col < 0 or row >= cls.total_rows or col >= cls.total_cols:
            return None
        else:
            return cells[row * cls.total_cols + col]

    def check_neighbors(self, cells: t.List["Cell"]) -> t.Optional["Cell"]:
        neighbors = []

        top = self.get_2d(cells, self.row, self.col - 1)
        right = self.get_2d(cells, self.row + 1, self.col)
        bottom = self.get_2d(cells, self.row, self.col + 1)
        left = self.get_2d(cells, self.row - 1, self.col)

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        if neighbors:
            return random.choice(neighbors)
        return None

    def remove_wall(self, neighbor: "Cell") -> None:
        x = self.row - neighbor.row
        y = self.col - neighbor.col

        if x == 1:
            self.walls.top = False
            neighbor.walls.bottom = False
        elif x == -1:
            self.walls.bottom = False
            neighbor.walls.top = False
        elif y == 1:
            self.walls.left = False
            neighbor.walls.right = False
        elif y == -1:
            self.walls.right = False
            neighbor.walls.left = False
