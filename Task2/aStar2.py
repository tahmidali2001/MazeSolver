from collections import deque
import parse_lay_file

def manhattan_distance(pos1, pos2):
  # Calculate the Manhattan distance between two positions
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar_search(maze, start, goals):
  total_path = []
  total_cost = 0
  total_nodes_expanded = 0
  total_max_depth = 0
  total_max_fringe_size = 0
  
  for goal in goals:
      queue = deque([(start, [start], 0)]) 
      visited = set()  # Track visited nodes
      max_tree_depth = 0
      max_fringe_size = 1
  
      while queue:
          current_position, path, cost = queue.popleft()
          max_tree_depth = max(max_tree_depth, len(path) - 1)
          visited.add(current_position)
  
          if current_position == goal:
              total_path.append(path)
              total_cost += cost
              total_nodes_expanded += len(visited)
              total_max_depth = max(total_max_depth, max_tree_depth)
              total_max_fringe_size = max(total_max_fringe_size, len(queue))
              break
  
          row, col = current_position
  
          # Define possible movements (up, down, left, right)
          moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
  
          for move_row, move_col in moves:
            if 0 <= move_row < len(maze) and 0 <= move_col < len(maze[0]) \
                    and maze[move_row][move_col] != '%' and (move_row, move_col) not in visited:
                new_cost = cost + 1 
                heuristic = manhattan_distance((move_row, move_col), goal)
                total_new_cost = new_cost + heuristic
                queue.append(((move_row, move_col), path + [(move_row, move_col)], total_new_cost))
                max_fringe_size = max(max_fringe_size, len(queue))
  
  return total_path, total_cost, total_nodes_expanded, total_max_depth, total_max_fringe_size

