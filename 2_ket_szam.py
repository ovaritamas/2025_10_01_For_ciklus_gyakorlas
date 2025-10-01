"""
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
"""

a = int(input("Adj egy számot: "))
b = int(input("Adj még egy számot: "))

if a < b:
    for i in range(a + 1, b):
        print(i)
elif a > b:
    for q in range(a - 1, b, -1):
        print(q)