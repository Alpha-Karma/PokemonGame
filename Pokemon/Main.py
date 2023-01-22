from Pokemon import *
from Pessoa import *
import pickle 


def escolher_pokemon_inicial(Player):
    print("Olá {}, você poderá escolher agora o pokemon que lhe acompanhará nesta jornada!!".format(Player))
    
    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)
    
    print("Você possui 3 escolhas:")
    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)
    
    while True:
        escolha = input("Escolha seu pokemon: ")
        
        if escolha == "1":
            Player.capturar(pikachu)
            break
            
        elif escolha == "2":
            Player.capturar(charmander)
            break
        
        elif escolha == "3":
            Player.capturar(squirtle)
            break
        
        else:
            print("Escolha inválida:") 
            
def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("Jogo salvo com sucesso !!")
    except Exception as error:
        print("Algo deu errado")
        print(error)
        
def carregar_jogo():
    try:
        with open("database.db" "wb") as arquivo:
            player = pickle.dump(arquivo)
            return player
    except Exception as error:
        print("Save não encontrado.")
        
            
if __name__ == "__main__":
    print("------------------------------------------------------")
    print("Bem vindo ao jogo Pokemon RPG de terminal!!!")
    print("------------------------------------------------------")
    
    player = carregar_jogo()

    if not player:
        nome = input("Olá, qual seu nick: ")
        player = Player(nome)
        print("Olá {}, esse é um mundo habitado por pokemons,"
            "então trabalhe duro para se tornar um mestre pokemon".format(player))
        print("Capture o máximo de pokemons que conseguir e derrote"
            "seus inimigos")
        player.mostrar_dinheiro()
        
        if player.pokemons:
            print("Já vi que tem alguns pokemons")
            player.mostrar_pokemons
        else:
            print("Você deve escolher seu primeiro pokemon!!")
            escolher_pokemon_inicial(player)
        
        print("Pronto, agora você já pode lutar com seu rival de infância.")
        inimigo1 = Inimigo(nome="ex", pokemons=[PokemonAgua("squirtle", level=1)])
        player.batalhar(inimigo1)
        
        salvar_jogo(player)
    
    while True:
        print("---------------------MENU-----------------------------")
        print("O que deseja fazer?")
        print("1 - Explorar o mundo :o")
        print("2 - batalhar")
        print("3 - ver pokedex")
        print("4 - ver conta")
        print("9 - sair do jogo :c")
        escolha = input("Sua escolha: ")
        print("------------------------------------------------------")

       
        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            player.batalhar(Inimigo())
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        elif escolha =="4":
            player.mostrar_dinheiro()
        elif escolha == "9":
            print("------------------------------------------------------")
            print("Saindo, Volte sempre !!!")
            print("------------------------------------------------------")
            break
        else:
            print("ERRO: escolha inválida!!")
        

