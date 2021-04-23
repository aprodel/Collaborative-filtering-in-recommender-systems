# Uncomment the line above to load a correction to this exercise.

# Reusable tool code

def predict_rating(user,train_set,item,similarity='pearson',k=100):
    
    mean_rating = np.nanmean(np.delete(user,item))
    
    similarities = []
    if similarity == 'pearson':
        similarities = [(u,pearson_similarity(user,train_set[u,:],target_item=item)) for u in range(train_set.shape[0])]
    if similarity == 'cosine':
        similarities = [(u,cosine_similarity(user,train_set[u,:],target_item=item)) for u in range(train_set.shape[0])]
        
    similarities = sorted(similarities, key=lambda x: x[1],reverse=True)[:k]

    sum_similarities = 0
    pred = 0
    for u,s in similarities:
        rating = train_set[u,item]
        if ~np.isnan(rating):
            pred += (rating - np.nanmean(train_set[u,:])) * s
            sum_similarities += s
    
    if sum_similarities != 0:
        pred /= sum_similarities
    
    return pred+mean_rating
    