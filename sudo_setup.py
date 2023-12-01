import random

def given_num():
  given_numbers = 0
  given_valid = False
  while not given_valid:
    list_occur = [0,1,1,2,2,2,3,3,4,4,4,5,6]      # how many times a number from one to nine is given, 9 could be given zero times
    list_numbers = []
    for i in range(9):
      number = random.choice(list_occur)
      list_occur.remove(number)
      list_numbers.append(number)
    given_numbers = sum(list_numbers)
    if given_numbers == 28:                       # the sum total of all the numbers should be equal to 28 which gives 28 given numbers
      given_valid = True
      break

  ONE_TO_NINE = {k:0 for k in range(1,10)}
  for key in ONE_TO_NINE:
    number_ran = random.choice(list_numbers)
    ONE_TO_NINE[key] = number_ran
    list_numbers.remove(number_ran)
  return ONE_TO_NINE

One_to_nine = given_num()
ROW_RANGE = 9
COL_RANGE = 9
BLOCK_RANGE = 9

# ----------------------------- original ------------------------------ #
class Given_numbers :
  def __init__(self):
    self.dict_numbers = One_to_nine       # the value always stays the same just the positions of the numbers are changed
    self.main_rows = [[0 for x in range(COL_RANGE)] for y in range(ROW_RANGE)]
    self.main_cols = [[0 for y in range(ROW_RANGE)] for x in range(COL_RANGE)]
    self.main_blocks = {k:[[0 for x in range(3)] for y in range(3)] for k in range(BLOCK_RANGE)}

  # the key in the dictionary represents the numbers 1 to 9 to be represented in the card
    for key in self.dict_numbers:
      for times in range(self.dict_numbers[key]):     # randomly places the key of the dictionary x amount of times on the card
        self.chosen_number = key
        self.col_list_index = random.randint(0,COL_RANGE-1)
        self.col_index = random.randint(0,ROW_RANGE-1)
        self.row_list_index = self.col_index
        self.row_index = self.col_list_index
        self.valid = False
        
        while not self.valid:
          if self.hori_check() and self.vert_check() and self.block_check() and self.square_check():
            self.main_rows[self.row_list_index][self.row_index] = self.chosen_number
            self.main_cols[self.col_list_index][self.col_index] = self.chosen_number
            self.main_blocks[self.block_num()][self.row_list_index%3][self.row_index%3] = self.chosen_number
            self.valid = True
            break

    with open("Example.txt","w") as file:
      for row in self.main_rows:
        file.write(f'{" ".join(map(str,row))}\n')

  def square_check(self):   # checks if the square is not contain a number
    if self.main_cols[self.col_list_index][self.col_index] == 0:
      return True
    else:
      self.col_list_index = random.randint(0,COL_RANGE-1)
      self.col_index = random.randint(0,ROW_RANGE-1)
      self.row_list_index = self.col_index
      self.row_index = self.col_list_index
    return False

  def hori_check(self):     # checks the row for the same number if true it chooses a different square
    if self.chosen_number in self.main_rows[self.row_list_index]:
      self.col_list_index = random.randint(0,COL_RANGE-1)
      self.col_index = random.randint(0,ROW_RANGE-1)
      self.row_list_index = self.col_index
      self.row_index = self.col_list_index
      return False
    else:
      return True
  
  def vert_check(self):    # checks the column for the same number if true it chooses a different square
    if self.chosen_number in self.main_cols[self.col_list_index]:
      self.col_list_index = random.randint(0,COL_RANGE-1)
      self.col_index = random.randint(0,ROW_RANGE-1)
      self.row_list_index = self.col_index
      self.row_index = self.col_list_index
      return False
    else:
      return True
  
  def block_check(self):    # checks the block for the same number if true it chooses a different square
    for row in self.main_blocks[self.block_num()]:
      if self.chosen_number in row:
        self.col_list_index = random.randint(0,COL_RANGE-1)
        self.col_index = random.randint(0,ROW_RANGE-1)
        self.row_list_index = self.col_index
        self.row_index = self.col_list_index
        return False
    return True
  
  def block_num(self):  # gets the correct key from main_block proportional to the chosen indexes for the square
    if 2 >= self.row_list_index >= 0:
      self.block_add = 0
    if 5 >= self.row_list_index >= 3:
      self.block_add = 2
    if 8 >= self.row_list_index >= 6:
      self.block_add = 4
    
    self.func_block_key = self.col_list_index//3 + self.row_list_index//3 + self.block_add
    return self.func_block_key
