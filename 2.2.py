Coca_Cola = False
Fanta_Cola = False
Sprite = False
Adocicada = False
Noz_de_cola = False
Cafeina = False
Acida = False


def base_fatos():

    global Noz_de_cola
    Noz_de_cola = True

if __name__ == '__main__':

    base_fatos()

    for i in range (0, 10):

        if Noz_de_cola and Fanta_Cola:
            Adocicada = True

        if Noz_de_cola and Cafeina:
            Coca_Cola = True

        if Noz_de_cola:
            Sprite = True
            Fanta_Cola = True

        if Coca_Cola and Adocicada:
            Acida = True

        if Acida:
            print(f'Ácida = sim\n')
            break
    else:
        print(f'Ácida = não\n')

