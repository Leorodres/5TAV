import random
import csv

class JogoDaVelha:
    def __init__(self, modo_jogo, num_jogos=1):
        self.modo_jogo = modo_jogo
        self.num_jogos = num_jogos
        self.resultados = {"X": 0, "O": 0, "Empate": 0}
        self.tabuleiros = []
        self.total_jogos = 0
        self.iniciar_jogos()

    def iniciar_jogos(self):
        for _ in range(self.num_jogos):
            self.tabuleiro = [0] + [0] * 10
            self.jogador_atual = 1 if random.randint(1, 6) % 2 == 0 else -1
            print(f"\n\nO jogador {'X' if self.jogador_atual == 1 else 'O'} começa!")
            self.jogar()

        if self.num_jogos > 1:
            print("\nResultados:")
            print(f"Vitórias de X: {self.resultados['X']}")
            print(f"Vitórias de O: {self.resultados['O']}")
            print(f"Empates: {self.resultados['Empate']}")
            print(f"Tabuleiros de todos os jogos: {self.tabuleiros}")

    def jogar(self):
        while True:
            if self.modo_jogo == "JxJ":
                self.mostrar_tabuleiro()
                posicao = int(input(f"Jogador {'X' if self.jogador_atual == 1 else 'O'}, escolha uma posição de 1 a 9 para jogar (1 é canto superior esquerdo, 9 é canto inferior direito): ")) - 1
                if 0 <= posicao <= 8 and self.tabuleiro[posicao + 1] == 0:
                    self.fazer_jogada(posicao, self.jogador_atual)
                else:
                    print("Posição inválida! Tente novamente.")
                    continue  
            elif self.modo_jogo in ["JxAleatório", "JxCampeão"]:
                if self.jogador_atual == 1:
                    self.mostrar_tabuleiro()
                    posicao = int(input(f"Jogador {'X' if self.jogador_atual == 1 else 'O'}, escolha uma posição de 1 a 9 para jogar (1 é canto superior esquerdo, 9 é canto inferior direito): ")) - 1    
                    if self.tabuleiro[posicao + 1] == 0:
                        self.fazer_jogada(posicao, 1)
                    else:
                        print("Posição inválida! Tente novamente.")
                        continue
                else:  
                    self.jogada_computador()
            else:
                self.jogada_computador()
            if self.checar_vencedor():
                self.mostrar_tabuleiro()
                vencedor = 'X' if self.jogador_atual == 1 else 'O'
                print(f"O jogador {vencedor} venceu!")
                self.tabuleiro[10] = vencedor
                self.resultados[vencedor] += 1
                break
            elif self.tabuleiro[0] == 9:  # Verifica se deu empate
                self.mostrar_tabuleiro()
                print("Empate!")
                self.tabuleiro[10] = 'V'
                self.resultados["Empate"] += 1
                break

            # Alterna o jogador
            self.jogador_atual *= -1

        # Atualiza o acumulado de resultados ao final do jogo
        self.total_jogos += 1
        acumulado_resultados = [
            self.total_jogos,
            self.resultados['X'],  # Acumulado de vitórias do jogador 1 (X)
            self.resultados['Empate'],  # Acumulado de velhas (empates)
            self.resultados['O']  # Acumulado de vitórias do jogador 2 (O)
        ]
        self.tabuleiros.append(self.tabuleiro[:10] + acumulado_resultados)
        with open('resultados.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)

            # Escrevendo cada linha no arquivo
            for linha in self.tabuleiros:
                escritor.writerow(linha)
        

    def fazer_jogada(self, posicao, jogador):
        self.tabuleiro[posicao + 1] = jogador
        self.tabuleiro[0] += 1  # Numero de jogadas

    def jogada_computador(self):
        if self.modo_jogo in ["JxAleatório", "Aleatório_vs_Aleatório"]:
            print("Jogada do computador aleatório...")
            self.jogada_aleatoria()
        elif self.modo_jogo in ["JxCampeão", "Campeão_vs_Campeão"]:
            print("Jogada do computador campeão...")
            self.jogada_campeao()
        elif self.modo_jogo == "Aleatório_vs_Campeão":
            if self.jogador_atual == 1:
                print("Jogada do computador aleatório...")
                self.jogada_aleatoria()
            else:
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
        
        for posicao in range(9): # Tenta vencer
            if self.tabuleiro[posicao + 1] == 0:
                self.tabuleiro[posicao + 1] = self.jogador_atual
                if self.checar_vencedor():
                    self.fazer_jogada(posicao, self.jogador_atual)
                    return
                self.tabuleiro[posicao + 1] = 0

        if self.tabuleiro[5] == 0: # Caso o centro esteja vazio, joga no centro
            self.fazer_jogada(4, self.jogador_atual)
            return

        for posicao in range(9): # Tenta bloquear
            if self.tabuleiro[posicao + 1] == 0:
                self.tabuleiro[posicao + 1] = jogador_adversario
                if self.checar_vencedor():
                    self.tabuleiro[posicao + 1] = self.jogador_atual
                    self.fazer_jogada(posicao, self.jogador_atual)
                    return
                self.tabuleiro[posicao + 1] = 0

        
        
        # Laterais dos cantos
        cantos_com_laterais = {
            1: [2, 4],
            3: [2, 6],  
            7: [4, 8],  
            9: [6, 8]   
        }

        # Verifica se a contagem de jogada é a correta para a jogada das laterais
        if all(self.tabuleiro[i] == 0 for i in [1, 3, 7, 9] if i != self.jogador_atual):
            for canto, laterais in cantos_com_laterais.items():  
                if all(self.tabuleiro[lateral] == jogador_adversario for lateral in laterais) and self.tabuleiro[canto] == 0:
                    self.fazer_jogada(canto - 1, self.jogador_atual)
                    return


        if self.tabuleiro[5] == jogador_adversario and self.tabuleiro[0] == 1: # Caso o centro esteja ocupado joga em um canto
            if self.tabuleiro[1] == 0:
                self.fazer_jogada(0, self.jogador_atual)
                return
            if self.tabuleiro[3] == 0:
                self.fazer_jogada(2, self.jogador_atual)
                return
            if self.tabuleiro[7] == 0:
                self.fazer_jogada(6, self.jogador_atual)
                return
            if self.tabuleiro[9] == 0:
                self.fazer_jogada(8, self.jogador_atual)
                return
        
        # Verifica se o centro está ocupado pelo jogador adversário e se já ocorreram duas jogadas para impedir
        if self.tabuleiro[5] == jogador_adversario and self.tabuleiro[0] == 3:
            cantos = [1, 3, 7, 9]
            for canto in cantos: # Procura um canto disponível e joga nele
                if self.tabuleiro[canto] == 0:
                    self.fazer_jogada(canto - 1, self.jogador_atual)
                    return

        cantos_opostos = [(1, 9), (3, 7), (9, 1), (7, 3)] # Caso o inimigo jogou em cantos opostos joga em uma lateral
        if not any(self.tabuleiro[pos] != 0 for pos in [2, 4, 6, 8]):
            for canto1, canto2 in cantos_opostos:
                if (self.tabuleiro[canto1] == jogador_adversario and
                    self.tabuleiro[canto2] == jogador_adversario):
                    for lateral in [2, 4, 6, 8]:
                        if self.tabuleiro[lateral] == 0:
                            self.fazer_jogada(lateral - 1, self.jogador_atual)
                            return

        # Se não der pra jogar nas laterais, joga no canto oposto
        opostos = {
            1: 8, 
            3: 6, 
            7: 2, 
            9: 0
        }
        for canto in opostos:
            if self.tabuleiro[canto] == jogador_adversario and self.tabuleiro[opostos[canto] + 1] == 0:
                self.fazer_jogada(opostos[canto], self.jogador_atual)
                return

        # joga aleatoriamente caso nada funcione
        self.jogada_aleatoria()


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
modo = 0
while modo < 1 or modo > 6:
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