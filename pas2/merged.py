
# tabla_principala = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

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

#intoarce adevarat doar daca pozitia e libera
def setare_element(tabla, poz)->bool:
    if tabla[poz] == '':
        return True
    return False

# insereaza X pentru utilizator, in functie de ce pozitie isi alege acesta
#TODO de rezolvat astfel incat functia sa intoarca tabla (este obligatoriu ca functia sa intoarca ceva)
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
                break #return tabla
            else:
                print('Pozitia este deja ocupata! te rog sa alegi alta pozitie!')
        except ValueError:
            print('Te rog sa introduci un numar!')

# testeaza daca exista o combinatie castigatoare
def verificare_castig(lista)->bool:
    castig = False
    for lista_mica in lista:
        if lista_mica[0] == lista_mica[1] == lista_mica[2] and lista_mica[0] != '':
            castig = True
    return castig

def remiza(tabla):
    plina = True
    if '' in tabla.values():
        plina = False
    return plina


    # plina = True
    # # if '' in tabla.values()
    # for i in range(1, 10):
    #     if tabla[i] == '':
    #         plina = False
    #         break
    # return plina

def resetare():

        return {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}


def afisare_tabla(tabla):
    return f"{tabla[1]} | {tabla[2]} | {tabla[3]}\n---------\n{tabla[4]} | {tabla[5]} | {tabla[6]}\n---------\n{tabla[7]} | {tabla[8]} | {tabla[9]}\n"

# locurile libere
def locuri_libere(tabla):
    locuri_l = []
    for k, v in tabla.items():
        if v == '':
            locuri_l.append(k)
    return locuri_l

# verificarea si blocarea
def blocheaza_verifica(tabla, semn):
    castig = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # linii
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # coloane
        [1, 5, 9], [3, 5, 7]  # diagonale
    ]
    for structura in castig:
        valori = [tabla[structura[0]], tabla[structura[1]], tabla[structura[2]]]
        if valori.count(semn) == 2 and '' in valori:  # doua semne la fel si un loc liber
            index_gol = valori.index('')
            tabla[structura[index_gol]] = '0'
            return True
    return False

# mutarea calculator
#TODO de rezolvat astfel incat functia sa intoarca tabla, nu sa aiba un return gol
def mutare_calculator(tabla_bis, dif):
    if dif == 'greu':
        # verificare daca calculatorul castiga
        if blocheaza_verifica(tabla_bis, '0'):
            return
        # verificare daca utilizatorul castiga si blocare
        if blocheaza_verifica(tabla_bis, 'X'):
            return
        # mutare pe pozitiile favorabile daca nu blocam sau castigam
        pozitii_favorabile = [5, 1, 3, 7, 9, 2, 4, 6, 8]
        for pozitie in pozitii_favorabile:
            if tabla_bis[pozitie] == '':
                tabla_bis[pozitie] = '0'
                return
    elif dif == 'usor':
        pozitii_favorabile = [5, 1, 3, 7, 9, 2, 4, 6, 8]
        for pozitie in pozitii_favorabile:
            if tabla_bis[pozitie] == '':
                tabla_bis[pozitie] = '0'
                return

# ajuta utilizatorul sa aleaga nivelul de dificultate
def dificultate():
    while True:
        dif = input("Alege dificultatea jocului: (usor/greu) ")
        if dif != 'usor' and dif != 'greu':
            print('Te rog alege o optiune valida! (usor/greu)')
            continue
        else:
            return dif
#TODO de rezolvat astfel incat functia sa intoarca ceva (spre exemplu, rezultatul_jocului, de tip string)
def principal():
    # pentru mai multe jocuri consecutive
    while True:
        jucator_activ = 'utilizator'
        tabla_de_joc = resetare()
        dif = dificultate()
        # pentru un singur joc
        while True:
            print(afisare_tabla(tabla_de_joc))
            if jucator_activ == 'utilizator':
                introducere_elem_nou(tabla_de_joc, 'X')
            else:
                print(tabla_de_joc, 'linia 138')
                mutare_calculator(tabla_de_joc, dif)
                print(tabla_de_joc, 'linia 140')
            lista = completare_lista(tabla_de_joc)
            if verificare_castig(lista):
                print(afisare_tabla(tabla_de_joc))
                print(f'A castigat: {jucator_activ}ul') #return rezultat joc
                break
            elif remiza(tabla_de_joc):
                print(afisare_tabla(tabla_de_joc))
                print('Remiza!') #return rezultat joc
                break
            if jucator_activ == 'utilizator':
                jucator_activ = 'calculator'
            else:
                jucator_activ = 'utilizator'

        decizie = input('Doriti sa incepi un joc nou? (da/nu) ')
        if decizie != 'da':
            break

principal()
