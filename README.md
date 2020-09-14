# Collaborative Filtering

O projeto proposto é um trabalho acadêmico da disciplina comércio eletrônico ministrada pelo professor Dr. Filipe Mutz.

## O Projeto
 
Para este projeto, será utilizada a base de dados [MovieLens Small](https://grouplens.org/datasets/movielens/latest/) (a base de 1MB) . O projeto consiste em implementar o algoritmo de collaborative filtering apresentado no vídeo “Fundamentos de Sistemas de Recomendação”. O programa deve solicitar que o usuário diga se gostou ou não de 10 filmes escolhidos aleatoriamente. Em seguida, o programa deve sugerir 5 filmes usando
o algoritmo de collaborative filtering. Tanto ao perguntar as notas dos filmes para os usuários, quanto
ao exibir as recomendações, exiba o título e o gênero do filme.

Observação: na base de dados, as avaliações dos filmes são notas de 0 a 5. Transforme as notas
menores que 2.5 em “não gostou” e notas maiores ou iguais a 2.5 em “gostou”.

## Como rodar o projeto. 
O projeto foi desenvolvido na plataforma collab research, utilizando a linguagem de programção python na versão 3+. Foi utilizado a biblioteca Pandas que é uma ótima opção para data science. Caso queira rodar o projeto, certifique-se que você possui a biblioteca pandas instalada na sua máquina.

```console
    python3 main.py
```

[collab research](https://colab.research.google.com/drive/1zxXyTh5cxKEuKH4F-pJg9RQ7KbNB39o8?usp=sharing) - Projeto executado.

## Collaborative Filtering Algorithm

A técnica de filtragem colaborativa consiste em filtrar os items que o usuário possa gostar com base em 
reações de usuários semelhantes[1](https://realpython.com/build-recommendation-engine-collaborative-filtering/#:~:text=Remove%20ads-,What%20Is%20Collaborative%20Filtering%3F,similar%20to%20a%20particular%20user.). 


