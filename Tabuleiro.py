import random

class JogoDaVelhaConsole:
    def __init__(self):
        # Inicializa o vetor de jogo com 10 posições (1 para número de jogadas, 9 para o tabuleiro)
        self.tabuleiro = [0] + [0] * 9
        # Aleatoriza o jogador que inicia
        self.jogador_atual = 1 if random.randint(1, 6) % 2 == 0 else -1
        print(f"O jogador {'X' if self.jogador_atual == 1 else 'O'} começa!")
        self.jogar()

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            posicao = int(input(f"Jogador {'X' if self.jogador_atual == 1 else 'O'} Escolha uma posição de 1 a 9 para jogar (1 é canto superior esquerdo, 9 é canto inferior direito): ")) - 1
            if self.tabuleiro[posicao + 1] == 0:
                self.fazer_jogada(posicao, self.jogador_atual)
            else:
                print("Posição inválida! Tente novamente.")
                continue
            if self.checar_vencedor():
                self.mostrar_tabuleiro()
                print(f"O jogador {'X' if self.jogador_atual == 1 else 'O'} venceu!")
                break
            elif self.tabuleiro[0] == 9:  # Verifica se deu empate
                self.mostrar_tabuleiro()
                print("Empate!")
                break

            # Alterna o jogador
            self.jogador_atual *= -1

    def fazer_jogada(self, posicao, jogador):
        self.tabuleiro[posicao + 1] = jogador
        self.tabuleiro[0] += 1

    def mostrar_tabuleiro(self):
        simbolos = {1: 'X', -1: 'O', 0: ' '}
        print("\nTabuleiro atual:")
        for i in range(0, 9, 3):
            print(f"{simbolos[self.tabuleiro[i + 1]]} | {simbolos[self.tabuleiro[i + 2]]} | {simbolos[self.tabuleiro[i + 3]]}")
            if i < 6:
                print("---------")

    def checar_vencedor(self):
        v = self.tabuleiro[1:10]

        # linhas
        if (v[0] == v[1] == v[2] != 0) or (v[3] == v[4] == v[5] != 0) or (v[6] == v[7] == v[8] != 0):
            return True

        # colunas
        if (v[0] == v[3] == v[6] != 0) or (v[1] == v[4] == v[7] != 0) or (v[2] == v[5] == v[8] != 0):
            return True

        # diagonais
        if (v[0] == v[4] == v[8] != 0) or (v[2] == v[4] == v[6] != 0):
            return True

        return False

# Inicializa o jogo
JogoDaVelhaConsole()
