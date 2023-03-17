import time

def bomber_man(n, grid):

    def detonation(arr,i,j):
        arr[i][j] = '.'
        if i !=0 and j != 0:
            try:
                arr[i][j-1] = '.'
            except:
                pass
            try:
                arr[i][j+1] = '.'
            except:
                pass
            try:
                arr[i-1][j] = '.'
            except:
                pass
            try:
                arr[i+1][j] = '.'
            except:
                pass

    arr = []
    for i in range(len(grid)):
        arr.append(list(grid[i]))
        grid[i] = list(grid[i])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if arr[i][j] == '.':
                arr[i][j] = 'O'

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                detonation(arr,i,j)

    for i in range(len(arr)):
        arr[i] = ''.join(arr[i])

    return arr

def Print(arr):
    for i in arr:
        print(i,'\n')



n = 9
grid = [
    '.......',
    '...O...',
    '....O..',
    '.......',
    'OO.....',
    'OO.....'
]


time.sleep(n/3)
Print(grid)
time.sleep(n/3)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print('O',end='')
    print('\n')

time.sleep(n/3)
Print(bomber_man(n, grid))