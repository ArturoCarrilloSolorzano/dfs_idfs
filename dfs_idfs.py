import itertools
import random
import time

def num_matrix(rows, cols, steps=25):
    nums = list(range(1, rows * cols)) + [0]
    goal = [ nums[i:i+rows] for i in range(0, len(nums), rows) ]

    puzzle = goal
    for steps in range(steps):
        puzzle = random.choice(gen_kids(puzzle))

    return puzzle, goal


def gen_kids(puzzle):
    for row, level in enumerate(puzzle):
        for column, item in enumerate(level):
            if(item == 0):
                kids = get_kids(row, column, puzzle)
                return kids

def get_kids(row, column, puzzle):
    kids = []
    if(row > 0 ):
        kids.append(swap(row - 1, column, row, column, puzzle))
    if(row < 2):
        kids.append(swap(row + 1, column, row, column, puzzle))
    if(column > 0):
        kids.append(swap(row, column - 1, row, column, puzzle))
    if(column < 2):
        kids.append(swap(row, column + 1, row, column, puzzle))
    
    return kids

def swap(row, col, zrow, zcol, array):
    import copy
    s = copy.deepcopy(array)
    s[zrow][zcol], s[row][col] = s[row][col], s[zrow][zcol]
    return s

def dfs(puzzle, goal):
    stack = []
    visited = [puzzle]
    stack.append([puzzle])
    while stack:
        path = stack.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for adjacent in gen_kids(node):
            if adjacent not in visited:
                visited.append(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                stack.append(new_path)


def id_dfs(puzzle, goal):
    def idfs(path, depth):
        if depth == 0:
            return
        if path[-1] == goal:
            return path
        for move in gen_kids(path[-1]):
            if move not in path:
                next_path = idfs(path + [move], depth - 1)
                if next_path:
                    return next_path
    for depth in itertools.count():
        path = idfs([puzzle], depth)
        if path:
            return path

puzzle, goal = num_matrix(3,3, 30)
total_time = 0
print(goal)
print(puzzle)
t0 = time.time()
solution = dfs(puzzle, goal)
t1 = time.time()
total_time += t1 - t0
print('Puzzle resuelto en', total_time, 'segundos.')
for level in solution:
    for item in level:
        print(item)
    print("\n")
print(goal)
print(puzzle)
total_time = 0
t0 = time.time()
solution = id_dfs(puzzle, goal)
t1 = time.time()
total_time += t1 - t0
print('Puzzle resuelto en', total_time, 'segundos.')
for level in solution:
    for item in level:
        print(item)
    print("\n")