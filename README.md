# Jogo de Dados - README

Este é um simples jogo de dados onde os jogadores tentam acumular pontos lançando um dado. O objetivo do jogo é ser o primeiro a atingir a pontuação máxima de 50 pontos, sem perder pontos no processo.

## Descrição do Jogo

- O jogo pode ser jogado por **2 a 4 jogadores**.
- Cada jogador pode decidir se quer continuar jogando ou parar a sua vez. Durante sua vez, ele joga o dado, e a pontuação obtida é acumulada.
- Se um jogador rolar o dado e obtiver o valor **1**, ele perde toda a pontuação acumulada na rodada e sua vez termina imediatamente.
- O jogo termina quando um jogador atinge a pontuação máxima de **50 pontos**, sendo este o vencedor.

## Como Jogar

1. O número de jogadores será solicitado no início (deve ser entre 2 e 4).
2. Cada jogador, por sua vez, pode optar por **rolar o dado**. Se o jogador escolher não rolar o dado, a vez dele termina.
3. O dado será rolado aleatoriamente, gerando um número entre **1 e 6**.
4. Se o jogador rolar o **1**, ele perde todos os pontos acumulados na rodada e a vez dele é finalizada.
5. Se o jogador rolar qualquer outro número, ele acumula os pontos e pode continuar jogando ou decidir encerrar sua vez.
6. O primeiro jogador a atingir **50 pontos** é o vencedor.

## Como Executar

1. Clone o repositório ou copie o código em um arquivo Python (.py).
2. Execute o código utilizando um interpretador Python.
3. Siga as instruções no terminal para jogar!

### Exemplo de Execução:

```
Quantos jogadores vão jogar(2 - 4): 3
Jogador 1
Deseja rolar o dado? (s): s
você rodou o valor  4
sua pontuação agora é  4

Deseja rolar o dado? (s): s
você rodou o valor  3
sua pontuação agora é  7

Deseja rolar o dado? (s): n
sua pontuação agora é  7

Jogador 2
Deseja rolar o dado? (s): s
você rodou o valor  5
sua pontuação agora é  5

...

O jogador 1 venceu com 50 pontos
```

## Detalhes Técnicos

- **Função `roll()`**: Simula o lançamento de um dado, retornando um número entre 1 e 6.
- **Estrutura de Dados**: Utiliza uma lista (`players_pontuacao`) para armazenar a pontuação acumulada de cada jogador.
- **Entrada de Dados**: O programa solicita a quantidade de jogadores e, durante o jogo, pergunta ao jogador se ele deseja rolar o dado.

## Requisitos

- Python 3.x instalado.
- Nenhum módulo externo é necessário. O jogo utiliza apenas a biblioteca padrão do Python.

## Possíveis Melhorias

- Adicionar um sistema de feedback sobre o estado do jogo (como imprimir as pontuações durante o jogo).
- Implementar um sistema de "melhor de X partidas" para jogos contínuos.
- Adicionar um limite de tempo por turno para tornar o jogo mais dinâmico.

## Licença

Este projeto é de código aberto e pode ser usado, modificado ou distribuído conforme necessário.

---

Divirta-se jogando! 🎲
