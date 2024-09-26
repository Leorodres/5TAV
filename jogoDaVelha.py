import tkinter as tk
from tkinter import messagebox
import random

class JogoDaVelha:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Jogo da Velha")
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]
        self.criar_botoes()
        # Aleatoriza o jogador a iniciar e caso seja o "O" faz uma jogada aleatoria
        self.jogador_atual = "X" if random.randint(1, 6) % 2 == 0 else "O"
        if self.jogador_atual == "O":
            self.jogador_aleatorio()

    def criar_botoes(self):
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        for linha in range(3):
            for coluna in range(3):
                botao = tk.Button(self.raiz, text="", font=('Arial', 24), width=5, height=2,
                                  command=lambda l=linha, c=coluna: self.clique(l, c))
                botao.grid(row=linha, column=coluna, padx=5, pady=5)
                self.botoes[linha][coluna] = botao

    def clique(self, linha, coluna):
        # Verifica se o botao clicado possui algo, caso não preenche com o jogador atual
        if self.tabuleiro[linha][coluna] is None:
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)

            if self.checar_vencedor():
                messagebox.showinfo("Fim de Jogo", f"{self.jogador_atual} venceu!")
                self.reiniciar()
            
            # Verifica se todos os botoes estao preenchidos com texto
            elif all(cel is not None for linha in self.tabuleiro for cel in linha):
                messagebox.showinfo("Empate", "Empate!")
                self.reiniciar()
            else:
                # Modifica o jogador que está jogando
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
                if self.jogador_atual == "O":
                    self.jogador_aleatorio()

    def jogador_aleatorio(self):
        botoes_vazios = [(l, c) for l in range(3) for c in range(3) if self.tabuleiro[l][c] is None] # Verifica botoes vazios
        linha, coluna = random.choice(botoes_vazios)
        self.clique(linha, coluna)

    def checar_vencedor(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] is not None:
                return True
        for coluna in range(3): 
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] and self.tabuleiro[0][coluna] is not None:
                return True
            
        # Diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] is not None:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] is not None:
            return True
        return False

    def reiniciar(self):
        self.jogador_atual = "X"
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)] # Limpa tabuleiro
        for linha in range(3): # Limpa texto botões
            for coluna in range(3):
                self.botoes[linha][coluna].config(text="")

root = tk.Tk()
app = JogoDaVelha(root)
root.mainloop()
