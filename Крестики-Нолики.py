field = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

player = "X"


def print_field(): # игровое поле
    print("  0 1 2")
    for i in range(3):
        print(i, *field[i])
    print()


def check_winner(): # проверка победителя
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != "-":
            return field[i][0]
        if field[0][i] == field[1][i] == field[2][i] != "-":
            return field[0][i]

    if field[0][0] == field[1][1] == field[2][2] != "-":
        return field[0][0]
    if field[0][2] == field[1][1] == field[2][0] != "-":
        return field[0][2]

    return None


def is_draw(): # проверка на ничью
    for row in field:
        if "-" in row:
            return False
    return True


print("Крестики-нолики\n")
print("Пример написание (0 2)")

while True: # игровой цикл
    print_field()

    row, col = map(int, input(f"Ход игрока {player}: ").split())

    if field[row][col] != "-":
        print("Клетка занята!\n")
        continue

    field[row][col] = player

    winner = check_winner()
    if winner:
        print_field()
        print("Победил игрок", winner)
        break

    if is_draw():
        print_field()
        print("Ничья")
        break

    player = "O" if player == "X" else "X" # смена игрока
