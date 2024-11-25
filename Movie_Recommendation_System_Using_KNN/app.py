from flask import Flask, render_template, request, redirect, url_for
from recommendation import recommend_movies, recommend_similar_movies, filter_movies, add_rating
from visualization import plot_user_activity
import pandas as pd
import os

app = Flask(__name__)

# Geçerli kullanıcı ID'lerini kontrol etmek için yükleme
ratings = pd.read_csv('data/ratings.csv')
movies = pd.read_csv('data/movies.csv')
valid_user_ids = ratings['userId'].unique()

@app.route('/')
def index():
    return render_template('index.html', max_user_id=max(valid_user_ids))

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form.get('user_id')
    if not user_id or not user_id.isdigit():
        return render_template('error.html', message="Lütfen geçerli bir kullanıcı ID'si girin.")
    
    user_id = int(user_id)
    if user_id not in valid_user_ids:
        return render_template('error.html', message=f"Kullanıcı ID'si {user_id} mevcut değil.")

    recommendations = recommend_movies(user_id)
    if recommendations.empty:
        return render_template('error.html', message="Bu kullanıcı için öneri bulunamadı.")
    
    return render_template('recommendations.html', movies=recommendations)

@app.route('/similar', methods=['POST'])
def similar_movies():
    movie_title = request.form.get('movie_title')
    if not movie_title:
        return render_template('error.html', message="Lütfen geçerli bir film adı girin.")
    
    try:
        recommendations = recommend_similar_movies(movie_title)
        return render_template('recommendations.html', movies=recommendations)
    except KeyError:
        return render_template('error.html', message=f"'{movie_title}' adlı film bulunamadı.")

@app.route('/filter', methods=['POST'])
def filter_movies_route():
    genre = request.form.get('genre')
    year = request.form.get('year')
    min_rating = request.form.get('min_rating', 0)

    filtered_movies = filter_movies(genre, year, float(min_rating))
    if filtered_movies.empty:
        return render_template('error.html', message="Filtreye uyan film bulunamadı.")
    
    return render_template('recommendations.html', movies=filtered_movies)

@app.route('/rate', methods=['POST'])
def rate_movie():
    user_id = request.form.get('user_id')
    movie_id = request.form.get('movie_id')
    rating = request.form.get('rating')

    if not (user_id and movie_id and rating):
        return render_template('error.html', message="Lütfen tüm alanları doldurun.")
    
    try:
        add_rating(int(user_id), int(movie_id), float(rating))
        return render_template('success.html', message="Derecelendirme başarıyla eklendi!")
    except ValueError as e:
        return render_template('error.html', message=str(e))

@app.route('/visualize/<int:user_id>')
def visualize(user_id):
    if user_id not in valid_user_ids:
        return render_template('error.html', message=f"Kullanıcı ID'si {user_id} mevcut değil.")

    plot_path = plot_user_activity(user_id)
    return render_template('visualization.html', image_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
