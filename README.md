# Trabalho-Final-de-Intelig-ncia-Artificial
Problema do Cavalo em Python 🐴

Este é um programa em Python que resolve o problema do cavalo, também conhecido como "O Passeio do Cavalo". O problema consiste em encontrar um caminho para que um cavalo percorra todas as casas de um tabuleiro de xadrez, passando por cada casa uma única vez, sendo esse um complexo problema estudado na área da matemática.

## Requisitos

- Python 3.x

## Como executar o programa

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Baixe o arquivo `cavalo.py` deste repositório.
3. Abra o terminal: Abra o terminal ou prompt de comando em seu sistema operacional. A forma de fazer isso pode variar dependendo do sistema operacional que você está usando. Por exemplo:

No Windows, você pode pressionar Win + R, digitar cmd e pressionar Enter.

No macOS, você pode abrir o Launchpad, digitar "Terminal" na barra de busca e clicar no aplicativo "Terminal".

No Linux, você pode pressionar Ctrl + Alt + T para abrir o terminal.

4. Navegue até o diretório do arquivo: Use o comando cd para navegar até o diretório onde o arquivo cavalo.py está localizado. Por exemplo, se você salvou o arquivo na área de trabalho, pode usar o seguinte comando no terminal:

   ```bash
   python cavalo.py
   ```

5. O programa irá exibir o tabuleiro de xadrez com o caminho percorrido pelo cavalo.

## Funcionamento do programa

O programa utiliza a abordagem de busca em profundidade para encontrar um caminho válido para o cavalo percorrer todas as casas do tabuleiro.

O tabuleiro é representado por uma matriz NxN, onde cada casa é identificada por um par de coordenadas (linha, coluna). O cavalo começa em uma casa inicial (definida no código) e, a partir dessa posição, o programa tenta mover o cavalo para uma casa vizinha que ainda não tenha sido visitada. Esse processo continua até que todas as casas tenham sido visitadas ou não haja mais movimentos válidos.

O programa exibirá o tabuleiro com o caminho percorrido pelo cavalo, indicando a ordem em que as casas foram visitadas.

## Algoritmos utilizados:

- Algoritmo Genético
- Heurística de busca gulosa
- Heurística AML

## Autores 
	Anna Gabriela Mota
	Gabriel Brecciani Rebolla



).
