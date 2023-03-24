from classes.personagens import Personagem

personagens=list()

mago=Personagem('mago','magia',2000,1500,2000)
bruxa=Personagem('bruxa','magia',3000,1000,2000)
dragao=Personagem('dragão','fogo',5000,3000,5000)
cavaleiro=Personagem('cavaleiro','espada',3000,2000,5000)
elfo=Personagem('elfo','velocidade',4000,2500,1300)
centuriao=Personagem('centurião','velocidade',5000,3500,3500)
rei=Personagem('rei','palavra',3000,5000,5000)
exercito=Personagem('exercito','espada',5000,5000,5000)
lanceiro=Personagem('lanceiro','lanças',3500,1500,1500)
conselheiro=Personagem('conselheiro','palavra',100,1500,1500)
guardas=Personagem('guardas','espada',2500,2500,5000)
cacador=Personagem('Caçador','armas',3000,5000,2000)
princesa=Personagem('princesa','flexas',3000,2500,1500)
flexeiro=Personagem('flecheiro','flexas',3500,2500,1500)
orc=Personagem('orc','bastão',5000,2500,3000)

personagens.extend([mago,bruxa,dragao,cavaleiro,elfo,centuriao,rei,exercito,lanceiro,conselheiro,guardas,cacador,princesa,flexeiro,orc])
