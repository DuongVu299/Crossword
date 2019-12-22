board_size = input("How big do you want the grid? ")
while not board_size.isdigit():
    board_size = input("Grid size must be an integer, enter grid size again: ")
board_size = int(board_size)

blank = " "
board = [[blank] * board_size for i in range(board_size)]  # Create a grid size board_size x board_size

num_words = input("How many words to make crossword: ")
while not num_words.isdigit():
    num_words = input("Word number must be an integer, enter word number again: ")
num_words = int(num_words)

words = []

for i in range(num_words):
    words.append(input("Enter word %s: " % (i + 1)))

placed_words = []  # Create a list of placed and unplaced words on the grid
unplaced_words = []


def print_board():
    """
    Assumes the parameter board is a 2 dimensional array,
    Print every element of that array into a grid.
    """
    for y in range(-2, board_size + 2):
        for x in range(-1, board_size + 1):
            if y == -2 or y == board_size + 1:
                if x == -1 or x == board_size:
                    print(" ", end=" ")
                else:
                    print(x % 10, end=" ")
            elif y == -1 or y == board_size:
                if x == -1 or x == board_size:
                    print(" ", end=" ")
                else:
                    print("_", end=" ")
            else:
                if x == -1:
                    print("|", end=" ")
                elif x == board_size:
                    print("|", end=str(y))
                else:
                    print(board[x][y], end=" ")
        print("")


def add_first_word(word):
    """
    Assumes the parameter: board is a 2d array, word is a string.
    Add the word to the center of the grid.
    """
    col = board_size // 2 - len(word) // 2
    row = board_size // 2

    for x in range(col, len(word) + col):
        board[x][row] = word[x - col]
    placed_words.append(word)


def check_vertical(word, row, col):
    """
    Assumes the parameter:
    board is a 2d array,
    word is a string,
    row and col are 2 integers.
    Check if the word can be added to the board vertically at the given row and column.
    """
    blank_num = 0
    if len(word) + row > board_size:
        return False

    if row < board_size - len(word):
        if board[col][row + len(word)] != " ":
            return False
    if row > 0:
        if board[col][row - 1] != " ":
            return False

    for i in range(row, len(word) + row):
        if i >= board_size:
            return False
        else:
            if board[col][i] == " ":
                if col == 0:
                    if board[col + 1][i] != " ":
                        return False
                if col == board_size - 1:
                    if board[col - 1][i] != " ":
                        return False
                else:
                    if board[col + 1][i] != " " or board[col - 1][i] != " ":
                        return False
                    else:
                        blank_num += 1
            else:
                if i - row != -1:
                    if board[col][i] != word[i - row]:
                        return False
                else:
                    return False

    if blank_num < len(word):
        return True
    else:
        return False


def add_vertical(word):
    """
    Assumes the parameter:
    board is a 2d array,
    word is a string,
    Add the word to the grid vertically.
    """
    for col in range(board_size - 1):
        for row in range(board_size - len(word) + 1):
            if check_vertical(word, row, col):
                for i in range(row, len(word) + row):
                    board[col][i] = word[i - row]
                placed_words.append(word)
                return True

    unplaced_words.append(word)
    return False


def check_horizontal(word, row, col):
    """
    Assumes the parameter:
    board is a 2d array,
    word is a string,
    row and col are 2 integers.
    Check if the word can be added to the board horizontally at the given row and column.
    """
    blank_num = 0
    if len(word) + col > board_size:
        return False

    if col < board_size - len(word):
        if board[col + len(word)][row] != " ":
            return False
    if col > 0:
        if board[col - 1][row] != " ":
            return False

    for i in range(col, len(word) + col):
        if i >= board_size:
            return False
        else:
            if board[i][row] == " ":
                if row == 0:
                    if board[i][row + 1] != " ":
                        return False
                if row == board_size - 1:
                    if board[i][row - 1] != " ":
                        return False
                else:
                    if board[i][row + 1] != " " or board[i][row - 1] != " ":
                        return False
                    else:
                        blank_num += 1
            else:
                if i - col != -1:
                    if board[i][row] != word[i - col]:
                        return False
                else:
                    return False

    if blank_num < len(word):
        return True
    else:
        return False


def add_horizontal(word):
    """
    Assumes the parameter:
    board is a 2d array,
    word is a string,
    Add the word to the grid horizontally.
    """
    for row in range(board_size - 1):
        for col in range(board_size - len(word) + 1):
            if check_horizontal(word, row, col):
                for i in range(col, len(word) + col):
                    board[i][row] = word[i - col]
                placed_words.append(word)
                return True

    unplaced_words.append(word)
    return False


def add_words():
    """
    Assumes the parameter: board is a 2d array, l is a list of strings
    Add the strings to the grid to form a crossword.
    """
    for i in range(len(words)):
        if i == 0:
            add_first_word(words[i])
        if i != 0 and i % 2 == 0:
            add_horizontal(words[i])
        if i % 2 == 1:
            add_vertical(words[i])


def add_unplaced_words():
    """
    Assumes the parameter: board is a 2d array, unplaced_words is a list of strings
    Iterate through the unplaced words and add them to the board (if possible)
    """
    for word in unplaced_words:
        test = True
        for row in range(board_size - len(word) + 1):
            for col in range(board_size - 1):
                if check_vertical(word, row, col) and test:
                    for i in range(row, len(word) + row):
                        board[col][i] = word[i - row]

                    placed_words.append(word)
                    unplaced_words.remove(word)
                    test = False
                    break

        for row in range(board_size - 1):
            for col in range(board_size - len(word) + 1):
                if check_horizontal(word, row, col) and test:
                    for i in range(col, len(word) + col):
                        board[i][row] = word[i - col]

                    placed_words.append(word)
                    unplaced_words.remove(word)
                    test = False
                    break


def crossword():
    """
    Assumes the parameter l is a list of string
    Print the crossword made of these strings
    If a string cannot be added, print the word and the error message
    """
    add_words()
    add_unplaced_words()

    print_board()

    for word in unplaced_words:
        print("no matching found: " + word)
        unplaced_words.remove(word)


crossword()
input("")
