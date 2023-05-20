from PIL import ImageGrab
import pyautogui

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 410
TOP = 158
RIGHT = 945
BOTTOM = 620

EMPTY = 0
RED = 1
BLUE = 2


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]

    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == RED:
                    print("R", end=" \t")
                elif grid[i][j] == BLUE:
                    print("B", end=" \t")
            print("\n")

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = (50, 55)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 75
                y = startCord[1] + j * 72
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        #cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][0] + LEFT,
            self._get_grid_cordinates()[column][1] + TOP,
        )

    def is_valid_move(self, column):
        return self.board[0][column] == EMPTY

    def is_game_over(self):
        # Check horizontal wins
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] != EMPTY:
                    return True

        # Check vertical wins
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] != EMPTY:
                    return True

        # Check diagonal wins (top-left to bottom-right)
        for i in range(3):
            for j in range(4):
                if self.board[i][j + 3] == self.board[i + 3][j + 3] != EMPTY:
                    return True

        # Check diagonal wins (bottom-left to top-right)
        for i in range(3, 6):
            for j in range(4):
                if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][
                    j + 3] != EMPTY:
                    return True

        # Check if board is full
        for i in range(6):
            for j in range(7):
                if self.board[i][j] == EMPTY:
                    return False

        return True

    #make evaluation function
    def evaluate(self):
        return 0

    def utility(self):
        # Count the number of possible four-in-a-row alignments for each player
        red_count = 0
        blue_count = 0

        # Check horizontal alignments
        for i in range(6):
            for j in range(4):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                    if self.board[i][j] == RED:
                        red_count += 1
                    elif self.board[i][j] == BLUE:
                        blue_count += 1

        # Check vertical alignments
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                    if self.board[i][j] == RED:
                        red_count += 1
                    elif self.board[i][j] == BLUE:
                        blue_count += 1

        # Check diagonal alignments (top-left to bottom-right)
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]:
                    if self.board[i][j] == RED:
                        red_count += 1
                    elif self.board[i][j] == BLUE:
                        blue_count += 1

        # Check diagonal alignments (bottom-left to top-right)
        for i in range(3, 6):
            for j in range(4):
                if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]:
                    if self.board[i][j] == RED:
                        red_count += 1
                    elif self.board[i][j] == BLUE:
                        blue_count += 1

        # Calculate the utility value
        return red_count - blue_count

    def copy(self):
        new_board = Board()
        new_board.board = [row.copy() for row in self.board]
        return new_board

    def get_available_moves(self):
        moves = []
        for i in range(7):
            if self.board[0][i] == EMPTY:
                moves.append(i)
        return moves



