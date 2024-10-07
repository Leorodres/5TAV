import random

class JogoDaVelha:
    def __init__(self, modo_jogo, num_jogos=1):
        self.modo_jogo = modo_jogo
        self.num_jogos = num_jogos
        self.resultados = {"X": 0, "O": 0, "Empate": 0}
        self.iniciar_jogos()

    def iniciar_jogos(self):
        for _ in range(self.num_jogos):
            self.tabuleiro = [0] + [0] * 9
            self.jogador_atual = 1 if random.randint(1, 6) % 2 == 0 else -1
            print(f"O jogador {'X' if self.jogador_atual == 1 else 'O'} começa!")
            self.jogar()

        if self.num_jogos > 1:  # Exibir resultados se mais de um jogo for jogado
            print("\nResultados:")
            print(f"Vitórias de X: {self.resultados['X']}")
            print(f"Vitórias de O: {self.resultados['O']}")
            print(f"Empates: {self.resultados['Empate']}")

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()  # Mostrar o tabuleiro no início de cada turno
            if self.modo_jogo in ["JxJ"]:
                posicao = int(input(f"Jogador {'X' if self.jogador_atual == 1 else 'O'} Escolha uma posição de 1 a 9 para jogar (1 é canto superior esquerdo, 9 é canto inferior direito): ")) - 1
                if self.tabuleiro[posicao + 1] == 0:
                    self.fazer_jogada(posicao, self.jogador_atual)
                    
            if self.modo_jogo in ["JxAleatório", "JxCampeão"]:
                if self.jogador_atual == 1:  # Jogador humano
                    posicao = int(input("Escolha uma posição de 1 a 9 para jogar (1 é canto superior esquerdo, 9 é canto inferior direito): ")) - 1
                    if self.tabuleiro[posicao + 1] == 0:
                        self.fazer_jogada(posicao, 1)
                    else:
                        print("Posição inválida! Tente novamente.")
                        continue
                else:
                    self.jogada_computador()
            else:
                self.jogada_computador()
            print(self.tabuleiro)

            if self.checar_vencedor():
                self.mostrar_tabuleiro()  # Mostrar o tabuleiro após a vitória
                vencedor = 'X' if self.jogador_atual == 1 else 'O'
                print(f"O jogador {vencedor} venceu!")
                self.resultados[vencedor] += 1
                break
            elif self.tabuleiro[0] == 9:  # Verifica se deu empate
                self.mostrar_tabuleiro()
                print("Empate!")
                self.resultados["Empate"] += 1
                break

            # Alterna o jogador
            self.jogador_atual *= -1

    def fazer_jogada(self, posicao, jogador):
        self.tabuleiro[posicao + 1] = jogador
        self.tabuleiro[0] += 1  # Numero de jogadas

    def jogada_computador(self):
        if self.modo_jogo in ["JxAleatório", "Aleatório_vs_Aleatório"]:
            print("Jogada do computador aleatório...")
            self.jogada_aleatoria()
        elif self.modo_jogo in ["JxCampeão", "Aleatório_vs_Campeão", "Campeão_vs_Campeão"]:
            print("Jogada do computador campeão...")
            self.jogada_campeao()

    def jogada_aleatoria(self):
        while True:
            posicao = random.randint(0, 8)
            if self.tabuleiro[posicao + 1] == 0:
                self.fazer_jogada(posicao, self.jogador_atual)
                break

    def jogada_campeao(self):
        jogador_adversario = 1 if self.jogador_atual == -1 else -1

        # Se for centro, joga nele
        if self.tabuleiro[5] == 0:
            self.fazer_jogada(4, self.jogador_atual)
            return

        # Bloqueia o outro jogador
        for posicao in range(9):
            if self.tabuleiro[posicao + 1] == 0:
                self.tabuleiro[posicao + 1] = jogador_adversario
                if self.checar_vencedor():
                    self.tabuleiro[posicao + 1] = self.jogador_atual  # Aqui é onde a jogada do campeão é feita
                    self.fazer_jogada(posicao, self.jogador_atual)  # Atualiza o vetor de jogadas
                    return
                self.tabuleiro[posicao + 1] = 0

        # Tenta vencer
        for posicao in range(9):
            if self.tabuleiro[posicao + 1] == 0:
                self.tabuleiro[posicao + 1] = self.jogador_atual
                if self.checar_vencedor():
                    self.fazer_jogada(posicao, self.jogador_atual)  # Atualiza o vetor de jogadas
                    return
                self.tabuleiro[posicao + 1] = 0

        self.jogada_aleatoria()  # Se nenhuma jogada estratégica for feita, joga aleatoriamente


    def mostrar_tabuleiro(self):
        print("\nTabuleiro atual:")
        simbolos = {1: 'X', -1: 'O', 0: ' '}
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


# Interface para escolha do tipo de jogo
print("Escolha o modo de jogo:")
print("1. Jogador vs Jogador")
print("2. Jogador vs Aleatório")
print("3. Jogador vs Campeão")
print("4. Aleatório vs Aleatório")
print("5. Aleatório vs Campeão")
print("6. Campeão vs Campeão")

modo = int(input("Digite o número do modo de jogo desejado: "))
num_jogos = 1

if modo in [4, 5, 6]:
    num_jogos = int(input("Quantas partidas serão jogadas? "))

modos = {
    1: "JxJ", 
    2: "JxAleatório", 
    3: "JxCampeão", 
    4: "Aleatório_vs_Aleatório", 
    5: "Aleatório_vs_Campeão", 
    6: "Campeão_vs_Campeão"
}

JogoDaVelha(modos[modo], num_jogos)
