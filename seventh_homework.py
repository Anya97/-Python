#1

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res_str = ''
        for i in range(len(self.matrix)):
            res_str += str(*self.matrix[i]) + '\n'
        return f'Матрица {res_str}'

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            result.append([])
            for j in range(len(self.matrix[i])):
                n = self.matrix[i][j] + other.matrix[i][j]
                result[i].append(n)
        return Matrix(result)
    
a = Matrix([[1,2],[3,4]])
b = Matrix([[0,7],[8,3]])
print(a+b)

#2
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    coat = 0
    suit = 0
    #@abstractmethod
    #def cost_expense_coat(self):
    #    pass
    #@abstractmethod
    #def cost_expense_suit(self):
    #    pass

class Clothes(MyAbstractClass):
    #coat = 0
    #suit = 0
    def __init__(self, size, height):
        self.coat = size
        self.suit = height
    
    def cost_expense_coat(self):
        return self.coat/6.5 + 0.5
    
    def cost_expense_suit(self):
        return 2 * self.suit + 0.3
    
    @property
    def total_consumption(self):
        return ((self.coat/6.5 + 0.5) + (2 * self.suit + 0.3))

clothes = Clothes(365, 99)
print(clothes.cost_expense_coat())
print(clothes.cost_expense_suit())
print(clothes.total_consumption)

#3

class Cell:
    def __init__(self, cells_number):
        self.cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)
            
    def __sub__(self, other):
        res = self.cells_number - other.cells_number
        if res > 0:
            return Cell(res)
        else:
            raise RuntimeError ('Разность клеток < 0')
    
    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)
    
    def __truediv__(self, other):
        res_div = self.cells_number // other.cells_number
        if res_div != 0:
            return Cell(res_div)
        else:
            raise RuntimeError ('Число клеток равно 0')

    def make_order(self, number_in_row):
        return ('*'*number_in_row + '\n')*(self.cells_number // number_in_row) + '*'*(self.cells_number%number_in_row)
    
cell1 = Cell(55)
cell2 = Cell(99)
print((cell1 + cell2).cells_number)
print((cell2 - cell1).cells_number)
print((cell1 * cell2).cells_number)
print((cell2 / cell1).cells_number)
print(cell1.make_order(10))












    
