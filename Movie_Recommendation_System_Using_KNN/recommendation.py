import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

ratings = pd.read_csv('data/ratings.csv')
movies = pd.read_csv('data/movies.csv')

def recommend_movies(user_id, num_recommendations=5):
    user_ratings = ratings[ratings['userId'] == user_id]
    rated_movies = user_ratings['movieId'].unique()

    similar_users = ratings[~ratings['movieId'].isin(rated_movies)]
    top_movies = similar_users.groupby('movieId')['rating'].mean().sort_values(ascending=False)

    recommended_movies = movies[movies['movieId'].isin(top_movies.index[:num_recommendations])]
    return recommended_movies[['movieId', 'title', 'genres']]

def recommend_similar_movies(movie_title, num_recommendations=5):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    similar_movies_indices = [i[0] for i in sim_scores[1:num_recommendations+1]]
    return movies.iloc[similar_movies_indices][['title', 'genres']]

def filter_movies(genre=None, year=None, min_rating=0):
    filtered_movies = movies
    if genre:
        filtered_movies = filtered_movies[filtered_movies['genres'].str.contains(genre, case=False)]
    if year:
        filtered_movies = filtered_movies[filtered_movies['title'].str.contains(f'({year})', regex=True)]
    return filtered_movies

def add_rating(user_id, movie_id, rating):
    new_rating = pd.DataFrame([[user_id, movie_id, rating]], columns=['userId', 'movieId', 'rating'])
    new_rating.to_csv('data/ratings.csv', mode='a', header=False, index=False)
