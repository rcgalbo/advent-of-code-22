def split_lines(dat: str) -> list[list[str]]:
    throws = dat.split('\n')
    throws = [throw.strip() for throw in throws]
    throws = [throw.split(' ') for throw in throws]
    throws = [throw for throw in throws if throw[0] != '']
    return throws

def find_game_state(opp: str, player: str) -> str:
    game_state = ''
    if player == 'X':
        if opp == 'A':
            game_state = 'Tie'
        elif opp == 'B':
            game_state = 'Loss'
        elif opp == 'C':
            game_state = 'Win'
    elif player == 'Y':
        if opp == 'A':
            game_state = 'Win'
        elif opp == 'B':
            game_state = 'Tie'
        elif opp == 'C':
            game_state = 'Loss'
    elif player == 'Z':
        if opp == 'A':
            game_state = 'Loss'
        elif opp == 'B':
            game_state = 'Win'
        elif opp == 'C':
            game_state = 'Tie'
    return game_state            

def score_throw(throw: list[str]) -> int:
    opp, player = throw
    score = 0
    score_dict = {
            'A': 1, 'X': 1,
            'B': 2, 'Y': 2,
            'C': 3, 'Z': 3      
    }
    game_state = find_game_state(opp, player)
    if game_state == 'Loss':
        score += score_dict[player]
    if game_state == 'Tie':
        score += 3 + score_dict[player]
    if game_state == 'Win':
        score += 6 + score_dict[player]
    return score

def score_game(throws: list[list[str]]) -> int:
    score = sum([score_throw(throw) for throw in throws])
    return score

def find_right_move(opp: str, decision: str) -> str:
    right_move = ''
    if opp == 'A':
        if decision == 'X':
            right_move = 'Z'
        elif decision == 'Y':
            right_move = 'X'
        elif decision == 'Z':
            right_move = 'Y'
    elif opp == 'B':
        if decision == 'X':
            right_move = 'X'
        elif decision == 'Y':
            right_move = 'Y'
        elif decision == 'Z':
            right_move = 'Z'
    elif opp == 'C':
        if decision == 'X':
            right_move = 'Y'
        elif decision == 'Y':
            right_move = 'Z'
        elif decision == 'Z':
            right_move = 'X'
    return right_move      
    
def score_game_part2(throws: list[list[str]]) -> int:
    # convert opp, direction to scorable sheet
    converted_throws = []
    for throw in throws:
        opp, decision = throw
        player = find_right_move(opp,decision)
        converted_throws.append([opp, player])
    return score_game(converted_throws)


if __name__ == '__main__':
    with open('data/day2.txt') as dat:
        f = dat.read()
    throws = split_lines(f)
    print(score_game(throws))

    print(score_game_part2(throws))