"""Laboratory No. 6     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
# using loop and string formatting
table = [["a", "a^2", "a^3"],
[1, 1, 1],
[2, 4, 8],
[3, 9, 27],
[4, 16, 64]]
for row in table:
    print(' {}  {:^20}  {} '.format(*row))