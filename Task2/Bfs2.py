from collections import deque
import parse_lay_file



def breadthFirstSearch(maze, start, goals):
  total_paths = []
  total_path_length = 0
  total_nodes_expanded = 0
  total_max_depth = 0
  total_max_fringe_size = 0

  for goal in goals:
      queue = deque([(start, [start])])
      visited = set()  # Keep track of visited nodes
      nodes_expanded = 0
      max_depth = 0
      max_fringe_size = 1

      while queue:
          current_position, path = queue.popleft()

          visited.add(current_position)
          nodes_expanded += 1

          row, col = current_position

          if (row, col) == goal:
              total_paths.append(path)
              total_path_length += len(path)
              total_nodes_expanded += len(visited)
              total_max_depth = max(total_max_depth, len(path))
              total_max_fringe_size = max(total_max_fringe_size, len(queue))
              break

          max_depth = max(max_depth, len(path))

          # Define possible movements (up, down, left, right)
          moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

          for move_row, move_col in moves:
              if 0 <= move_row < len(maze) and 0 <= move_col < len(maze[0]) \
                      and maze[move_row][move_col] != '%' and (move_row, move_col) not in visited:
                  queue.append(((move_row, move_col), path + [(move_row, move_col)]))
                  max_fringe_size = max(max_fringe_size, len(queue))

      total_nodes_expanded += nodes_expanded

  return total_paths, total_path_length, total_nodes_expanded, total_max_depth, total_max_fringe_size

