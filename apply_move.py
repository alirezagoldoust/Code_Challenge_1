# Write applying move of user choice
# Enjoy coding! 🚀
from pprint import pprint
#player,playedspace
def apply(game_infos,gameState):
    player = game_infos[0]
    playedspace = game_infos[1]
    gameState.reverse()
    for i in range (len(gameState)):
        if gameState[i][playedspace]==0:
            if player == "p1":
                gameState[i][playedspace]= 1
            elif player == "p2":
                gameState[i][playedspace]=2
            break
    gameState.reverse()
#    print(gameState)
    return(gameState)
#array = ["p2",2]
#game = [
#    [0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0],
#    [0,0,2,0,0,0,0],
#    [0,0,2,0,0,0,0],
#]
#apply(array,game)