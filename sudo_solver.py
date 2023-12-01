from sudo_setup import Given_numbers

ROW_RANGE = 9
COLUMN_RANGE = 9
BLOCK_RANGE = 9

def block_check(num,block_key):
  global BLOCKS
  for row in BLOCKS[block_key]:
    if num in row:
      return False
  
  return True

class Solver:
# --------------------------- MAIN -------------------------#
  def __init__(self):
    self.possible = False
    self.not_poss = 0
    while not self.possible:    # generates a new card each time it is not possible to solve the current card using the same amount of numbers that need to be shown, example 1 needs to appear twice on the card
      self.shuffle = True      
      self.grid,self.rows,self.columns,self.blocks = self.generator()
      
      for times in range(3):       # if row_check and col_check is called at least 3 times it gaurentees that it should be solved
        self.row_check()
        self.col_check()
      for row in self.grid:
        if 0 in row:
          self.shuffle = True
          break
        else:
          self.shuffle = False
      
      if self.shuffle == False:
        self.possible = True
        break
      else:
        self.not_poss += 1

# ----------------------- card generator ------------------- #
  def generator(self):
    self.rows = []
    self.columns = []
    self.blocks = {k:[[0 for v in range(3)] for v in range(3)] for k in range(BLOCK_RANGE)}

# self.generate calls the class given numbers and each time it is called it shuffles the given numbers on the card to new positions
    self.generate = Given_numbers()    
    with open("Example.txt") as file:
      content = file.readlines()
      self.grid = [list(map(int, (item.strip("\n").split()))) for item in content]
    
    for row in range(ROW_RANGE):
      if 2>=row>=0:
        block_add = 0
      if 5>=row>=3:
        block_add = 2
      if 8>=row>=6:
        block_add = 4
      self.rows.append(self.grid[row].copy())
      for column in range(COLUMN_RANGE):
        self.block_key = row//3 + column//3 + block_add
        self.blocks[self.block_key][row%3][column%3] = self.grid[row][column]
    
    for column in range(COLUMN_RANGE):
      temp_list = []
      for row in range(ROW_RANGE):
        temp_list.append(self.grid[row][column])
      self.columns.append(temp_list)
    return self.grid, self.rows, self.columns, self.blocks
  
# ---------------------- block check ----------------- #
  def block_check(self,num):
    for row in self.blocks[self.block_key]:
      if num in row:
        return False
    
    return True
  
# ----------------------- row check ------------------- #
  def row_check(self):
    for row in range(ROW_RANGE):
      if 2>=row>=0:
        block_add = 0
      if 5>=row>=3:
        block_add = 2
      if 8>=row>=6:
        block_add = 4
      for num in range(1,10):
        count_num = 0
        for col in range(COLUMN_RANGE):
          self.block_key = col//3 + row//3 + block_add
          if num not in self.rows[row] and num not in self.columns[col] and self.rows[row][col] == 0 and self.block_check(num):
            count_num += 1
        
        if count_num == 1:
          for col in range(COLUMN_RANGE):
            self.block_key = col//3 + row//3 + block_add
            if num not in self.rows[row] and num not in self.columns[col] and self.rows[row][col] == 0 and self.block_check(num):
              self.grid[row][col] = num
              self.rows[row][col] = num
              self.columns[col][row] = num
              self.blocks[self.block_key][row%3][col%3] = num
              self.row_check()
  
# ---------------------- columns check ------------------------- #
  def col_check(self):
    for col in range(COLUMN_RANGE):
      for num in range(1,10):
        count_num = 0
        for row in range(ROW_RANGE):
          if 2>= row >=0:
            block_add = 0
          if 5>=row>=3:
            block_add = 2
          if 8>=row>=6:
            block_add = 4
          
          self.block_key = col//3 + row//3 + block_add
          if num not in self.rows[row] and num not in self.columns[col] and self.columns[col][row] == 0 and self.block_check(num):
            count_num += 1
        
        if count_num == 1:
          for row in range(ROW_RANGE):
            if 2>= row >=0:
              block_add = 0
            if 5>=row>=3:
              block_add = 2
            if 8>=row>=6:
              block_add = 4
            self.block_key = col//3 + row//3 + block_add
            if num not in self.rows[row] and num not in self.columns[col] and self.columns[col][row] == 0 and self.block_check(num):
              self.grid[row][col] = num
              self.rows[row][col] = num
              self.columns[col][row] = num
              self.blocks[self.block_key][row%3][col%3] = num
              self.col_check()