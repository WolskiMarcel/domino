import random

def create_domino_set():
    domino_set = [[a, b] for b in range(7) for a in range(7) if a <= b]
    while True:
        random.shuffle(domino_set)
        stock_pieces = domino_set[0:14]
        computers_hand = domino_set[14:21]
        players_hand = domino_set[21:28]

        max_double = max(max(computers_hand), max(players_hand))
        if max_double[0] == max_double[1]:
            break
    return stock_pieces, computers_hand, players_hand, max_double

def turn(computers_hand, players_hand,max_double):
    if max_double in computers_hand:
        computers_hand.remove(max_double)
        status = "player"
    else:
        players_hand.remove(max_double)
        status = "computer"
    domino_snake = []
    domino_snake.append(max_double)
    return status, domino_snake


def make_move(status, move, domino_snake, hand, stock_pieces):
    abs_move = abs(move)
    i_move = abs_move - 1
    if abs_move in range(1, len(hand)+1):
        if 0 < move:
            domino_snake.append(hand.pop(i_move))
        elif move < 0:
            domino_snake.insert(0, hand.pop(i_move))
    elif move == 0:
        extra_piece = take_extra(stock_pieces)
        if extra_piece is not None:
            hand.append(extra_piece)
    else:
        print("Invalid input. Please try again.")

    status = "player" if status == "computer" else "computer"
    return status

def take_extra(stock_pieces):
    if stock_pieces:
        return stock_pieces.pop()
    else:
        return None

def get_valid_input(hand):
    while True:
        try:
            v_move = int(input())
            abs_move = abs(v_move)
            if abs_move in range(1, len(hand)+1):
                return v_move
            elif v_move == 0:
                return v_move
            else:
                print("Invalid input. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please try again.")
def game():
    stock_pieces, computers_hand, players_hand, max_double = create_domino_set()
    status, domino_snake = turn(computers_hand, players_hand, max_double)
    while True:
        print("="*70)
        print("Stock size:", len(stock_pieces))
        print("Computer pieces:", len(computers_hand))
        print("")
        print(*domino_snake if len(domino_snake) <= 6 else (*domino_snake[:3], "...", *domino_snake[-3:]), sep=" ")
        print("")
        print("Your pieces:")
        print(*[f'{i + 1}:{e}' for i, e in enumerate(players_hand)], sep='\n')
        print("")

        if len(players_hand) == 0:
            print(f"Status: The game is over. You won!")
            break
        elif len(computers_hand) == 0:
            print(f"Status: The game is over. The computer won!")
            break
        elif status == "player":
            print("Status: It's your turn to make a move. Enter your command.")
            move_player = get_valid_input(players_hand)
            status = make_move(status,move_player, domino_snake,players_hand,stock_pieces)
        elif status == "computer":
            comp = input("Status: Computer is about to make a move. Press Enter to continue...\n")
            move_computer = random.choice(range(-len(computers_hand),len(computers_hand)))
            status = make_move(status,move_computer, domino_snake, computers_hand,stock_pieces)

def main():
    game()

if __name__ == "__main__":
    main()