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