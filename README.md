# Território da Nlogônia
--------------
## Problem description

A Nlogônia é um país tropical, com muitas belezas naturais internacionalmente famosas; dentre elas, encontram-se as belas praias que compõem o arquipélago do país, que todo verão recebem milhões de turistas estrangeiros.

O Ministério do Turismo da Nlogônia está preparando o país para a chegada dos turistas, mas para fazer seu planejamento, precisa saber a extensão da costa nlogônica. Para isso, ele gerou um mapa que divide o território nacional em vários quadrados, que podem ser ocupados por água ou por terra; considera-se que um quadrado é parte da costa nlogônica se ele é um quadrado ocupado por terra que tem um lado em comum com um quadrado ocupado por água.

Na figura abaixo, (a) mostra um trecho do mapa gerado e (b) mostra os quadrados do trecho dado que são costa.


Como a Nlogônia é um país muito grande, o ministro do turismo pediu que você escrevesse um programa que, dado o mapa da Nlogônia, determina a extensão da costa nlogônica.

Entrada

A primeira linha da entrada contém dois inteiros M e N indicando, respectivamente, o número de linhas e o número de colunas do mapa. Cada uma das M linhas seguintes contém N caracteres: um caractere '.' indica que aquele quadrado do território é ocupada por água; um caractere '#' indica que aquele quadrado do território é ocupada por terra.

Considere que todo o espaço fora da área do mapa é ocupado por água.

Saída

Seu programa deve imprimir uma única linha contendo um único inteiro, indicando quantos quadrados do território fazem parte da costa da Nlogônia.

Restrições

1 ≤ M,N ≤ 1000
Exemplos

```ssh
Entrada
5 5

.....
..#..
.###.
..#..
.....

Saída
4

Entrada
10 10

..........
.....###..
....#####.
.#...##...
..........
.......##.
.##.......
..##......
..###.....
..#####...

Saída
22
```

## Installation
### From source
First, [download](https://github.com/dayanepabla/territorio/archive/master.zip) or clone this repository as follow

```ssh
$ git clone https://github.com/dayanepabla/territorio.git
$ cd territorio/
```
Execute the command below to run the program
```sh
$ bin/territorio
```
Enjoy! ;)

## Author
Dayane Pabla - <dayanepabla@gmail.com>
