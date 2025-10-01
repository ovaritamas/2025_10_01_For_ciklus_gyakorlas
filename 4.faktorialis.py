"""
Számold ki egy adott szám faktoriálisát! A számot a felhasználótól kérd be!
"""
szam = int(input("Adj egy egész számot: "))
y = 1

for i in range(1, szam+1):
    y *= i

print(f"A szám faktoriálisa:{y}")