import random
import pandas as pd

'''
  Funçao para alterar os ratings do usuário.
  As notas dada pelos usuários igual ou acima de 2.5 são trocadas por 'gostei'
  As notas abaixo de 2.5 são trocadas por 'não gostei'
'''
def changeStatus(ratings):
  # Alterar todos os valores abaixo de 2.5 para 0.
  ratings.loc[ratings['rating'] < 2.5, 'rating' ] = 0
  
  # Alterar todos os valores maiores ou iguais a 2.5 para 1.
  ratings.loc[ratings['rating'] >= 2.5, 'rating' ] = 1
  
  #Altera os valores 0 para 'não gostei' e 1 para 'gostei'.
  ratings['rating'] = ratings['rating'].replace(0,'não gostei')
  ratings['rating'] = ratings['rating'].replace(1,'gostei')
  
  return ratings


# Função responsável por perguntar o rating para cada filme ao usuário.
def ratingMovies(rand_movies):
  liked_list = {}
  disliked_list = {} 

  # Transforma o dataframe em uma lista. Data: [movieId,Title,Genres]
  rand_movies = rand_movies.values.tolist()
  for movie in rand_movies:
    movie[2] = movie[2].replace('|',', ')
    rating = float(input("Nota (0 a 5) do filme: "+ movie[1]+ " do genero: "+ movie[2] +"?\n"))
    #Seleciona os filmes que o usuário gostou.
    if (rating >= 2.5):
      liked_list[movie[0]] = movie[1]
    else:
      #Seleciona os filmes que ele não gostou
      disliked_list[movie[0]] = movie[1]
  #endfor
  return liked_list,disliked_list


#Função para achar a lista de usuários que gostam do mesmo filme.
def find_colabs(liked_list, ratings):
  userIds = []
  for key in liked_list.keys():
    #Para cada movieId que o usuário gostou eu procuro os UserIds que deram algum rating.
    r = ratings.loc[ratings['movieId'] == key,['userId','rating']]
    #Depois é selecionado os userIds que deram o rating 'gostei'
    r = r.loc[r['rating']=='gostei',['userId']]
    r = r.values.tolist()
    #Verifica se o userId ja foi adicionado na lista.
    for i in range (len(r)):
      if (r[i][0] not in userIds):
        userIds.append(r[i][0])
  #Retorna a lista de usuerID
  return userIds


# Função que computa os votos de acordo com o collaborative filtering.
# Retorna os 5 mais votados.
def scoreCalculator(userIds,ratings):
  score = {}
  for user in userIds:
    # Seleciona a lista de rating do usuário
    ids = ratings.loc[ratings['userId']==user,['rating','movieId']]
    #Filtra a lista por gostei.
    ids = ids.loc[ids['rating']=='gostei','movieId']
    #Filtra a lista pegando só os movieIds que o usuário gostou.
    ids = ids.values.tolist()
    for id in ids:
      #Se o movieID não foi computado, cria a instância dele e computa.
      if id not in score:
        score[id] = 1
      else:
        #Caso ele já exista, só computa.
        score[id] = score[id] +1
    #endfor
  score = list(score.items())
  score.sort(key=lambda x: x[1])
  
  #Seleciona os 5 melhores.
  recomendMovies = score[-5:]

  return recomendMovies


#Função que acha o nome/genero do filme e retorna o dataframe com as informações.
def findMovies(recomendMovies,movies,userIds):
  title = []
  genres = []
  score = []
  for i in range(len(recomendMovies)-1,-1,-1):
    # Seleciona o Title e o Genero do filme.
    res = movies.loc[movies['movieId']==recomendMovies[i][0],['title','genres']]
    # Transforma o data frame em lista para filtragem.
    res = res.values.tolist()
    title.append(res[0][0])
    genres.append(res[0][1].replace('|',', ')) 
    #Calcula o percentual dos votos. 
    percent = (recomendMovies[i][1]*100)//len(userIds)
    score.append(percent)
    i -= 1
  # Cria o data frame para indicar os filmes ao usuário.
  data = {"title":title,"genres":genres,"score(%)":score}
  df = pd.DataFrame.from_dict(data)

  return df