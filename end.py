def print_board(board):
    cells = [c if c != " " else str(i+1) for i, c in enumerate(board)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}\n")
def check_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    return all(c != " " for c in board)
def get_move(player, board):
    while True:
        try:
            pos = int(input(f"Ход игрока {player} (1-9): "))
        except ValueError:
            print("Введите число от 1 до 9.")
            continue
        if not 1 <= pos <= 9:
            print("Позиция вне диапазона. Попробуйте снова.")
            continue
        idx = pos - 1
        if board[idx] != " ":
            print("Клетка занята. Выберите другую.")
            continue
        return idx
def tic_tac_toe():
    board = [" "] * 9
    player = "X"
    print("Крестики-нолики. Игроки: X и O. Пустые клетки отмечены номерами 1–9.")
    print_board(board)
    while True:
        move = get_move(player, board)
        board[move] = player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Победа игрока {winner}!")
            break
        if is_draw(board):
            print("Ничья.")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
