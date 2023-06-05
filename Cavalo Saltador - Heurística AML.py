#Heurística AML
import random
#Tamanho ideial de tabuleiro: 8x8
size = int(input("Informe o tamanho do tabuleiro: ")) # Define o tamanho do labirinto
print("\n")

move_x = [0, 2, 1, -1, -2, -2, -1, 1, 2] # Movimentos possíveis de horizontalmente
move_y = [0, 1, 2, 2, 1, -1, -2, -2, -1] # Movimentos possíveis verticalmente
start_board = [[0] * (size+1) for _ in range(size+1)] # Inicia o tabuleiro 
n = 0

def Print(): # Imprime o tabuleiro solução
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f'{start_board[i][j]:5}', end='')
        print()
    print()

def NextMove(i, x, y): # Verifica o próximo movimento possível
    global n
    min_moves = size + 1
    next_x = -1
    next_y = -1
    for k in range(1, size+1):
        u = x + move_x[k]
        v = y + move_y[k]
        if 1 <= u <= n and 1 <= v <= n and start_board[u][v] == 0:
            moves = CountNextMoves(u, v)
            if moves < min_moves:
                min_moves = moves
                next_x = u
                next_y = v
    return next_x, next_y

def CountNextMoves(x, y): # Conta os movimentos possíveis a partir de uma direção 
    count = 0
    for k in range(1, size+1):
        u = x + move_x[k]
        v = y + move_y[k]
        if 1 <= u <= n and 1 <= v <= n and start_board[u][v] == 0:
            count += 1
    return count

def TryNextMove(i, x, y, sucess): # Realiza a busca para encontrar o caminho do cavalo 
    global n
    sucess[0] = False
    start_board[x][y] = i
    if i == n * n:
        sucess[0] = True
        return
    next_x, next_y = NextMove(i, x, y)
    if next_x != -1 and next_y != -1:
        TryNextMove(i+1, next_x, next_y, sucess)
        if not sucess[0]:
            start_board[next_x][next_y] = 0

if __name__ == '__main__':
    q = [False] # Lista utilizada para indicar se um caminho é válido 
   
    n = size
    for i in range(1, n+1): # Imprime o tabuleiro, inicializando as posições com valor 0 
        for j in range(1, n+1):
            start_board[i][j] = 0
            
    #Define a posição inicial 
    i = random.randint(0, size-1) 
    j = random.randint(0, size-1)

    start_board[i][j] = [0][0]
    TryNextMove(2, i, j, q)
    if q[0]:
        Print()
    else:
        print("Caminho não encontrado")
