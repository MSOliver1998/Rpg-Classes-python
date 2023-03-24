from db_personagens import personagens
from random import randint

def dividir_cartas(quantidade=5):
    cartas_p1=[]
    cartas_p2=[]
    for index in range(0,quantidade*2):
        carta_num=randint(0,len(personagens)-1)
        carta=personagens[carta_num]
        if index%2==0:
            cartas_p1.append(carta)
        else:
            cartas_p2.append(carta)
        personagens.pop(carta_num)
    return [cartas_p1,cartas_p2]
    

def ver_personagens(personagens):
    print('-'*68)
    print(f'|{"n":^3}|{"nome":^15}| {"poder":^10}| {"vida":^10}| {"ataque":^10}| {"defesa":^10}| ')
    print('-'*68)
    for index,personagem in enumerate(personagens):
        persona=personagem.info_personagem()
        print(f'|{index:^3}|\033[035m{persona["name"].upper():^15}\033[0m| \033[034m{persona["power"]:^10}\033[0m| \033[033m{persona["life"]:^10}\033[0m| \033[031m{persona["atk"]:^10}\033[0m| \033[032m{persona["dfs"]:^10}\033[0m|')
        print('-'*68)

def ver_personagem(personagem,numero):
    print('-'*68)
    print(f'|{"n":^3}|{"nome":^15}| {"poder":^10}| {"vida":^10}| {"ataque":^10}| {"defesa":^10}| ')
    print('-'*68)
    persona=personagem.info_personagem()
    print(f'|{numero:^3}|\033[035m{persona["name"].upper():^15}\033[0m| \033[034m{persona["power"]:^10}\033[0m| \033[033m{persona["life"]:^10}\033[0m| \033[031m{persona["atk"]:^10}\033[0m| \033[032m{persona["dfs"]:^10}\033[0m|')
    print('-'*68)


def ataque(atacante,defensor):
    ataque=atacante.atacar()
    life=defensor.defesa(ataque)
    if life==0:
        return True
    return False


def recarregar(personagem,escolha,recarga:str):
    if recarga=='dfs':
        personagem.aum_dfs()
    if recarga=='atk':
        personagem.aum_atk()
    ver_personagem(personagem,escolha)

def input_int(text="insira o valor para teste: "):
    is_num=input(f'{text}')
    while type(is_num)!=int:
        try:
            is_num=int(is_num)
        except:
            is_num=input(f'{text}')
        else:
            return int(is_num)
    