"""
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""

szam = int(input("Adj egy egész számot, és és kiszámolom egytől a számok összegét: "))
y = 0


for i in range(1, szam):
    y += i
    #print(i)

print(f"A számok öszzege:{y}")