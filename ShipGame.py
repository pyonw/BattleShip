# Author: Woo Pyon
# GitHub username: pyonw
# Date: 02/23/22
# Description: Create a game that allows two people to play Battleship
#              Each player has their own 10x10 grid to place their ships on
#              Take turns firing torpedo at a square on the enemy's grid. Ship is sunk when all squares are hit
#              When a player sinks their opponent's final ship, they win

class ShipGame:
    def __init__(self):
        arr = []
        for i in range(10):
            col = []
            for j in range(10):
                col.append(' ')
            arr.append(col)
        arr_2 = []
        for a in range(10):
            col_2 = []
            for b in range(10):
                col_2.append(' ')
            arr_2.append(col_2)
        self.board_first = arr
        self.board_second = arr_2
        self.state = "UNFINISHED"
        self.ship_list_1 = []
        self.ship_list_2 = []
        self.turn ='first'

    def get_current_state(self):
        return self.state

    def place_ship(self, player, length, coordinates, orientation):
        """Allows player(P1 or P2) to place ships correctly in their grid"""
        letter_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        coord = int(coordinates[1])
        if len(coordinates) == 3:
            coord = int(coordinates[1] + coordinates[2])
            #to read double digit numbers like 10
        if coord > 10:
            return False
        if not coordinates[0] in letter_dict:
            return False
        if length < 2:
            return False
        #the arguments above test if the ships can be placed properly. If it overlaps it'll return false
        #If the ships length is less than 2 it'll return false
        #If its out of the coordinates range returns false
        temp_ship = []
        if(player == "first"):
            if self.board_first[letter_dict[coordinates[0]]][coord - 1] == 'x':
                return False
            if(orientation == "C"):
                if length + letter_dict[coordinates[0]] > 10:
                    return False
                for i in range(length):
                    temp_ship.append((letter_dict[coordinates[0]]+i, coord-1))
                    self.board_first[letter_dict[coordinates[0]]+i][coord-1] = 'x'
                self.ship_list_1.append(temp_ship)
            if(orientation == "R"):
                if length + coord - 1 > 10:
                    return False
                for i in range(length):
                    temp_ship.append((letter_dict[coordinates[0]], coord - 1 + i))
                    self.board_first[letter_dict[coordinates[0]]][coord-1+i] = 'x'
                self.ship_list_1.append(temp_ship)
        elif(player == "second"):
            if self.board_second[letter_dict[coordinates[0]]][coord - 1] == 'x':
                return False
            if (orientation == "C"):
                if length + letter_dict[coordinates[0]] > 10:
                    return False
                for i in range(length):
                    temp_ship.append((letter_dict[coordinates[0]] + i, coord - 1))
                    self.board_second[letter_dict[coordinates[0]] + i][coord - 1] = 'x'
                self.ship_list_2.append(temp_ship)
            if (orientation == "R"):
                if length + coord - 1 > 10:
                    return False
                for i in range(length):
                    temp_ship.append((letter_dict[coordinates[0]], coord - 1 + i))
                    self.board_second[letter_dict[coordinates[0]]][coord - 1 + i] = 'x'
                self.ship_list_2.append(temp_ship)
        return True

    def fire_torpedo(self, player, coordinates):
        """Each player takes turns firing a torpedo,
        picking a coordinate on the opponent's grid"""
        letter_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        coord = int(coordinates[1])
        if len(coordinates) == 3:
            coord = int(coordinates[1] + coordinates[2])
        if coord > 10:
            return False
        if not coordinates[0] in letter_dict:
            return False
        if self.get_current_state() in ("FIRST_PLAYER_WON", "SECOND_PLAYER_WON"):
            return False
        if self.get_current_state() == "UNFINISHED":
            if (player == "first"):
                if self.turn == 'second':
                    return False
                if self.board_second[letter_dict[coordinates[0]]][coord - 1] == 'x':
                    self.board_second[letter_dict[coordinates[0]]][coord - 1] = 'o'
                self.turn = 'second'
                for i in self.ship_list_2:
                    counter = 0
                    for j in i:
                        if (self.board_second[j[0]][j[1]] == 'o'):
                            counter += 1
                    if (counter == len(i)):
                        self.ship_list_2.remove(i)
                    if (len(self.ship_list_2) == 0):
                        self.state = "FIRST_PLAYER_WON"

            if (player == "second"):
                if self.turn == 'first':
                    return False
                if self.board_first[letter_dict[coordinates[0]]][coord - 1] == 'x':
                    self.board_first[letter_dict[coordinates[0]]][coord - 1] = 'o'
                self.turn = 'first'
                for i in self.ship_list_1:
                    counter = 0
                    for j in i:
                        if (self.board_first[j[0]][j[1]] == 'o'):
                            counter += 1
                    if (counter == len(i)):
                        self.ship_list_1.remove(i)
                if (len(self.ship_list_1) == 0):
                    self.state = "SECOND_PLAYER_WON"
        return True


    def get_num_ships_remaining(self, player):
        """How many ships each players have left"""
        if (player == "first"):
            return len(self.ship_list_1)
        if (player == "second"):
            return len(self.ship_list_2)

game = ShipGame()
game.place_ship('first', 5, 'A1', 'C')
game.place_ship('second', 5, 'A1', 'R')
game.place_ship('first', 5, 'A1', 'R')
print(game.board_first)
print(game.get_current_state())

