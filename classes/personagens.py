class Personagem:
    def __init__ (self,nome:str,power:str,life:int,atk:int,dfs:int):
        self.name=nome
        self.power=power
        self.life=life
        self.atk=atk
        self.dfs=dfs

    def atacar(self):
        print(f'{self.name} está atacando com {self.power}')
        return(self.atk)
    
    def defesa(self,ataque):
        print(f'{self.name} está defendendo')
        if ataque>self.dfs:
            self.life-=ataque-self.dfs
            if self.life>0:
                print(self.life)
            else:
                print(f'{self.name} eliminado')
                return 0
        else:
            print('nenhum dano sofrido')

    
    def aum_dfs(self):
        self.dfs+=500
        return f'{self.name} fez uma recarga na defesa {self.dfs}'

    def aum_atk(self):
        self.atk+=500
        return f'{self.name} fez uma recarga no ataque {self.atk}'

    def info_personagem(self)->dict:
        return {'name':self.name,'power':self.power,'life':self.life,'atk':self.atk,'dfs':self.dfs}
