import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import openai

# Carregar o dataset
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

# Criar a matriz de utilizadores e filmes
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
user_movie_matrix.fillna(0, inplace=True)

# Calcular a similaridade do coseno entre os utilizadores
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

openai.api_key = 'YOUR_OPENAI_API_KEY'

def recommend_movies(user_id, num_recommendations=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:num_recommendations+1]
    similar_user_movies = user_movie_matrix.loc[similar_users]
    movie_recommendations = similar_user_movies.mean().sort_values(ascending=False).index
    return movie_recommendations[:num_recommendations]

def get_movie_details(movie_id):
    movie = movies[movies['movieId'] == movie_id]
    return movie['title'].values[0], movie['genres'].values[0]

def llm_recommendation(user_id, num_recommendations=5):
    movie_ids = recommend_movies(user_id, num_recommendations)
    recommendations = []

    for movie_id in movie_ids:
        title, genres = get_movie_details(movie_id)
        prompt = f"Filme: {title}\nGêneros: {genres}\nO que você acha deste filme?"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        
        recommendation = response.choices[0].text.strip()
        recommendations.append({
            'title': title,
            'genres': genres,
            'recommendation': recommendation
        })

    return recommendations