from pprint import pprint


def apply(game_infos, gameState):
    player = game_infos[0]
    playedspace = game_infos[1]
    gameState.reverse()
    for i in range(len(gameState)):
        if gameState[i][playedspace] == 0:
            if player == "p1":
                gameState[i][playedspace] = -1
            elif player == "p2":
                gameState[i][playedspace] = 1
            break
    gameState.reverse()
    return gameState


board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


pprint(apply(["p1", 3], board))
