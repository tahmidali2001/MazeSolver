from collections import deque


def breadth_first_search(maze, start, goals):
  #Initialize queue with start position and path
  queue = deque([(start, [start])])
  visited = set()  #Keep track of visited nodes
  max_depth = 0
  max_fringe_size = 1

  while queue:
    current_position, path = queue.popleft()
    if current_position in visited:
      continue

    visited.add(current_position)

    row, col = current_position

    if current_position in goals:
      return path, len(path), len(visited), max_depth, max_fringe_size

    max_depth = max(max_depth, len(path))

    #Define possible movements (up, down, left, right)
    moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    for move_row, move_col in moves:
      if 0 <= move_row < len(maze) and 0 <= move_col < len(maze[0]) \
              and maze[move_row][move_col] != '%' \
              and (move_row, move_col) not in visited:
        queue.append(((move_row, move_col), path + [(move_row, move_col)]))
        max_fringe_size = max(max_fringe_size, len(queue))

  return None, 0, len(visited), max_depth, max_fringe_size  #If no path found
