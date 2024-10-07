import tkinter as tk
from tkinter import messagebox
import random

# Classe que representa o Jogo da Velha
class JogoDaVelha:
    def __init__(self, raiz):
        # Inicializa a janela principal e o jogador atual
        self.raiz = raiz
        self.raiz.title("Jogo da Velha")  # Título da janela
        
        self.jogador_atual = "X"  # O jogo sempre começa com o jogador "X"
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]  # Cria um tabuleiro 3x3 vazio
        self.criar_widgets()  # Chama o método que cria a interface (botões)

    def criar_widgets(self):
        # Cria uma grade 3x3 de botões para representar o tabuleiro
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        
        for linha in range(3):
            for coluna in range(3):
                # Cria um botão vazio para cada célula do tabuleiro
                botao = tk.Button(self.raiz, text="", font=('Arial', 24), width=5, height=2,
                                  command=lambda l=linha, c=coluna: self.on_botao_clicado(l, c))
                botao.grid(row=linha, column=coluna, padx=5, pady=5)  # Coloca o botão no grid (interface)
                self.botoes[linha][coluna] = botao  # Armazena o botão em uma lista para referência futura
    
    def on_botao_clicado(self, linha, coluna):
        # Executado quando um botão é clicado
        
        # Verifica se a célula está vazia (ou seja, não foi clicada antes)
        if self.tabuleiro[linha][coluna] is None:
            # Marca a célula com o jogador atual ("X" ou "O")
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.botoes[linha][coluna].config(text=self.jogador_atual)
            
            # Verifica se o jogador atual ganhou
            if self.verificar_vencedor():
                messagebox.showinfo("Jogo da Velha", f"Jogador {self.jogador_atual} ganhou!")
                self.reiniciar_jogo()  # Reinicia o jogo após uma vitória
            # Verifica se o tabuleiro está cheio (empate)
            elif all(celula is not None for linha in self.tabuleiro for celula in linha):
                messagebox.showinfo("Jogo da Velha", "Empate!")
                self.reiniciar_jogo()  # Reinicia o jogo em caso de empate
            else:
                # Alterna o jogador para o próximo turno (troca entre "X" e "O")
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
    
    def verificar_vencedor(self):
        # Verifica se há um vencedor no tabuleiro (linhas, colunas ou diagonais)
        
        # Verifica as linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] is not None:
                return True
        
        # Verifica as colunas
        for coluna in range(3):
            if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] and self.tabuleiro[0][coluna] is not None:
                return True
        
        # Verifica as diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0] is not None:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2] is not None:
            return True
        
        return False  # Se ninguém ganhou, retorna False
    
    def reiniciar_jogo(self):
        # Reinicia o jogo, limpando o tabuleiro e os botões
        self.jogador_atual = "X"  # O jogador "X" sempre começa
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]  # Limpa o tabuleiro
        # Limpa os textos dos botões na interface
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna].config(text="")

    def clicar_botao_aleatorio(self):
        # Encontra todas as células vazias
        celulas_vazias = [(linha, coluna) for linha in range(3) for coluna in range(3) if self.tabuleiro[linha][coluna] is None]
        
        if celulas_vazias:
            # Seleciona uma célula vazia aleatoriamente
            linha, coluna = random.choice(celulas_vazias)
            self.on_botao_clicado(linha, coluna)

# Cria a janela principal (root) e inicializa o jogo
root = tk.Tk()
app = JogoDaVelha(root)

# Exemplo de como clicar em um botão aleatório após 2 segundos
root.after(2000, app.clicar_botao_aleatorio)

root.mainloop()  # Inicia o loop principal da interface
