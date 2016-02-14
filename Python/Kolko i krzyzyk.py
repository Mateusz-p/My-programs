rozmiar = 0
plansza = []
litery = []
liczby = []
tura = 1
wskazane_pole = 'A1'
czy_wspolrzedne_wlasciwe = True
sprawdz_wygrana = False
zwyciezca = ''

print('Przed rozpoczęciem gry proszę podać rozmiar planszy, oraz imiona graczy')
print('Uwaga! Przy podawaniu współrzędnych należy uwzględnić wielkość liter.')

# Określamy rozmiar
while rozmiar < 20 or rozmiar > 40:
    rozmiar = int(input('Rozmiar planszy: '))
    if not 20 <= rozmiar <= 40:
        print('Minimaly rozmiar: 20\nMaksymalny rozmiar: 40')

# Dodajemy oznaczenia współrzędnych
for i in range(0, rozmiar):
    if i < 26:
        litery.append(chr(65+i))
    else:
        litery.append(chr(71+i))
litery = ''.join(litery)
plansza.append('  '+litery)

# Wstawiamy oznaczenia współrzędnych do planszy
for i in range(0,9):
    liczby.append(' ' + str(i+1))
for i in range(9, rozmiar):
    liczby.append(str(i+1))

for i in range(0,rozmiar):
    plansza.append([liczby[i]] + ['-'] * rozmiar)

# Funkcja drukująca planszę
def pokazPlansze(zmienna):
    for i in zmienna:
        print(''.join(i))

# Współrzędne punktu A1: [1][1]

gracz_1 = input('Imię pierwszego gracza: ')
gracz_2 = input('Imię drugiego gracza: ')

# Funkcja sprawdzająca, czy gracz podał właściwe współrzędne
def czyWspolrzedneWlasciwe(arg):
    podane_wspolrzedne = []
    if rozmiar <= 26:
        if not (ord(arg[0]) >= 65 and ord(arg[0]) <= 64 + rozmiar): # Czy arg[0] = litera w zakresie planszy
            return False
        else:
            podane_wspolrzedne.append(arg[0])
        if len(arg) == 2: # Czy arg[1] to cyfra
            if not 49 <= ord(arg[1]) <= 57:
                return False
            else:
                podane_wspolrzedne.append(arg[1])
        elif len(arg) == 3:
            if not 49 <= ord(arg[1]) <= 57:
                return False
            else:
                podane_wspolrzedne.append(arg[1:3])
        else:
            return False
        if int(podane_wspolrzedne[1]) > rozmiar:
            return False
    if rozmiar > 26:
        if ord(arg[0]) < 65 or (90 < ord(arg[0]) < 97) or ord(arg[0]) > 70 + rozmiar:
            return False
        else:
            podane_wspolrzedne.append(arg[0])
        if len(arg) == 2:
            if not 49 <= ord(arg[1]) <= 57:
                return False
            else:
                podane_wspolrzedne.append(arg[1])
        elif len(arg) == 3:
            if not 49 <= ord(arg[1]) <= 57:
                return False
            else:
                podane_wspolrzedne.append(arg[1:3])
        else:
            return False
        if int(podane_wspolrzedne[1]) > rozmiar:
            return False    
    if 'A' <= podane_wspolrzedne[0] <= 'Z':
        podane_wspolrzedne[0] = ord(podane_wspolrzedne[0]) - 64
    else:
        podane_wspolrzedne[0] = ord(podane_wspolrzedne[0]) - 70
    
    podane_wspolrzedne[0], podane_wspolrzedne[1] = int(podane_wspolrzedne[1]), podane_wspolrzedne[0]
    
    if plansza[podane_wspolrzedne[0]][podane_wspolrzedne[1]] != '-':
        return False
    elif tura == 1:
        plansza[podane_wspolrzedne[0]][podane_wspolrzedne[1]] = 'o'
    else:
        plansza[podane_wspolrzedne[0]][podane_wspolrzedne[1]] = 'x'
    
    return True

# Funkcja sprawdzająca czy wygraliśmy
def sprawdzWygrana(arg):
    for i in range(1, len(arg)):
        for j in range(1, len(arg)-4):
            if arg[i][j] == arg[i][j+1] == arg[i][j+2] == arg[i][j+3] == arg[i][j+4] != '-':
                plansza[i][j], plansza[i][j+2], plansza[i][j+4] = 'W', 'I', 'N'
                return True
    for i in range(1, len(arg)-4):
        for j in range(1, len(arg)):
            if arg[i][j] == arg[i+1][j] == arg[i+2][j] == arg[i+3][j] == arg[i+4][j] != '-':
                plansza[i][j], plansza[i+2][j], plansza[i+4][j] = 'W', 'I', 'N'               
                return True
    for i in range(1, len(arg)-4):
        for j in range(1, len(arg)-4):
            if arg[i][j] == arg[i+1][j+1] == arg[i+2][j+2] == arg[i+3][j+3] == arg[i+4][j+4] != '-':
                plansza[i][j], plansza[i+2][j+2], plansza[i+4][j+4] = 'W', 'I', 'N'
                return True
    for i in range(1, len(arg)-4):
        for j in range(5, len(arg)):
            if arg[i][j] == arg[i+1][j-1] == arg[i+2][j-2] == arg[i+3][j-3] == arg[i+4][j-4] != '-':
                plansza[i][j], plansza[i+2][j-2], plansza[i+4][j-4] = 'W', 'I', 'N'
                return True
    return False

while True:
    if tura == 1:
        print('\nRuch:', gracz_1)
        pokazPlansze(plansza)
        wskazane_pole = input('Gdzie chcesz postawić kółko: ')
        czy_wspolrzedne_wlasciwe = czyWspolrzedneWlasciwe(wskazane_pole)
        while not czy_wspolrzedne_wlasciwe:
            print('Proszę podać poprawne współrzędne.')
            wskazane_pole = input('Gdzie chcesz postawić kółko: ')
            czy_wspolrzedne_wlasciwe = czyWspolrzedneWlasciwe(wskazane_pole)
        sprawdz_wygrana = sprawdzWygrana(plansza)
        if sprawdz_wygrana:
            pokazPlansze(plansza)
            zwyciezca = gracz_1
            break
        tura = 2
    if tura == 2:
        print('\nRuch:', gracz_2)
        pokazPlansze(plansza)
        wskazane_pole = input('Gdzie chcesz postawić krzyżyk: ')
        czy_wspolrzedne_wlasciwe = czyWspolrzedneWlasciwe(wskazane_pole)
        while not czy_wspolrzedne_wlasciwe:
            print('Proszę podać poprawne współrzędne.')
            wskazane_pole = input('Gdzie chcesz postawić krzyżyk: ')
            czy_wspolrzedne_wlasciwe = czyWspolrzedneWlasciwe(wskazane_pole)
        sprawdz_wygrana = sprawdzWygrana(plansza)
        if sprawdz_wygrana:
            pokazPlansze(plansza)
            zwyciezca = gracz_2
            break
        tura = 1

print('Gratulacje', zwyciezca)
