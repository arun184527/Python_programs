import numpy as np
# Rows = Users
# Columns = Products
# 0 means not rated
ratings = np.array([
    [5, 4, 0, 1, 0],   # User 1
    [4, 0, 4, 1, 2],   # User 2
    [0, 3, 4, 0, 5],   # User 3
    [5, 4, 5, 0, 1],   # User 4
    [1, 0, 2, 4, 0]    # User 5
])
users = np.array(["U1", "U2", "U3", "U4", "U5"])
products = np.array(["Phone", "Laptop", "TV", "Camera", "Headset"])
# Cosine similarity
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
# Similarity matrix
n = ratings.shape[0]
similarity = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        similarity[i][j] = cosine_sim(ratings[i], ratings[j])
print("User Similarity Matrix:\n", similarity)
# Recommend products
def recommend(user_index, top=2):
    sim_scores = similarity[user_index]
    sim_scores[user_index] = 0   # ignore self
    best_user = np.argmax(sim_scores)
    print("\nMost Similar User:", users[best_user])
    user_ratings = ratings[user_index]
    best_ratings = ratings[best_user]
    recommendations = []
    for i in range(len(products)):
        if user_ratings[i] == 0 and best_ratings[i] >= 4:
            recommendations.append(products[i])
    if recommendations:
        print("Recommended Products:", recommendations)
    else:
        print("No strong recommendations found")
# Test
user_id = 0   # U1
recommend(user_id)