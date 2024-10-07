import random

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [0] + [0] * 9
        # Aleatoriza o jogador que inicia
        self.jogador_atual = 1 if random.randint(1, 6) % 2 == 0 else -1
        print(f"O jogador {'X' if self.jogador_atual == 1 else 'O'} começa!")
        self.jogar()

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            if self.jogador_atual == 1:  # Jogador humano
                posicao = int(input("Escolha uma posição de 1 a 9 para jogar (1 é canto superior esquerdo, 9 é canto inferior direito): ")) - 1
                if self.tabuleiro[posicao + 1] == 0:
                    self.fazer_jogada(posicao, 1)
                else:
                    print("Posição inválida! Tente novamente.")
                    continue
            else:  # Jogada do computador
                self.jogada_computador()

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
        self.tabuleiro[0] += 1 # Numero de jogadas

    def jogada_computador(self):
        print("Jogada do computador...")
        
        # Verifica se é a primeira jogada e joga no centro, se estiver disponível
        if self.tabuleiro[5] == 0:  # Centro corresponde à posição 5
            self.fazer_jogada(4, -1)
            return
        # Bloqueia o jogador humano se ele estiver prestes a ganhar
        for posicao in range(9):
            if self.tabuleiro[posicao + 1] == 0:  # Se a posição estiver vazia
                self.tabuleiro[posicao + 1] = 1  # Temporariamente faz a jogada do humano
                if self.checar_vencedor():
                    self.tabuleiro[posicao + 1] = -1  # Bloqueia a jogada do humano com a jogada do computador
                    return
                self.tabuleiro[posicao + 1] = 0  # Reseta a posição se não for uma jogada vencedora

        # Tenta vencer se possível
        for posicao in range(9):
            if self.tabuleiro[posicao + 1] == 0:  # Se a posição estiver vazia
                self.tabuleiro[posicao + 1] = -1  # Faz a jogada do computador
                if self.checar_vencedor():  # Verifica se o computador venceu
                    return
                self.tabuleiro[posicao + 1] = 0  # Reseta a posição se não for uma jogada vencedora

        # Caso não possa bloquear ou vencer, realiza uma jogada aleatória
        while True:
            posicao = random.randint(0, 8)
            if self.tabuleiro[posicao + 1] == 0:  # Se a posição estiver vazia
                self.fazer_jogada(posicao, -1)
                break


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
JogoDaVelha()
