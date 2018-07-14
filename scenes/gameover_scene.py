from gameover.gameover import Gameover
import game_object
from input.input_manager import global_input_manager

class GameoverScene:
    def __init__(self):
        pass
    def setup(self):
        gameover = Gameover(640,368)
        game_object.add(gameover)


    def destroy(self):
        game_object.clear()