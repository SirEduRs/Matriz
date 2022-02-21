# Copyright © 2022 by Eduardo Rodrigues. All rights reserved.
# Licensed under the GNU General Public License v3.0. See the LICENSE file.

from __future__ import annotations

from random import randint
from typing import List, TypeVar

from tabulate import tabulate

List_Matriz = List[List[int]]
T = TypeVar('T', bound='Matriz')


class Matriz:
    def __init__(self, matriz: List_Matriz = None) -> None:
        """Construtor da classe Matriz.
        
        Args:
            matriz (List[List[int]], None): A matriz que será definida.
        """
        self._matriz = matriz

    def __new__(self, matriz: List_Matriz = None) -> Matriz:
        return super().__new__(self)

    def __repr__(self) -> str:
        return (
            f"<Matriz order={Matriz.get_order(self._matriz)} " \
            f"rows={len(self._matriz)} columns={len(self._matriz[0])}>"
        )

    def __neg__(self) -> Matriz:
        """ Retorna a matriz com os elementos dentro dela negativos.

        Note:
            Caso haja elementos negativos na matriz original, os sinais deles serão trocados,
            de acordo, com a regra dos sinais na matemática.

        Returns:
            Matriz: A matriz com os elementos negativos.

        Raises:
            TypeError: Se a matriz não foi definida.
        """
        matriz = self._matriz
        matriz_z = []
        if matriz:
            for i in range(len(matriz)):
                matriz_z.append([])
                for j in range(len(matriz[i])):
                    matriz_z[i].append(-matriz[i][j])
            return Matriz(matriz=matriz_z)
        else:
            raise TypeError("A matriz não foi definida.")

    def __add__(self, other: T) -> Matriz:
        """Soma duas matrizes.

        Args:
            other (Matriz): A matriz que será somada.

        Returns:
            Matriz: A matriz resultante da soma.

        Raises:
            TypeError: Se a outra 'Matriz' não for definida.
            ValueError: Se as matrizes não possuírem a mesma ordem.
        """
        matriz = self._matriz
        matriz_z = []
        get_order = Matriz.get_order
        if isinstance(other, Matriz):
            if get_order(matriz) == get_order(other._matriz):
                for i in range(len(matriz)):
                    matriz_z.append([])
                    for j in range(len(matriz[i])):
                        matriz_z[i].append(matriz[i][j] + other._matriz[i][j])
                return Matriz(matriz=matriz_z)
            else:
                raise ValueError(
                    "As matrizes não possuem a mesma ordem. Impossível somar."
                )
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: 'Matriz' and '{other.__class__.__name__}'"
            )

    def __sub__(self, other: T) -> Matriz:
        """Subtrai duas matrizes.

        Args:
            other (Matriz): A matriz que será subtraída.

        Returns:
            Matriz: A matriz resultante da subtração.

        Raises:
            TypeError: Se a outra 'Matriz' não for definida.
            ValueError: Se as matrizes não possuírem a mesma ordem.
        """
        matriz = self._matriz
        matriz_z = []
        get_order = Matriz.get_order
        if isinstance(other, Matriz):
            if get_order(matriz) == get_order(other._matriz):
                for i in range(len(matriz)):
                    matriz_z.append([])
                    for j in range(len(matriz[i])):
                        matriz_z[i].append(matriz[i][j] - other._matriz[i][j])
                return Matriz(matriz=matriz_z)
            else:
                raise ValueError(
                    "As matrizes não possuem a mesma ordem. Impossível subtrair."
                )
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: 'Matriz' and '{other.__class__.__name__}'"
            )

    def __mul__(self, other: T | int) -> List[Matriz, str]:
        """ Multiplica duas matrizes ou um número por uma matriz.

        Args:
            other (Matriz, int): A matriz ou um número que será multiplicado.

        Returns:
            Matriz: A matriz resultante da multiplicação.

        Raises:
            TypeError: Se a outra 'Matriz' não for da classe 'Matriz' ou se o número não for inteiro.
            ValueError: Se o número de linhas da matriz 1 for diferente do número de colunas da matriz 2.
        """
        matriz = self._matriz
        matriz_z = []
        if isinstance(other, Matriz):
            if len(matriz[0]) == len(other._matriz):
                txt = ""
                for i in range(len(matriz)):
                    matriz_z.append([])
                    for j in range(len(other._matriz[0])):
                        matriz_z[i].append(0)
                        for k in range(len(matriz[i])):
                            txt += f"Z{i+1}{j+1} += {matriz[i][k]} * {other._matriz[k][j]} = {matriz[i][k] * other._matriz[k][j]}\n"
                            matriz_z[i][j] += matriz[i][k] * other._matriz[k][j]
                return [Matriz(matriz=matriz_z), txt]
            else:
                raise ValueError(
                    f"As matriz 1 tem {len(matriz[0])} colunas e a matriz 2 tem {len(other._matriz[0])} linhas. Impossível multiplicar."
                )
        elif isinstance(other, int):
            return self.multiply_matriz(other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: 'Matriz' and '{other.__class__.__name__}'"
            )

    def __rmul__(self, other: T | int) -> List[Matriz, str]:
        return self.__mul__(other)

    @classmethod
    def generate_random_matriz(cls, row: int, col: int) -> Matriz:
        """Gera uma matriz totalmente aleatória.
        
        Args:
            row (int): Número de linhas da matriz.
            col (int): Número de colunas da matriz.

        Returns:
            Matriz: Uma matriz aleatória.
        """
        matriz = []
        for i in range(row):
            matriz.append([])
            for j in range(col):
                matriz[i].append(randint(-100, 100))
        return cls(matriz=matriz)

    @staticmethod
    def get_order(matriz: List_Matriz) -> str:
        try:
            len(matriz[0])
        except TypeError as e:
            if str(e) == "object of type 'int' has no len()":
                return f"{len(matriz)}X1"
        return f"{len(matriz)}X{len(matriz[0])}"

    def show_matriz(self) -> str:
        """ Retorna uma string contendo a matriz.

        Returns:
            str: Uma string contendo a matriz.

        Raises:
            TypeError: Se a matriz não for definida.
        """
        matriz = self._matriz
        if matriz:
            return tabulate(matriz, tablefmt="fancy_grid")
        else:
            raise TypeError("A matriz não foi definida.")

    def transpose(self) -> Matriz:
        """Transpõe a matriz.
        
        Returns:
            Matriz: A matriz transposta.

        Raises:
            TypeError: Se a matriz não for definida.
        """
        matriz = self._matriz
        if matriz:
            try:
                len(matriz[0])
            except TypeError as e:
                if str(e) == "object of type 'int' has no len()":
                    return matriz
                else:
                    raise e
            new_matriz = []
            for i in range(len(matriz[0])):
                new_matriz.append([])
                for j in range(len(matriz)):
                    new_matriz[i].append(matriz[j][i])
            return Matriz(new_matriz)
        else:
            raise TypeError("A matriz não foi definida.")

    @property
    def T(self) -> Matriz:
        """Matriz: A matriz transposta."""
        return self.transpose()

    def multiply_matriz(self, num: int) -> Matriz:
        """Multiplica a mesma matriz por um determinado número.

        Args:
            num (int): O número que a matriz será multiplicada.
        
        Returns:
            Matriz: A matriz resultante da multiplicação.

        Raises:
            TypeError: Se a matriz não for definida.
        """
        matriz = self._matriz
        matriz_z = []
        if matriz:
            for i in range(len(matriz)):
                matriz_z.append([])
                for j in range(len(matriz[i])):
                    matriz_z[i].append(matriz[i][j] * num)
            return Matriz(matriz=matriz_z)
        else:
            raise TypeError("A matriz não foi definida.")