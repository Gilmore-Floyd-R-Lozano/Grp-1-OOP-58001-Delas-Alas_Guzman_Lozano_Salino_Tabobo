"""Laboratory No. 6     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
# using tabulate() fucntion
from tabulate import tabulate

data = [[1, 1, 1, ],
[2, 4, 8],
[3, 9, 27],
[4, 16, 64]]

print(tabulate(data, headers=["a", "a^2", "a^3"]))