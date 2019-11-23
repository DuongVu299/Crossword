# DUONG VU
# STUDENT ID: 500941776
# SECTION 6

blank = " "
board = [[blank] * 20 for i in range(20)]                       # Create a 20x20 grid

num_words = int(input("How many words to make crossword: "))
l = []

for i in range(num_words):
    l.append(input("Enter word: "))

placed_words = []                                               # Create a list of placed and unplaced words on the grid
unplaced_words = []

def printboard(board):
    '''
    Assumes the parameter board is a 20x20 2 dimensional array,
    Print every element of that array into a grid.
    '''    
    board_size = 20
    for y in range(-2, board_size + 2):
        for x in range(-1, board_size + 1):
            if y == -2 or y == board_size + 1:
                if x == -1 or x == board_size:
                    print(" ", end="")
                else:
                    print(x % 10, end="")
            elif y == -1 or y == board_size:
                if x == -1 or x == board_size:
                    print(" ", end="")
                else:
                    print("_", end="")
            else:
                if x == -1:
                    print("|", end="")
                elif x == board_size:
                    print("|", end=str(y))
                else:
                    print(board[x][y], end="")
        print("")

def addFirstWord(board, word):
    '''
    Assumes the parameter: board is a 20x20 2d array, word is a string.
    Add the word to the center of the grid.
    '''
    col = 20 // 2 - len(word) // 2
    row = 20 // 2

    for x in range(col, len(word) + col):
        board[x][row] = word[x - col]
    placed_words.append(word)

def checkvertical(board, word, row, col):
    '''
    Assumes the parameter:
    board is a 20x20 2d array,
    word is a string,
    row and col are 2 integers.
    Check if the word can be added to the board vertically at the given row and column.
    '''
    blank = 0
    if len(word) + row > 20:
        return False
        
    if row < 20 - len(word):
        if board[col][row + len(word)] != " ":
            return False
    if row > 0:
        if board[col][row - 1] != " ":
            return False

    for i in range(row, len(word) + row):
        if i >= 20:
            return False
        else:
            if board[col][i] == " ":
                if col == 0:
                    if board[col + 1][i] != " ":
                        return False
                if col == 19:
                    if board[col - 1][i] != " ":
                        return False
                else:
                    if board[col + 1][i] != " " or board[col - 1][i] != " ":
                        return False
                    else:
                        blank += 1
            else:
                if i - row != -1:
                    if board[col][i] != word[i - row]:
                        return False
                else:
                    return False

    if blank < len(word):
        return True
    else:
        return False            

def addvertical(board, word):
    '''
    Assumes the parameter:
    board is a 20x20 2d array,
    word is a string,
    Add the word to the grid vertically.
    '''
    for col in range(19):
        for row in range(20 - len(word) + 1):
            if checkvertical(board, word, row, col):
                for i in range(row, len(word) + row):
                    board[col][i] = word[i - row]
                placed_words.append(word)
                return True
    
    unplaced_words.append(word)
    return False

def checkhorizontal(board, word, row, col):
    '''
    Assumes the parameter:
    board is a 20x20 2d array,
    word is a string,
    row and col are 2 integers.
    Check if the word can be added to the board horizontally at the given row and column.
    '''
    blank = 0
    if len(word) + col > 20:
        return False

    if col < 20 - len(word):
        if board[col + len(word)][row] != " ":
            return False
    if col > 0:
        if board[col - 1][row] != " ":
            return False

    for i in range(col, len(word) + col):
        if i >= 20:
            return False
        else:
            if board[i][row] == " ":
                if row == 0:
                    if board[i][row + 1] != " ":
                        return False
                if row == 19:
                    if board[i][row - 1] != " ":
                        return False
                else:
                    if board[i][row + 1] != " " or board[i][row - 1] != " ":
                        return False
                    else:
                        blank += 1
            else:
                if i - col != -1:
                    if board[i][row] != word[i - col]:
                        return False
                else:
                    return False

    if blank < len(word):
        return True
    else:
        return False

def addhorizontal(board, word):
    '''
    Assumes the parameter:
    board is a 20x20 2d array,
    word is a string,
    Add the word to the grid horizontally.
    '''
    for row in range(19):
        for col in range(20 - len(word) + 1):
            if checkhorizontal(board, word, row, col):
                for i in range(col, len(word) + col):
                    board[i][row] = word[i - col]
                placed_words.append(word)
                return True
    
    unplaced_words.append(word)
    return False

def addwords(board, l):
    '''
    Assumes the parameter: board is a 20x20 2d array, l is a list of strings
    Add the strings to the grid to form a crossword.
    '''
    for i in range(len(l)):
        if i == 0:
            addFirstWord(board, l[i])
        if i != 0 and i % 2 == 0:
            addhorizontal(board, l[i])
        if i % 2 == 1:
            addvertical(board, l[i])

def add_unplaced_words(board, unplaced_words):
    '''
    Assumes the parameter: board is a 20x20 2d array, unplaced_words is a list of strings
    Iterate through the unplaced words and add them to the board (if possible)
    '''
    for word in unplaced_words:
        test = True
        for row in range(20 - len(word) + 1):
            for col in range(19):
                if checkvertical(board, word, row, col) and test:
                    for i in range(row, len(word) + row):
                        board[col][i] = word[i - row]

                    placed_words.append(word)
                    unplaced_words.remove(word)
                    test = False
                    break

        for row in range(19):
            for col in range(20 - len(word) + 1):
                if checkhorizontal(board, word, row, col) and test:
                    for i in range(col, len(word) + col):
                        board[i][row] = word[i - col]

                    placed_words.append(word)
                    unplaced_words.remove(word)
                    test = False
                    break

def crossword(l):
    '''
    Assumes the parameter l is a list of string
    Print the crossword made of these strings
    If a string cannot be added, print the word and the error message
    '''
    board = [[blank] * 20 for i in range(20)]
    addwords(board, l)
    add_unplaced_words(board, unplaced_words)

    printboard(board)

    for words in unplaced_words:
        print("no matching found: " + words)
        unplaced_words.remove(words)


crossword(l)
print(placed_words)
print(unplaced_words)
