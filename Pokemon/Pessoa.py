import random

from Pokemon import *

NOMES = [
    "José", "Maria", "Gabriel", "Nefasta", "Soneka", "ES7", "Rakel", "Tian", "Dimmy", "Pablo",
    "Stella", "Wing", "WangGod", "Alisson", "Silvão", "Picezah","Crazy", "Bissoli", "Mah", 
    "Muçando", "Cereja", "Rexy", "Eragon", "RBN", "Vicky", "Hooking",
]

POKEMON = [
    PokemonFogo("Charmander"),
    PokemonFogo("Charmiliom"),
    PokemonFogo("Fogarel"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonEletrico("Trovãozin"),
    PokemonAgua("Aquatico"),
    PokemonAgua("Squirtle"),
    PokemonAgua("PeixeSapo"),   
]

class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons
        
        self.dinheiro = dinheiro
        
    def __str__(self):
        return self.nome
    
    def mostrar_pokemons(self):
        
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem nenhum pokemon !!".format(self))
    
    def mostrar_dinheiro(self):
        print("Você possui ${} em sua conta.".format(self.dinheiro))
        
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou ${}".format(quantidade))
        self.mostrar_dinheiro()
            
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))
        
        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()       
        pokemon = self.escolher_pokemon()
        
        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha!!!".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print("{} ganhou a batalha!!!".format(pessoa))
                    break
        else:
            print("Esta batalha não pode ocorrer!")
        
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Este jogador não possui pokemons")
                                    
        
class Player(Pessoa):
    tipo = "player"
    
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!!".format(self, pokemon))
    
    def escolher_pokemon(self):
        self.mostrar_pokemons()
        
        if self.pokemons:
            while True:
                escolha = input("escolha seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida!!")
        else:
            print("ERRO: Este jogador não possui pokemons")
            
    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMON)
            print("Você encontrou um pokemon selvagem: {}".format(pokemon))
            escolha = input("Deseja capturar? (s/n)")
            if escolha == "s":
                if random.random() > 0.7:
                    self.capturar(pokemon)
                else:
                    print("Você não conseguiu capturar e ele fugiu!!")
            else:
                print("Ok, boa viagem!")
        else:
            print("Essa exploração não deu em nada.")
    
class Inimigo(Pessoa):
    tipo = "inimigo"
    
    def __init__(self, nome=None, pokemons=None):
        
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1,5)):
                pokemons_aleatorios.append(random.choice(POKEMON))
                super().__init__(nome=None, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=None, pokemons=pokemons)
    
   




