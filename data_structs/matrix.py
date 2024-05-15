class Matrix:
    def __init__(self):
        self.matrix: list[list[int | float]] = [[0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0],
                                                [0, 0, 0, 0, 0]]

    def resize(self, rows: int, columns: int) -> None:
        new_matrix = [[0 for column in range(columns)] for row in range(rows)]

        for i in range(min(len(self.matrix), rows)):
            for j in range(min(len(self.matrix[0]), columns)):
                new_matrix[i][j] = self.matrix[i][j]

        self.matrix = new_matrix

    def get(self) -> list[list[int | float]]:
        return self.matrix

    def get_rows(self) -> int:
        return len(self.matrix)

    def get_columns(self) -> int:
        return len(self.matrix[0])

    def get_element(self, row: int, column: int) -> int | float:
        return self.matrix[row][column]

    def set_element(self, row: int, column: int, value: int | float) -> None:
        self.matrix[row][column] = value
