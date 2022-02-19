from __future__ import annotations

from typing import List

class Matriz(object):
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
            raise TypeError("Não é possivel somar com um tipo diferente de matriz")

    @staticmethod
    def create_matriz_generic(rows: int, cols: int, name: str) -> List[List[int]]:
        matriz = []
        for i in range(rows):
            matriz.append([])
            for j in range(cols):
                matriz[i].append(f"{name}{i+1}{j+1}")
        return matriz

    def show_matriz(self, matriz: List[List[int]]) -> str:
        txt = ""
        try:
            len(matriz[0])
        except TypeError as e:
            if str(e) == "object of type 'int' has no len()":
                for i in range(len(matriz)):
                    txt += f"{matriz[i]}\n"
                return txt
            else:
                raise e
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                txt += str(matriz[i][j]) + " "
            txt += "\n"
        return txt

    @staticmethod
    def get_column(matriz: List[List[int]], col: int) -> List[List[int]]:
        column = []
        for i in range(len(matriz)):
            column.append(matriz[i][col - 1])
        return column

    @staticmethod
    def get_row(matriz: List[List[int]], row: int) -> List[List[int]]:
        return matriz[row - 1]

    def check_to_multiply(self, matriz_x, matriz_y) -> bool:
        if len(matriz_x[0]) == len(matriz_y):
            return True
        else:
            return False

    def check_to_sum(self, matriz_x, matriz_y) -> bool:
        if self.get_order(matriz_x) == self.get_order(matriz_y):
            return True
        else:
            return False

    def sum(self, matriz_x: List[List[int]], matriz_y: List[List[int]]):
        if self.check_to_sum(matriz_x, matriz_y):
            matriz_z = []
            for i in range(len(matriz_x)):
                matriz_z.append([])
                for j in range(len(matriz_x[0])):
                    matriz_z[i].append(matriz_x[i][j] + matriz_y[i][j])
            return Matriz(matriz_z)
        else:
            return "Não é possivel somar, por causa das ordens das matrizes diferentes"

    def subtract(
        self, matriz_x: List[List[int]], matriz_y: List[List[int]]
    ) -> List[List[int]]:
        if self.check_to_sum(matriz_x, matriz_y):
            matriz_z = []
            for i in range(len(matriz_x)):
                matriz_z.append([])
                for j in range(len(matriz_x[0])):
                    matriz_z[i].append(matriz_x[i][j] - matriz_y[i][j])
            return matriz_z
        else:
            return (
                "Não é possivel subtrair, por causa das ordens das matrizes diferentes"
            )

    def multiply_matriz(self, matriz: List[List[int]] = None, num: int = 1) -> List[List[int]]:
        matriz_z = []
        matriz = matriz or self.matriz
        for i in range(len(matriz)):
            matriz_z.append([])
            for j in range(len(matriz[i])):
                matriz_z[i].append(matriz[i][j] * num)
        return matriz_z

    @staticmethod
    def get_matriz_transpose(matriz: List[List[int]]) -> List[List[int]]:
        matriz_transpose = []
        for i in range(len(matriz[0])):
            matriz_transpose.append([])
            for j in range(len(matriz)):
                matriz_transpose[i].append(matriz[j][i])
        return matriz_transpose

    def multiply(
        self, matriz_x: List[List[int]], matriz_y: List[List[int]]
    ) -> List[List[int]]:
        if self.check_to_multiply(matriz_x, matriz_y):
            matriz_z = []
            txt = ""
            for i in range(len(matriz_x)):
                matriz_z.append([])
                for j in range(len(matriz_y[0])):
                    matriz_z[i].append(0)
                    for k in range(len(matriz_y)):
                        txt += f"Z{i+1}{j+1} += {matriz_x[i][k]} * {matriz_y[k][j]} = {matriz_x[i][k] * matriz_y[k][j]}\n"
                        matriz_z[i][j] += matriz_x[i][k] * matriz_y[k][j]
            return matriz_z, txt
        else:
            return None

    def get_order(self, matriz: List[List[int]]) -> int:
        try:
            len(matriz[0])
        except TypeError as e:
            if str(e) == "object of type 'int' has no len()":
                return f"{len(matriz)} x 1"
        return f"{len(matriz)} x {len(matriz[0])}"

    def get_element(self, matriz: List[List[int]], row: int, col: int) -> int:
        return matriz[row - 1][col - 1]
        