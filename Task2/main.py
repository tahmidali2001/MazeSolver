import aStar2
import Bfs2
import parse_lay_file


def print_maze(paths, maze):
    if paths:
      for path in paths:
        for position in path:
          row, col = position
          maze[row][col] = '*'
      for row in maze:
        print(''.join(row))  # Print each row of the maze


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
  small_maze, small_start, small_goal = parse_lay_file.parse_lay_file(
      'Task2/smallSearch.lay')
  tiny_maze, tiny_start, tiny_goal = parse_lay_file.parse_lay_file(
      'Task2/tinySearch.lay')
  tricky_maze, tricky_start, tricky_goal = parse_lay_file.parse_lay_file(
      'Task2/trickySearch.lay')

  ##################################Task 1 Test: BFS#############################
  ##############Small Maze##################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = Bfs2.breadthFirstSearch(small_maze, small_start, small_goal)
  print("BFS on Small Search maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, small_maze)

  #########Tiny Maze################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = Bfs2.breadthFirstSearch(tiny_maze, tiny_start, tiny_goal)
  print("BFS on Tiny Search maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, tiny_maze)

  ##########Tricky Maze################
  bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size = Bfs2.breadthFirstSearch(tricky_maze, tricky_start, tricky_goal)
  print("BFS on Tricky Search maze")
  print_results(bfs_path, bfs_cost, bfs_nodes_expanded, bfs_max_tree_depth, bfs_max_fringe_size, tricky_maze)

  ############################################################Task 1 Test: A* search####################################################################
  ##########Small Maze##################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = aStar2.astar_search(small_maze, small_start, small_goal)
  print("A* search on Small Search maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, small_maze)

  #########Tiny Maze################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = aStar2.astar_search(tiny_maze, tiny_start, tiny_goal)
  print("A* search on Tiny Search maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, tiny_maze)
 
  ##########Tricky Maze################
  astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size = aStar2.astar_search(tricky_maze, tricky_start, tricky_goal)
  print("A* search on Tricky Search maze")
  print_results(astar_path, astar_cost, astar_nodes_expanded, astar_max_tree_depth, astar_max_fringe_size, tricky_maze)

  


if __name__ == "__main__":
  main()
