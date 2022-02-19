from __future__ import annotations

from typing import List, Iterable

List_Matriz = List[List[int]]

class Matriz:
    def __init__(self, matriz: List_Matriz = None):
        self.matriz = matriz
        self.matriz_x: List_Matriz = []

    def __repr__(self) -> str:
        return f"<Matriz order='{self.get_order(self.matriz)}'>"

    def __str__(self) -> str:
        return self.show_matriz()

    def __add__(self, other) -> Matriz:
        if isinstance(other, Matriz):
            soma = self.sum(self.matriz, other.matriz)
            return Matriz(soma)
        else:
            raise TypeError("Não é possivel somar, por causa do tipo das matrizes diferentes")

    def __sub__(self, other) -> Matriz:
        if isinstance(other, Matriz):
            sub = self.subtract(self.matriz, other.matriz)
            return Matriz(sub)
        else:
            raise TypeError("Não é possivel subtrair, por causa do tipo das matrizes diferentes")

    def __mul__(self, other) -> Matriz:
        if isinstance(other, Matriz):
            multi = self.multiply(self.matriz, other.matriz)
            return [Matriz(multi[0]), multi[1]]
        else:
            raise TypeError("Não é possivel multiplicar, por causa do tipo das matrizes diferentes")

    @classmethod
    def create_matriz_generic(cls, rows: int, cols: int, name: str, show: bool = False):
        matriz = []
        for i in range(rows):
            matriz.append([])
            for j in range(cols):
                if show:
                    matriz[i].append(f"{name}{i+1}{j+1}")
                else:
                    matriz[i].append(f"{i+1}{j+1}")
        return cls(matriz)


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

    def get_column(self, col: int) -> List_Matriz:
        column = []
        for i in range(len(self.matriz)):
            column.append(self.matriz[i][col - 1])
        return column

    def get_row(self, row: int) -> List_Matriz:
        return self.matriz[row - 1]

    def check_to_multiply(self, matriz_x: List_Matriz, matriz_y: List_Matriz) -> bool:
        if len(matriz_x[0]) == len(matriz_y):
            return True
        else:
            return False

    def check_to_sum(self, matriz_x: List_Matriz, matriz_y: List_Matriz) -> bool:
        if self.get_order(matriz_x) == self.get_order(matriz_y):
            return True
        else:
            return False

    def sum(self, matriz_x: List_Matriz, matriz_y: List_Matriz) -> Matriz:
        if self.check_to_sum(matriz_x, matriz_y):
            matriz_z = list()
            for i in range(len(matriz_x)):
                matriz_z.append([])
                for j in range(len(matriz_x)):
                    matriz_z[i].append(matriz_x[i][j] + matriz_y[i][j])
            return matriz_z
        else:
            return "Não é possivel somar, por causa das ordens das matrizes diferentes"

    def subtract(self, matriz_x: List_Matriz, matriz_y: List_Matriz) -> Matriz:
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

    def multiply_matriz(self, num: int) -> Matriz:
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

    @property
    def T(self):
        return self.get_matriz_transpose()

    def multiply(self, matriz_x: List_Matriz, matriz_y: List_Matriz) -> Iterable[Matriz | str]:
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
            return [matriz_z, txt]
        else:
            return None

    @staticmethod
    def get_order(matriz: Matriz) -> str:
        try:
            len(matriz[0])
        except TypeError as e:
            if str(e) == "object of type 'int' has no len()":
                return f"{len(matriz)} x 1"
        return f"{len(matriz)} x {len(matriz[0])}"

    def get_element(self, row: int, col: int) -> int:
        return self.matriz[row - 1][col - 1]
