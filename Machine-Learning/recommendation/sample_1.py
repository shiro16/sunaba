import numpy
from scipy.spatial.distance import cosine

def calc_item_score(target_user_index, user_rating_matrix):
    target_user_ratings = user_rating_matrix[target_user_index]
    item_similarity = numpy.zeros(len(target_user_ratings))
    for compare_user_index in range(len(user_rating_matrix)):
        compare_user_ratings = user_rating_matrix[compare_user_index]
        if compare_user_index == target_user_index:
            continue
        user_similarity = 1.0 - cosine(target_user_ratings, compare_user_ratings)
        item_similarity += user_similarity * compare_user_ratings
    return item_similarity

R = numpy.array(
    [
        [5, 3, 0, 0],
        [4, 0, 4, 1],
        [1, 1, 0, 5],
        [0, 0, 4, 4],
        [0, 1, 5, 4]
    ]
)

predict_ratings = calc_item_score(0, R)
