def parse_lay_file(filename):
  with open(filename, 'r') as file:
      maze = []
      start_position = None
      goals = []

      for row_idx, line in enumerate(file):
          row = []
          for col_idx, char in enumerate(line.strip()):
              if char == '%':
                  row.append('%')
              elif char == 'P':
                  row.append('S')
                  start_position = (row_idx, col_idx)
              elif char == '.':
                  row.append('G')
                  goals.append((row_idx, col_idx))
              elif char == ' ':
                  row.append(' ')
          maze.append(row)
        
  return maze, start_position, goals
