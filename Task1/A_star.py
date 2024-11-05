from collections import deque


def manhattan_distance(pos1, pos2):
  #Calculate the Manhattan distance between two positions
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar_search(maze, start, goals):
  #Initialize queue with start position, path, and cost
  queue = deque([(start, [start], 0)]) 
  visited = set()
  max_tree_depth = 0
  max_fringe_size = 1

  while queue:
      current_position, path, cost = queue.popleft()
      max_tree_depth = max(max_tree_depth, len(path) - 1)
      if current_position in visited:
          continue

      visited.add(current_position)

      if current_position in goals:
          return path, cost, len(visited), max_tree_depth, max_fringe_size

      row, col = current_position

      #Define possible movements (up, down, left, right)
      moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

      for move_row, move_col in moves:
          if 0 <= move_row < len(maze) and 0 <= move_col < len(maze[0]) \
                  and maze[move_row][move_col] != '%' \
                  and (move_row, move_col) not in visited:
              new_cost = cost + 1 
              heuristic = min(manhattan_distance((move_row, move_col), goal) for goal in goals)
              total_cost = new_cost + heuristic 
              queue.append(((move_row, move_col), path + [(move_row, move_col)], \
                            total_cost))
              max_fringe_size = max(max_fringe_size, len(queue))

  return None, None, None, None, None  # If no path found

