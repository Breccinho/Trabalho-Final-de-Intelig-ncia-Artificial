#Busca gulosa 
import random 

board_size = int(input("Informe o Tamanho do Tabuleiro: ")) #Tamanhho do tabuleiro a ser gerado
print("\n")

class Chessboard:
    def __init__(self, size): #Inicializando o tabuleiro vazio e seus possíveis movimentos
        self.size = size
        self.board = [[-1] * size for _ in range(size)]
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    def is_valid_move(self, x, y): # Verifica se o movimento é válido
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == -1
    
    def get_valid_moves(self, x, y): # Retorna uma lista de movimento válidos a partir da posição atual (x,y)
        valid_moves = []
        for dx, dy in self.moves:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y):
                count = 0
                for _, __ in self.moves:
                    if self.is_valid_move(new_x + _, new_y + __):
                        count += 1
                valid_moves.append((new_x, new_y, count))
        valid_moves.sort(key=lambda move: move[2])
        return valid_moves
    
    def greedy_search(self, x, y, move_count): # Verificação do algoritmo de busca gulosa
        self.board[x][y] = move_count
        if move_count == self.size ** 2 - 1:
            return True
        
        next_moves = self.get_valid_moves(x, y)
        for move in next_moves:
            new_x, new_y, _ = move
            if self.greedy_search(new_x, new_y, move_count + 1):
                return True
        
        self.board[x][y] = -1
        return False

    def solve(self, start_x, start_y): # Método chamado para implementar a solução, caso seja possível.
        if self.greedy_search(start_x, start_y, 0):
            self.print_board()
        else:
            print("Não a solução.")
    
    def print_board(self): # Imprime o tabuleiro com a solução encontrada
        print("Solução: ")
        for row in self.board:
            for move in row:
                print(f'{str(move).rjust(2):5}', end=" ")
            print()

# Posição inicial gerada aleatoriamente 
position_x = random.randint(0 , board_size-1)
position_y = random.randint(0, board_size-1)

# Criando o tabuleiro e resolvendo o passeio do cavalo
table = Chessboard(board_size)
table.solve(position_x, position_y)