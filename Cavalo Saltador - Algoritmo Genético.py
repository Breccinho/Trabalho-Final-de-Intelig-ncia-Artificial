#Algoritmo Genético
#Solução: 64 movimentos em um tabuleiro 8x8

import random 
import time 
import copy

def limit_board(limit): #Limita o tamanho máximo de tabuleiro até 16x16
    while True:
        valuer = int(input("Informe o tamanho do Tabuleiro ({}-16): ".format(limit)))
        if limit <= valuer <= 16:
            return valuer
        print("Tabuleiro inválido. Informe um tamanho entre 1 a 16")

table = limit_board(1) #tamanho da tabela (N x N)

def createTable(rows=table, columns=table, zeroes=True): #criar as tabelas em forma de vetores
    if zeroes: #se zeroes == true
        return [[0 for i in range(columns)] for j in range(rows)]#valores da geração
    else:
        return [[random.randint(0, 10) for i in range(columns)] for j in range(rows)]#retorna uma tabela de prioridade randomica

num_generation = int(input("Quantidade de gerações: "))#quantidade de geração
population_size = int(input("Tamanho da população: ")) #numero de individuo da população

class Start_Table():
    def __init__(self):
        self.priority_table = createTable(zeroes = False)#chama a criação da tabela de prioridade
        self.setDefault()

    def setDefault(self):
        self.moves = 0 #armazena quantidade de movimento realizados ate momento
        self.path = [] # o caminho do individuo pelo tabuleiro
        self.table = createTable()# cria um tabuleiro de prioridades
        self.position = (0, 0) #posição inicial 
        self.table[0][0] = 1 # Posição visitadas no tabuleiro

    def nextMoves(self):# gera os possiveis caminhos
        moves = []
        knight_moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        x, y = self.position
        for (dx, dy) in knight_moves:
            if x + dx < 0 or y + dy < 0:
                continue
            try:
                if self.table[x + dx][y + dy] == 0:
                    moves.append((x + dx, y + dy))
            except IndexError:
                continue

        return moves

    def getBestMove(self, moves):#analisa qual tem maior prioridade no codigo ou seja qual individuo possui o maior valor								 
        bestValue = float('-inf')
        bestMove = self.position
        for (x, y) in moves:
            if self.priority_table[x][y] > bestValue:
                bestValue = self.priority_table[x][y]
                bestMove = (x, y)

        return bestMove

    def moveTo(self, position):#movimenta a tabela
        x, y = position
        self.path.append(position)
        self.position = position
        self.moves += 1
        self.table[x][y] = self.moves + 1

    def run(self):# Executado até o indíviduo não obter nenhum movimento possível em sua lista de nextMoves,
				    # Encerrando a incrementação de novos movimentos
        self.setDefault()
        while self.nextMoves():
            moves = self.nextMoves()
            bestMove = self.getBestMove(moves)
            self.moveTo(bestMove)

    def mutation(self): # Realiza as mutações 
        x = random.randint(0, table - 1)
        y = random.randint(0, table - 1)
        self.priority_table[x][y] = random.randint(0, 10)
        self.run()

    def printTable(self): 
        for i in range(0, table):
            for j in range(0, table):
                print(repr(self.table[i][j]).rjust(3), end=' ')
            print()

    def printPriorityTable(self): 
        for i in range(0, table):
            for j in range(0, table):
                print(repr(self.priority_table[i][j]).rjust(3), end=' ')
            print()

    def __add__(self, other):#divida tabela em dois  e junta
        genetic = copy.deepcopy(self)
        for i in range(0, int(table / 2)):
            for j in range(0, table):
                genetic.priority_table[i][j] = other.priority_table[i][j]

        genetic.run()
        return genetic
    
class Population(): # Gera a população
    def __init__(self):
        self.games = []
        self.best_table = []
        self.worstSolutions = []

        for i in range(population_size):
            g = Start_Table()
            self.games.append(g)

    def run(self): # Percorre o tabuleiro
        for table in self.games:
            table.run()

        self.best_table.append(self.getbestSolution())
        self.worstSolutions.append(self.getworstSolution())

        print("({0}, {1})".format(self.best_table[-1].moves, self.worstSolutions[-1].moves))

    def getbestSolution(self): #armazena melhor Tabuleiro
        bestSolution = self.games[0]
        for game in self.games:
            if game.moves > bestSolution.moves:
                bestSolution = game

        return bestSolution

    def getworstSolution(self): #armazena pior Tabuleiro
        worstSolution = self.games[0]
        for game in self.games:
            if game.moves < worstSolution.moves:
                worstSolution = game

        return worstSolution

    def cross(self):
        pass

    def nextGeneration(self): # cria a próxima geração 
        new_generation = []
        for i in range(population_size):
            i = random.randint(0, population_size - 1)
            j = random.randint(0, population_size - 1)

            new_generation.append(self.games[i] + self.games[j])
            new_generation.append(self.games[j] + self.games[i])

            new_generation[-1].mutation()

        self.games = new_generation
        self.games[0] = self.best_table[-1]

if __name__ == '__main__':
    start = time.time()

    p = Population()

    for i in range(num_generation):
        p.run()
        p.nextGeneration()

    x = [i for i in range(num_generation)]
    y = []
    z = []

    for result in p.best_table:
        y.append(result.moves)

    for result in p.worstSolutions:
        z.append(result.moves)

    end = time.time()
    print(end - start)
print('\nGerações')
print(x)
print('\nMelhores Tabuleiro')
print(y)
print('\nPiorar Tabuleiro')
print(z)

bestSolution = p.best_table[-1]
print("\nTabela Prioritária")
bestSolution.printPriorityTable()
print("\nTabela Resultante")
bestSolution.printTable()