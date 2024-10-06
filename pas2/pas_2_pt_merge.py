tabla_de_joc = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

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

#pune valoarea unde este liber doar
def setare_element(tabla, poz)->bool:
    if tabla[poz] == '':
        return True
    else:
        return False


def verificare_castig(lista)->bool:
    castig = False
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

def resetare():

        return {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def introducere_elem_nou(tabla, elem):
    while True:
        try:
            pozitie = input('Voi introduce elementul pe pozitia: ')
            pozitie = int(pozitie)
            if pozitie not in range(1, 10):
                print('Introdu elementul pe pozitia corecta (1-9)!')
                continue
            if setare_element(tabla, pozitie): #daca pozitia e libera
                tabla[pozitie] = elem
                break
            else:
                print('Pozitia este deja ocupata! te rog sa alegi alta pozitie!')
        except ValueError:
            print('Te rog sa introduci un numar!')

def afisare_tabla(tabla):
    print(f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}")

def principal():
    # pentru mai multe jocuri consecutive
    while True:
        jucator_activ = 'X'
        tabla_de_joc = resetare()
        # pentru un singur joc
        while True:
            afisare_tabla(tabla_de_joc)
            introducere_elem_nou(tabla_de_joc, jucator_activ)
            lista = completare_lista(tabla_de_joc)
            if verificare_castig(lista):
                afisare_tabla(tabla_de_joc)
                print(f'A castigat jucatorul {jucator_activ}')
                break
            elif remiza(tabla_de_joc):
                afisare_tabla(tabla_de_joc)
                print('Remiza!')
                break
            if jucator_activ == 'X':
                jucator_activ = '0'
            else:
                jucator_activ = 'X'

        decizie = input('Doriti sa incepi un joc nou? (da/nu) ')
        if decizie != 'da':
            break

principal()


