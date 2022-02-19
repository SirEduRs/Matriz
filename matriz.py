from __future__ import annotations

from typing import List


class Matriz:
    def __init__(self, matriz: List[List[int]] = None):
        self.matriz = matriz

    def __repr__(self) -> str:
        return f"<Matriz order='{self.get_order(self.matriz)}'>"

    def __str__(self) -> str:
        return self.show_matriz(self.matriz)

    def __add__(self, other) -> Matriz:
        if isinstance(other, Matriz):
            return self.sum(self.matriz, other.matriz)
        else:
            raise TypeError(
                "Não é possivel somar com um tipo diferente de matriz"
            )

    @staticmethod
    def create_matriz_generic(rows: int, cols: int, name: str) -> Matriz:
        matriz = []
        for i in range(rows):
            matriz.append([])
            for j in range(cols):
                matriz[i].append(f"{name}{i+1}{j+1}")
        return matriz

    def show_matriz(self) -> str:
        txt = ""
        try:
            len(self.matriz[0])
        except TypeError as e:
            if str(e) == "object of type 'int' has no len()":
                for i in range(len(self.matriz)):
                    txt += f"{self.matriz[i]}\n"
                return txt
            else:
                raise e
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                txt += str(self.matriz[i][j]) + " "
            txt += "\n"
        return txt

    def get_column(self, col: int) -> List[List[int]]:
        column = []
        for i in range(len(self.matriz)):
            column.append(self.matriz[i][col - 1])
        return column

    def get_row(self, row: int) -> List[List[int]]:
        return self.matriz[row - 1]

    def check_to_multiply(self, matriz_y) -> bool:
        if len(self.matriz[0]) == len(matriz_y):
            return True
        else:
            return False

    def check_to_sum(self, matriz_y) -> bool:
        if self.get_order(self.matriz) == self.get_order(matriz_y):
            return True
        else:
            return False

    def sum(self, matriz_y: List[List[int]]):
        if self.check_to_sum(self.matriz, matriz_y):
            matriz_z = []
            for i in range(len(self.matriz)):
                matriz_z.append([])
                for j in range(len(self.matriz[0])):
                    matriz_z[i].append(self.matriz[i][j] + matriz_y[i][j])
            return Matriz(matriz_z)
        else:
            return "Não é possivel somar, por causa das ordens das matrizes diferentes"

    def subtract(self, matriz_y: List[List[int]]) -> List[List[int]]:
        if self.check_to_sum(self.matriz, matriz_y):
            matriz_z = []
            for i in range(len(self.matriz)):
                matriz_z.append([])
                for j in range(len(self.matriz[0])):
                    matriz_z[i].append(self.matriz[i][j] - matriz_y[i][j])
            return matriz_z
        else:
            return (
                "Não é possivel subtrair, por causa das ordens das matrizes diferentes"
            )

    def multiply_matriz(self, num: int):
        matriz_z = []
        for i in range(len(self.matriz)):
            matriz_z.append([])
            for j in range(len(self.matriz[i])):
                matriz_z[i].append(self.matriz[i][j] * num)
        return matriz_z

    def get_matriz_transpose(self):
        matriz_transpose = []
        for i in range(len(self.matriz[0])):
            matriz_transpose.append([])
            for j in range(len(self.matriz)):
                matriz_transpose[i].append(self.matriz[j][i])
        return matriz_transpose

    def multiply(self, matriz_y: List[List[int]]) -> List[List[int]]:
        if self.check_to_multiply(self.matriz, matriz_y):
            matriz_z = []
            txt = ""
            for i in range(len(self.matriz)):
                matriz_z.append([])
                for j in range(len(matriz_y[0])):
                    matriz_z[i].append(0)
                    for k in range(len(matriz_y)):
                        txt += f"Z{i+1}{j+1} += {self.matriz[i][k]} * {matriz_y[k][j]} = {self.matriz[i][k] * matriz_y[k][j]}\n"
                        matriz_z[i][j] += self.matriz[i][k] * matriz_y[k][j]
            return matriz_z, txt
        else:
            return None

    def get_order(self) -> int:
        try:
            len(self.matriz[0])
        except TypeError as e:
            if str(e) == "object of type 'int' has no len()":
                return f"{len(self.matriz)} x 1"
        return f"{len(self.matriz)} x {len(self.matriz[0])}"

    def get_element(self, row: int, col: int) -> int:
        return self.matriz[row - 1][col - 1]
