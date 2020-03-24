# Copyright 2012 Chris KlineOC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A command-line game of tic-tac-toe written in python 3.8.

Main objects are Game for game control, Player for player moves
(including AIPlayer for computer play), and io to handle
everything related to display and input.
"""

import my_io
from ai_player import AIPlayer
from game import Game, GameTied, InvalidMove
from player import Player

# Initialize objects
game = Game(3)
players = [Player('X'), AIPlayer('O')]
playing = True
my_io.init()

# Main game loop
while playing:
    my_io.print_board(game)
    try:
        for player in players:
            player.make_move(game)
            if game.check_winner(player.symbol):
                my_io.print_board(game)
                if players.index(player) == 0:
                    my_io.winner()
                else:
                    my_io.loser()
                playing = False
                break

    except InvalidMove:
        my_io.invalid()

    except GameTied:
        my_io.print_board(game)
        my_io.game_tied()
        break

    except KeyboardInterrupt:
        my_io.game_over()
        break
