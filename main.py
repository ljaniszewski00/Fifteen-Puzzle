# SISE 2021
# LABORATORY 1 - "FIFTEEN PUZZLE"

from Board import Board
from Game import Game
import argparse

if __name__ == '__main__':
    # Parsing the arguments
    # parser = argparse.ArgumentParser(description="strategy, strategy_method, start_file, solution_file, "
    #                                              "additional_file.")
    # parser.add_argument('strategy')
    # parser.add_argument('strategy_method')
    # parser.add_argument('start_file')
    # parser.add_argument('solution_file')
    # parser.add_argument('additional_file')
    # args = parser.parse_args()
    #
    # for argument in args.strategy_method:
    #     strategy_method.append(argument)

    # Creating the BOARD object along with reading the lines from input file and settings coordinates of empty fields
    # board = Board(args.start_file)
    board = Board("4x4_01_0001.txt")
    print(board)
    print("Empty fields coordinates:", board.empty_field_coordinates)
    # Creating the GAME object along with starting the game itself
    # game = Game(args.strategy, args.strategy_method, args.solution_file, args.additional_file, board)

    # Wait until user presses key
    # input("Press Enter to continue...")
