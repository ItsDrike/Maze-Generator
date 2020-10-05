# Maze Generator

This project was created purely for fun, it isn't meant to be used as an actual maze generator.
Although it's not impossible, but I'd advice removing the pygame GUI as that is a significant speed limitation.

## Visual example

![Maze GIF](https://user-images.githubusercontent.com/20902250/95110541-778c9200-073e-11eb-80b8-2e6c9ba617cd.gif)

## How does it work

The implementation I used is the depth-first search algorithm with backtracking. Explained simply, this is how it works:
First make a grid of cells and choose some starting cell

1. Mark this initial cell as current cell
2. Mark current cell as visited
3. While there are unvisited cells:
   1. If the current cell has any neighbors which have not been visited:
      1. Choose one of those neighbors randomly
      2. Push the current cell to the stack
      3. Remove the wall between the current cell and the chosen cell
      4. Make the chosen cell the current cell
      5. Mark chosen cell as visited
   2. Else if stack is not empty:
      1. Pop the cell from the stack
      2. Make that cell the current cell

To explain the algorithm briefly:
You need to go through the cells from some starting (first) cell and as it goes it chooses it's neighbor cell randomly. This can be for example the cell to the left. When it does that it removes the walls between this cell and the random neighbor cell. Then it repeats itself from the neighbor cell.
This is the basics of any depth-first search but the problem with this is that eventually it will reach a point where there are no neighbor cells which weren't visited already. At that point you need to implement backtracking. Luckily that's quite simple, all you need is a stack to which you'll push each time you visit a new cell and when you get stuck you simply pop the last position from the stack and go back. If that cell doesn't have any neighbors either, repeat this until you find a cell which does. Once you did that, you can continue the depth-first search.

If you're interesting in implementing this algorithm yourself, I'd recommend you to check the [wiki page](https://en.wikipedia.org/wiki/Maze_generation_algorithm) about maze generation, it explains it in detail and also gives you some other options apart from the depth-first search.
