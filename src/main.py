import random
import pandas as pd
from algorithms import *



# Cria o data frame de ratings: userId,rating,timestamp.
ratings = pd.read_csv('ratings.csv')
# Cria o data frame de filmes: movieId,title,Genres.
movies = pd.read_csv('movies.csv')

#Altera os ratings - Gostei, não gostei
ratings = changeStatus(ratings)

#Seleciona 10 filmes aleatórios.
rand_movies = movies.sample(n=10)

liked_list,disliked_list = ratingMovies(rand_movies)

#Acha os usuários que gostaram dos mesmos filmes. 
#Nota - Para cada filme, foi selecionado os usuários que gostaram. O resultado é a lista de todos os usuarios 
#que gostaram dos filmes.
userIds = find_colabs(liked_list,ratings)

# Aplicando o collaborative filtering
score = scoreCalculator(userIds,ratings)

# Criação do data frame com as informações dos filmes.
df = findMovies(score,movies,userIds)

print(df)