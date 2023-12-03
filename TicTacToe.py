#● Контекст
#Вероятнее всего, вы с детства знакомы с этой игрой.Пришло
#время реализовать её. Два игрока по очереди ставят крестики
#и нолики на игровое поле. Игра завершается когда кто-то
#победил, либо наступила ничья, либо игроки отказались
#играть.
#● Задача
#Написать игру в “Крестики-нолики”. Можете использовать
#любые парадигмы, которые посчитаете наиболее
#подходящими. Можете реализовать доску как угодно - как
#одномерный массив или двумерный массив (массив массивов).
#Можете использовать как правила, так и хардкод, на своё
#усмотрение. Главное, чтобы в игру можно было поиграть через
#терминал с вашего компьютера.

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Проверка по горизонтали и вертикали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Проверка на ничью
    is_full = all([cell != " " for row in board for cell in row])
    if is_full:
        return "Ничья"

    return None

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")
        row = int(input("Введите номер строки (0-2): "))
        col = int(input("Введите номер столбца (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Игрок {winner} победил!")
                break
            elif winner == "Ничья":
                print_board(board)
                print("Ничья!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Выбранная ячейка уже занята. Попробуйте еще раз.")


play_game()