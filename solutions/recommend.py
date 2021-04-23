# Uncomment the line above to load a correction to this exercise.

# Reusable tool code

def recommend(user,P,Q,k=10):
    rated_movies = np.where(~np.isnan(rating_matrix[user,:]))[0]
    pred_ratings = [[m,np.dot(nP[user,:],nQ.T[:,m])] for m in range(Q.shape[0]) if m not in rated_movies]
    top_ratings = sorted(pred_ratings, key = lambda x: x[1], reverse=True)[:k]
    
    return [df_movies[df_movies["movie_id"] == m[0]]["title"].values[0] for m in top_ratings]