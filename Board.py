# -----------------------------------------------------------
# Definition of Board class that represents a board object along with it's values like current board in game,
# coordinates (x,y) of empty field, children (another board objects), parent (when current object is one of children)
# and the move that led to this board configuration from parent's state
# -----------------------------------------------------------

from copy import deepcopy


class Board:
    empty_field_coordinates = []
    board = []

    def __init__(self, start_file_name=None, board=None, parent=None, last_move=None):
        if start_file_name is not None:
            self.load_start_board(start_file_name)
            self.initial_board = deepcopy(self.board)
            self.row_count = len(self.initial_board)
            self.column_count = len(self.initial_board[0])
            self.parent = parent
            self.last_move = last_move
            self.children = []
        else:
            self.board = board
            self.row_count = len(board)
            self.column_count = len(board[0])
            self.parent = parent
            self.last_move = last_move
            self.children = []

        self.identify_empty_field_coordinates()

    def __repr__(self):
        for row in range(int(self.row_count)):
            if row != 0:
                print()
            for column in range(int(self.column_count)):
                print(self.board[row][column] + " ", end="")
        print()

        return ""

    def load_start_board(self, start_file_name):
        """
        Load the board's 2D array with the values from the given file
        """

        f = open(f"start_files/{start_file_name}", "r")
        lines = f.readlines()
        self.row_count = lines[0][0]
        self.column_count = lines[0][2]
        lines = lines[1:]
        for line in lines:
            formatted_line = line.rstrip().split()
            self.board.append(formatted_line)

    def identify_empty_field_coordinates(self):
        """
        Check at which coordinates the 0 number is in the board and save those values
        """

        self.empty_field_coordinates.clear()
        for row in range(int(self.row_count)):
            for column in range(int(self.column_count)):
                if self.board[row][column] == "0":
                    self.empty_field_coordinates.append(row)
                    self.empty_field_coordinates.append(column)

    def make_child(self, move, modified_board):
        """
        Create another board object with given modified board (by the move that has been made)
        """

        child = Board(start_file_name=None, board=modified_board, parent=self, last_move=move)
        self.children.append(child)

    def make_move(self, move):
        """
        Create temporary board 2D array from current board's array but with modifying it by making a move in
        specific direction (left, right, up, down)
        """

        self.identify_empty_field_coordinates()
        empty_field_row = self.empty_field_coordinates[0]
        empty_field_column = self.empty_field_coordinates[1]

        tmp_board = deepcopy(self.board)

        if move == 'L' or move == 'l':
            # Checking if the field on left direction exists
            if empty_field_column > 0:
                # Saving the value of field on the left of 'empty field'
                tmp_value = tmp_board[empty_field_row][empty_field_column - 1]
                # Assigning 'empty field' to the field on the left of 'empty field'
                tmp_board[empty_field_row][empty_field_column - 1] = tmp_board[empty_field_row][empty_field_column]
                # Assigning saved, previous value of field on the left to previous 'empty field' field
                tmp_board[empty_field_row][empty_field_column] = tmp_value
                # Changing the coordinates of 'empty field' field
                self.make_child(move, tmp_board)
                return True
        elif move == 'R' or move == 'r':
            # Checking if the field on right direction exists
            if empty_field_column < 3:
                # Saving the value of field on the right of 'empty field'
                tmp_value = tmp_board[empty_field_row][empty_field_column + 1]
                # Assigning 'empty field' to the field on the right of 'empty field'
                tmp_board[empty_field_row][empty_field_column + 1] = tmp_board[empty_field_row][empty_field_column]
                # Assigning saved, previous value of field on the right to previous 'empty field' field
                tmp_board[empty_field_row][empty_field_column] = tmp_value
                # Changing the coordinates of 'empty field' field
                self.make_child(move, tmp_board)
                return True
        elif move == 'U' or move == 'u':
            # Checking if the field on up direction exists
            if empty_field_row > 0:
                # Saving the value of field above 'empty field'
                tmp_value = tmp_board[empty_field_row - 1][empty_field_column]
                # Assigning 'empty field' to the field above 'empty field'
                tmp_board[empty_field_row - 1][empty_field_column] = tmp_board[empty_field_row][empty_field_column]
                # Assigning saved, previous value of field above previous 'empty field' field
                tmp_board[empty_field_row][empty_field_column] = tmp_value
                # Changing the coordinates of 'empty field' field
                self.make_child(move, tmp_board)
                return True
        elif move == 'D' or move == 'd':
            # Checking if the field on down direction exists
            if empty_field_row < 3:
                # Saving the value of field under 'empty field'
                tmp_value = tmp_board[empty_field_row + 1][empty_field_column]
                # Assigning 'empty field' to the field under 'empty field'
                tmp_board[empty_field_row + 1][empty_field_column] = tmp_board[empty_field_row][empty_field_column]
                # Assigning saved, previous value of field under previous 'empty field' field
                tmp_board[empty_field_row][empty_field_column] = tmp_value
                # Changing the coordinates of 'empty field' field
                self.make_child(move, tmp_board)
                return True

        return False
