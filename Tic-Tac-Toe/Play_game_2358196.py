from noughtsandcrosses_2358196 import *
    
def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    welcome(board)
    total_score = 0
    score = 0  # It defines the score variable
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            print(f'Your scored {score} this game:')
        if choice == '2':
            save_score(score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return
    
if __name__ == '__main__':
    main()
