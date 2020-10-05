import typing as t

import pygame

from src.config import Options
from src.util import Colors


class Cell:
    def __init__(self, screen: pygame.Surface, col: int, row: int):
        self.screen = screen
        self.col = col
        self.row = row

        self.x = self.col * Options.cell_width
        self.y = self.row * Options.cell_width

    def lines(self, ignore: t.Optional[t.List[str]] = None) -> t.Tuple[(t.Tuple[t.Tuple[int, int]], ) * 4]:
        """
        Get all lines which should be drawn to make up the cell.

        You can ignore certain lines by specifying them in `ignore` list
        for example:
        ignore=["top", "right"]
        will ignore both top and right lines on the cell.
        """
        top_line = (self.x, self.y), (self.x + Options.cell_width, self.y)
        left_line = (self.x, self.y), (self.x, self.y + Options.cell_width)
        right_line = (self.x + Options.cell_width, self.y), (self.x + Options.cell_width, self.y + Options.cell_width)
        bottom_line = (self.x, self.y + Options.cell_width), (self.x + Options.cell_width, self.y + Options.cell_width)

        ret = [top_line, left_line, right_line, bottom_line]

        if not ignore:
            return tuple(ret)
        if "top" in ignore:
            ret.remove(top_line)
        if "left" in ignore:
            ret.remove(left_line)
        if "right" in ignore:
            ret.remove(right_line)
        if "bottom" in ignore:
            ret.remove(bottom_line)
        return tuple(ret)

    def draw(self) -> None:
        """Draw individual cell."""
        for line in self.lines():
            pygame.draw.line(
                self.screen, Colors.WHITE,
                *line
            )
