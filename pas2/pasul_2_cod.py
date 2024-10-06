tabla_de_joc = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

# utila pentru actualizarea listei care contine liniile, coloanele si diagonalele valide pentru un potential castig
def completare_lista(tabla):
    lista = [
        [tabla[1], tabla[2], tabla[3]],
        [tabla[4], tabla[5], tabla[6]],
        [tabla[7], tabla[8], tabla[9]],
        [tabla[1], tabla[4], tabla[7]],
        [tabla[2], tabla[5], tabla[8]],
        [tabla[3], tabla[6], tabla[9]],
        [tabla[1], tabla[5], tabla[9]],
        [tabla[3], tabla[5], tabla[7]]
    ]
    return lista

# verifica daca pozitia dorita este libera
def setare_element(tabla, poz)->bool:
    if tabla[poz] == '':
        return True
    else:
        return False

# insereaza elementul (X sau 0) pe pozitia dorita
def introducere_elem_nou(tabla, elem):
    while True:
        try:
            pozitie = input(f'Voi introduce elementul pe pozitia (1-9) pentru {elem}: ')
            pozitie = int(pozitie)
            if pozitie < 1 or pozitie > 9:
                print('Pozitiile valide sunt in intervalul 1-9. Te rog sa reintroduci!')
                continue
            if setare_element(tabla, pozitie):
                tabla[pozitie] = elem
                break
            else:
                print('Pozitia este deja ocupata. Te rog, selecteaza alta pozitie!')
        except ValueError:
            print("Trebuie sa introduci un numar! Te rog sa reintroduci!")

# verifica daca in urma mutarii a castigat cineva
def verificare_castig(lista)->bool:
    castig = False
    for lista_mica in lista:  #lista mica reprezinta o linie/ coloana/ diagonala unde se poate realiza castigul
        if lista_mica[0] == lista_mica[1] == lista_mica[2] and lista_mica[0] != '':
            castig = True
    return castig

# remiza este in cazul in care tabla este plina (deoarece daca este plina, atunci nu a fost declarat nimeni castigator)
def remiza(tabla):
    plina = True
    for i in range(1, 10):
        if tabla[i] == '':
            plina = False
            break
    return plina

# face tabla din nou goala
def resetare():
    return {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def afisare_tabla(tabla):
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

# programul principal
def x_0():
    print('Bine ai venit!')
    while True:
        jucator = 'X'
        tabla_de_joc = resetare()
        while True:
            afisare_tabla(tabla_de_joc)
            introducere_elem_nou(tabla_de_joc, jucator)
            lista = completare_lista(tabla_de_joc)
            if verificare_castig(lista):
                afisare_tabla(tabla_de_joc)
                print(f"A castigat jucatorul {jucator}")
                break
            elif remiza(tabla_de_joc):
                afisare_tabla(tabla_de_joc)
                print("remiza!")
                break
            if jucator == 'X':
                jucator = '0'
            else:
                jucator = 'X'
        print('Jocul s-a terminat! Doriti continuarea? (d/n)')
        decizie = input()
        if decizie != 'd':
            break

x_0()



