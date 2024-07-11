import random
import time

game = True
c = [True, False]
i = 0
lifep = 3
lifed = 3
vez_atual = "Player"
inimigo = ["Atacar", "Si"]
balas = None  # Variável global para balas

def main():
    global game, vez_atual
    print('Desejas jogar?')
    op = str(input()).lower()
    if op == "sim":
        while game:
            global balas, i, lifep, lifed
            balas = random.choice(c)
            time.sleep(0.5)
            print(f'Vida do jogador: {lifep} \nVida do inimigo: {lifed}')                        
            print(f'Total de balas: {6-i}')
            print("Vamos ver de quem é a vez...")
            time.sleep(1)
            if vez_atual == "Player":
                player_j()
            if vez_atual == "Inimigo":
                inimigo_j()
            testes()
    elif op == "nao":
        game = False
        time.sleep(0.5)
        print('Ate a proxima....')
        time.sleep(0.5)
    else:
        print('Invalido')

def player_j():
    global vez, i, lifep, lifed, balas, vez_atual
    if vez_atual == "Player":
        print('Aja!')
        time.sleep(0.5)
        print('Atirar em si ou no inimigo? (1/2)')
        es = int(input())
        if es == 1:
            print('Atirando em si...')
            time.sleep(1)
            print('.')
            time.sleep(1)
            if balas:
                print('Era uma bala real!')
                lifep -= 1
                i += 1
                vez_atual = "Inimigo"
            else:
                print('Bala falsa...')
                i += 1
                vez_atual = "Player"
        elif es == 2:
            print('Atirando no inimigo...')
            time.sleep(1)
            print('.')
            time.sleep(1)
            if balas:
                print('Era uma bala real!')
                lifed -= 1
                i += 1
                vez_atual= "Inimigo"
            else:
                print('Bala falsa...')
                i += 1
                vez_atual = "Inimigo"
        else:
            print("Invalido")
                    
def inimigo_j():
    global vez, i, lifep, lifed, balas, vez_atual
    if vez_atual == "Inimigo":
        print('Vez do inimigo....')
        time.sleep(1)
        atk = random.choice(inimigo)
        if atk == "Atacar":
            print('Ele irá te atacar...')
            time.sleep(1)
            print('.')
            time.sleep(1)
            if balas == True:
                print('Acertou!')
                lifep -= 1
                i += 1
                vez_atual = "Player"
            else:
                print("Bala falsa...")
                i += 1
                vez_atual = "Player"
        if atk == "Si":
            print('Ele irá se atacar...')
            time.sleep(1)
            print('.')
            time.sleep(1)
            if balas == True:
                print('Era verdadeira!')
                lifed -= 1
                i += 1
                vez_atual = "Player"
            else:
                print('Bala falsa...')
                i += 1
                vez_atual = "Inimigo"

def testes():
    global game, lifep, lifed, i
    if lifep <= 0:
        print('Voce perdeu...')
        game = False
    elif lifed <= 0:
        print('Voce ganhou, parabens!')
        game = False
    elif i > 3:
        print('Balas acabaram, deseja recarregar?')
        o = str(input()).lower()
        if o == "sim":
            i = 0
        else:
            print("Encerrando...")
            time.sleep(1)
            game = False

main()