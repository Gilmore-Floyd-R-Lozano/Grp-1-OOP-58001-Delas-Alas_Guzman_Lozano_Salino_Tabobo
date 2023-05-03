"""Laboratory No. 6     Group 1 - Delas Alas, Guzman, Lozano, Salino, Tabobo"""
# using loop to generate list and loop and string formatting to display table
table = [["a", "a^2", "a^3"]]
# generating list
for num in range(1, 5):
    table.extend([[str(num), str(num**2), str(num**3)]])
for row in table:
    print(' {}  {:^20}  {} '.format(*row))
