tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}


print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

def completare_lista(tabla):
    lista = [
        [tabla[1], tabla[2], tabla[3]],
        [tabla[4], tabla[5], tabla[6]],
        [tabla[7], tabla[8], tabla[9]],
        [tabla[1], tabla[4], tabla[7]],
        [tabla[2], tabla[5], tabla[8]],
        [tabla[3], tabla[6], tabla[9]],
        [tabla[1], tabla[5], tabla[8]],
        [tabla[3], tabla[5], tabla[7]]
    ]
    return lista

#pune valoarea unde este liber doar
def setare_element(tabla, poz)->bool:
    if tabla[poz] == '':
        return True
    else:
        return False


def verificare_castig(lista)->bool:
    castig = False
    print(lista)
    for lista_mica in lista:
        if lista_mica[0] == lista_mica[1] == lista_mica[2] and lista_mica[0] != '':
            castig = True
    return castig

def remiza(tabla):
    plina = True
    for i in range(1, 10):
        if tabla[i] == '':
            plina = False
            break
    return plina

def resetare(tabla):
    if remiza(tabla):
        tabla = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def introducere_elem_nou(tabla, elem):
    pozitie = input('voi introduce elementul pe pozitia: ')
    if pozitie.isdigit():
        pozitie = int(pozitie)
    while setare_element(tabla, pozitie) is False:
        pozitie = input('voi reintroduce elementul pe pozitia: ')
    tabla[pozitie] = elem
    lista = completare_lista(tabla)
    return tabla, completare_lista(tabla)

def afisare_tabla(tabla):
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")


lista = completare_lista(tabla)
while verificare_castig(lista) == False & remiza(tabla) == False:
    if verificare_castig(lista):
        resetare(tabla)
        print('a castigat utilizatorul!')
        break
    elif remiza(tabla):
        resetare(tabla)
        print("remiza!")
        break
    else:
        introducere_elem_nou(tabla, 'x')
        afisare_tabla(tabla)





