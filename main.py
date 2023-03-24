from functions_game import *

cartas=dividir_cartas()
i=0

while len(cartas[0])>0 and len(cartas[1])>0:
    if i%2==0:
        print('#'*68)
        print(f'{"vez do usuario":^68}')
        print('#'*68)
        ver_personagens(cartas[0])
        if len(cartas[0])>0:
            escolha=input_int(f'escolha uma carta 0-{len(cartas[0])-1}\n: ')
        else:
            escolha=0
        while escolha>len(cartas[0])-1 or escolha<0:
            print('valor de carta inexistente')
            escolha=input_int(f'escolha uma carta 0-{len(cartas[0])-1}\n: ')
        ver_personagem(cartas[0][escolha],escolha)
        acao=input_int('o que deseja fazer? \n\033[031m[0] atacar\033[0m\n\033[032m[1] recarregar\033[0m \n:')
        while acao>1 or acao<0:
            print('ação inválida')
            acao=input_int('o que deseja fazer? \n\033[031m[0] atacar\033[0m\n\033[032m[1] recarregar\033[0m \n:')
        if acao==0:
            if len(cartas[1])<1:
                atacar=0
            else:
                atacar=input_int(f'qual carta deseja atacar? 0-{len(cartas[1])-1}\n:')
                while atacar>len(cartas[1])-1 or atacar<0:
                    atacar=input_int(f'qual carta deseja atacar? 0-{len(cartas[1])-1}\n:')
            morreu=ataque(cartas[0][escolha],cartas[1][atacar])
            if morreu:
                cartas[1].pop(atacar)
                ver_personagens(cartas[1])
        if acao==1:
            item=input_int('qual categoria deseja recarregar \033[031m\n[0] Ataque\033[0m \033[032m\n[1] Defesa\033[0m\n:')
            while item>len(cartas[1]) or item<0:
                item=input_int('qual categoria deseja recarregar \033[031m\n[0] Ataque\033[0m \033[032m\n[1] Defesa\033[0m\n:')
            if item==0:
                recarregar(cartas[0][escolha],escolha,'atk')
            if item==1:
                recarregar(cartas[0][escolha],escolha,'dfs')
        i+=1
        
    else:
        print('#'*68)
        print(f'{"vez do pc":^68}')
        print('#'*68)
        if len(cartas[1])>1:
            escolha_pc=randint(0,len(cartas[1])-1)
        else:
            escolha_pc=0
        acao_pc=randint(0,1)
        if acao_pc==0:
            print('o pc está atacando!')
            if len(cartas)>1:
                atacar_pc=randint(0,len(cartas[0])-1)
            else:
                atacar_pc=0
            morreu=ataque(cartas[1][escolha_pc],cartas[0][atacar_pc])
            if morreu:
                cartas[0].pop(atacar_pc)
        if acao_pc==1:
            print('o pc esta recarregando!')
            item_pc=randint(0,1)
            if item_pc==0:
                recarregar(cartas[1][escolha_pc],escolha_pc,'atk')
            if item_pc==1:
                recarregar(cartas[1][escolha_pc],escolha_pc,'dfs')
        i+=1

print('fim de jogo')
