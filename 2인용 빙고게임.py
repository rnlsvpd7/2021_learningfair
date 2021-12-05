import random 
a = input('O/선 플레이어, 당신의 이름은? ')
b = input('X/후 플레이어, 당신의 이름은? ')

print("빙고를 만들어라~!!")

def print_grid(grid):
    print()
    print(grid[2][0], '|',  grid[2][1], '|', grid[2][2])
    print('----------')
    print(grid[1][0], '|', grid[1][1], '|', grid[1][2])
    print('----------')
    print(grid[0][0], '|', grid[0][1], '|', grid[0][2])

def free_position(grid, column_index, row_index):

    return grid[row_index][column_index] == ' '

def winner(grid, mark):
    if (grid[0][0] == mark and grid[0][1] == mark and grid[0][2] == mark) or\
    (grid[1][0] == mark and grid[1][1] == mark and grid[1][2] == mark) or\
    (grid[2][0] == mark and grid[2][1] == mark and grid[2][2] == mark) or\
    (grid[0][0] == mark and grid[1][0] == mark and grid[2][0] == mark) or\
    (grid[0][1] == mark and grid[1][1] == mark and grid[2][1] == mark) or\
    (grid[0][2] == mark and grid[1][2] == mark and grid[2][2] == mark) or\
    (grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark) or\
    (grid[2][0] == mark and grid[1][1] == mark and grid[0][2] == mark):
        return True
    else:
        return False

def grid_full(grid):
    if grid[0][0] != ' ' and \
    grid[0][1] != ' ' and \
    grid[0][2] != ' ' and \
    grid[1][0] != ' ' and \
    grid[1][1] != ' ' and \
    grid[1][2] != ' ' and \
    grid[2][0] != ' ' and \
    grid[2][1] != ' ' and \
    grid[2][2] != ' ':
        return True
    else:
        return False

print('게임설명:')
print('X 마크를 연속으로 세개 놓는 게임!!')
print('왼쪽 하단에서 오른쪽방향으로 1 부터 9 입니다.')

grid = [[' ', ' ', ' '], 
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

print_grid(grid)    

turn = 0 
while True:
    if turn == 0:
        number = int(input(f'{a}님 O 를 놓을 위치 번호를 선택하세요 (1 ~ 9): '))
        if number >= 1 and number <= 3:
            column_index = number - 1
            row_index = 0
        elif number >= 4 and number <= 6:
            column_index = number - 4
            row_index = 1
        elif number >= 7 and number <= 9:
            column_index = number - 7
            row_index = 2

        if free_position(grid, column_index, row_index):
            grid[row_index][column_index] = 'O'

            print_grid(grid)

            if winner(grid, 'O'):
                print(' ■■■ ■■■ ■   ■  ■■■ ■■      ■   ■■■ ■■■  ■')
                print('■      ■  ■ ■■ ■ ■      ■  ■  ■  ■   ■   ■      ■')
                print('■      ■  ■ ■ ■■ ■   ■ ■■    ■■■   ■     ■      ')
                print(' ■■■ ■■■ ■   ■  ■■■ ■  ■ ■    ■  ■ ■■■    ■')
                print(f'{a} 승리')
                break
            elif grid_full(grid):
                print('■■■  ■■      ■    ■    ■')
                print('■   ■ ■  ■  ■  ■  ■    ■')
                print('■   ■ ■■    ■■■  ■ ■ ■')
                print('■■■  ■  ■ ■    ■  ■  ■')
                print('무승부')
                break

            turn += 1
            turn %= 2

    elif turn == 1:     
        number = int(input(f'{b}님 X 를 놓을 위치 번호를 선택하세요 (1 ~ 9): '))
        if number >= 1 and number <= 3:
            column_index = number - 1
            row_index = 0
        elif number >= 4 and number <= 6:
            column_index = number - 4
            row_index = 1
        elif number >= 7 and number <= 9:
            column_index = number - 7
            row_index = 2

        if free_position(grid, column_index, row_index):
            grid[row_index][column_index] = 'X'  

            print_grid(grid)

            if winner(grid, 'X'):
                print(' ■■■ ■■■ ■   ■  ■■■ ■■      ■   ■■■ ■■■  ■')
                print('■      ■  ■ ■■ ■ ■      ■  ■  ■  ■   ■   ■      ■')
                print('■      ■  ■ ■ ■■ ■   ■ ■■    ■■■   ■     ■      ')
                print(' ■■■ ■■■ ■   ■  ■■■ ■  ■ ■    ■  ■ ■■■    ■')
                print(f'{b} 승리')
                break
            elif grid_full(grid):
                print('■■■  ■■      ■    ■    ■')
                print('■   ■ ■  ■  ■  ■  ■    ■')
                print('■   ■ ■■    ■■■  ■ ■ ■')
                print('■■■  ■  ■ ■    ■  ■  ■')
                print('무승부.')
                break

            turn += 1
            turn %= 2
