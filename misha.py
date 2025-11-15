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
