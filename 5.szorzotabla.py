"""
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""

x = int(input("Adje egy számot(1-10): "))
y = 1

for i in range(1, 11):
    print(f"{i} * {y} = {i * y }")

