import matplotlib.pyplot as plt
import pandas as pd

ratings = pd.read_csv('data/ratings.csv')

def plot_user_activity(user_id):
    user_ratings = ratings[ratings['userId'] == user_id]
    movie_counts = user_ratings.groupby('rating')['movieId'].count()
    
    plt.figure(figsize=(10, 6))
    movie_counts.plot(kind='bar', color='skyblue', title=f'Kullanıcı {user_id} Derecelendirme Dağılımı')
    plt.xlabel('Puan')
    plt.ylabel('Film Sayısı')
    plot_path = f'static/visualization_{user_id}.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path
