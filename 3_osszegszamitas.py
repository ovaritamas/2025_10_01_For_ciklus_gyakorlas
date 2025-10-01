"""
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""
jelszo = "tiktok1234"
felhasznalo_jelszo = input("Kérem a jelszót: ")

while jelszo != felhasznalo_jelszo:
    felhasznalo_jelszo = input("Kérem a jelszót: ")
else:
    print("Helyes!")