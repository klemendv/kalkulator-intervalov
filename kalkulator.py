def kalkulator_intervalov():
    print("Kalkulator intervalov")
    print("Izberite eno od možnosti:")
    print("1. Unija intervalov")
    print("2. Presek intervalov")
    print("3. Razlika intervalov")
    print("4. Izhod")

    izbira = input("Vaša izbira (1/2/3/4): ")

    if izbira == "1":
        interval1 = vnesi_interval("Vnesite prvi interval: ")
        interval2 = vnesi_interval("Vnesite drugi interval: ")
        unija = zdruzi_intervala(interval1, interval2)
        print(f"Unija intervalov: {unija}")
    elif izbira == "2":
        interval1 = vnesi_interval("Vnesite prvi interval: ")
        interval2 = vnesi_interval("Vnesite drugi interval: ")
        presek = presek_intervalov(interval1, interval2)
        print(f"Presek intervalov: {presek}")
    elif izbira == "3":
        interval1 = vnesi_interval("Vnesite prvi interval: ")
        interval2 = vnesi_interval("Vnesite drugi interval: ")
        razlika = razlika_intervalov(interval1, interval2)
        print(f"Razlika intervalov: {razlika}")
    elif izbira == "4":
        return
    else:
        print("Neveljavna izbira. Prosimo, izberite 1, 2, 3 ali 4.")

    kalkulator_intervalov()

def vnesi_interval(prompt):
    try:
        vnos = input(prompt)
        spodnja_meja, zgornja_meja = map(float, vnos.split())
        return (spodnja_meja, zgornja_meja)
    except ValueError:
        print("Napaka: Vnesite interval v obliki 'spodnja_meja zgornja_meja'.")
        return vnesi_interval(prompt)

def zdruzi_intervala(interval1, interval2):
    spodnja_meja = min(interval1[0], interval2[0])
    zgornja_meja = max(interval1[1], interval2[1])
    return (spodnja_meja, zgornja_meja)

def presek_intervalov(interval1, interval2):
    spodnja_meja = max(interval1[0], interval2[0])
    zgornja_meja = min(interval1[1], interval2[1])
    if spodnja_meja <= zgornja_meja:
        return (spodnja_meja, zgornja_meja)
    else:
        return "Prazno"

def razlika_intervalov(interval1, interval2):
    spodnja_meja = interval1[0]
    zgornja_meja = interval1[1]
    if spodnja_meja <= interval2[0] and zgornja_meja >= interval2[1]:
        return "Prazno"
    elif spodnja_meja <= interval2[0] and zgornja_meja < interval2[1]:
        return (zgornja_meja, interval2[1])
    elif spodnja_meja > interval2[0] and zgornja_meja >= interval2[1]:
        return (interval2[0], spodnja_meja)
    else:
        return interval1

if __name__ == "__main__":
    kalkulator_intervalov()
