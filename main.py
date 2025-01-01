import random
def roll():
    min_valor = 1
    max_valor = 6
    roll = random.randint(min_valor, max_valor)
    return roll


while  True:
    players = input("Quantos jogadores vão jogar(2 - 4): ")
    if players.isdigit():
        players = int(players)
        if players >= 4 or players <= 2:
            break
        else:
            print('precisa ter entre 2 e 4 jogadores')
    else:
        print("Quantidade inválida. Tente novamente")
        
pontuacao_maxima = 50

players_pontuacao = [0 for i in range(players)]
    
while max(players_pontuacao) < pontuacao_maxima:
    for player_idx in range(players):
        print(f'Jogador {player_idx + 1}')
        pontuacao_atual = 0
        
        while True:
            should_roll = input("Deseja rolar o dado? (s): ")
            if should_roll.lower() != "s":
                break
            valor = roll()
            if valor == 1:
                print("voce rodou 1: perdeu sua vez")
                pontuacao_atual = 0
                break
            else:
                pontuacao_atual += valor
                print("você rodou o valor ", valor)
                
            print("sua pontuação agora é ", pontuacao_atual, "\n")
        players_pontuacao[player_idx] += pontuacao_atual
        print("sua pontuação agora é ", players_pontuacao[player_idx], "\n")
        
        
pontuacao_maxima = max(players_pontuacao)
vencedor_idx = players_pontuacao.index(pontuacao_maxima)
print(f"O jogador {vencedor_idx + 1} venceu com {pontuacao_maxima} pontos")


        