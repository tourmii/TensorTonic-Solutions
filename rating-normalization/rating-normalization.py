def rating_normalization(matrix: list) -> list:
    """
    Returns the mean-centered user-item matrix.
    """
    # Write code here
    res = []
    for user in matrix:
        non_zero_ratings = [rating for rating in user if rating != 0]
        mean_user = sum(non_zero_ratings) / len(non_zero_ratings) if non_zero_ratings else 0
        for i in range(len(user)):
            if user[i] != 0:
                user[i] -= mean_user
        res.append(user)
    return res