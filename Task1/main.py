import A_star
import BFS
import parse_lay_file

def print_maze(path, maze):
  if path:
      for position in path:
          row, col = position
          maze[row][col] = "*"
      for row in maze:
          print(''.join(row))

def print_results(path, cost, nodes_expanded, max_depth, max_fringe_size, maze):
  if path:
    print_maze(path, maze)
    print("Solution Path:", path)
    print("Solution Cost:", cost)
    print("Number of Nodes Expanded:", nodes_expanded)
    print("Maximum Tree Depth Searched:", max_depth)
    print("Maximum Size of the Fringe:", max_fringe_size, "\n")
  else:
    print("No path found")


def main():
  big_maze, big_start, big_goal = parse_lay_file.parse_lay_file('bigMaze.lay')
  med_maze, med_start, med_goal = parse_lay_file.parse_lay_file('mediumMaze.lay')
  small_maze, small_start, small_goal = parse_lay_file.parse_lay_file('smallMaze.lay')
  open_maze, open_start, open_goal = parse_lay_file.parse_lay_file('openMaze.lay')

  
  ##################################################Task 1 Test: BFS#############################################################################
  ##########Big Maze##################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = BFS.breadth_first_search(big_maze, big_start, big_goal)
  print("BFS on big maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, big_maze)


  #########Medium Maze################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = BFS.breadth_first_search(med_maze, med_start, med_goal)
  print("BFS on medium maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, med_maze)

  ##########Small Maze################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = BFS.breadth_first_search(small_maze, small_start, small_goal)
  print("BFS on small maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, small_maze)
  
  ##########Open Maze###################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = BFS.breadth_first_search(open_maze, open_start, open_goal)
  print("BFS on open maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, open_maze)
   
  ############################################################Task 1 Test: A* search####################################################################
  ##########Big Maze##################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = A_star.astar_search(big_maze, big_start, big_goal)
  print("A* search on big maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, big_maze)
  
  #########Medium Maze################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = A_star.astar_search(med_maze, med_start, med_goal)
  print("A* search on medium maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, med_maze)
  
  ##########Small Maze################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = A_star.astar_search(small_maze, small_start, small_goal)
  print("A* search on small maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, small_maze)
  
  ##########Open Maze###################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = A_star.astar_search(open_maze, open_start, open_goal)
  print("A* search on open maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, open_maze)
   
if __name__ == "__main__":
  main()