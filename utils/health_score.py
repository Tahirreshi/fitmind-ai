def calculate_score(steps, sleep, heart, stress):
    score = 0

    # Steps (max 25)
    if steps >= 10000:
        score += 25
    elif steps >= 5000:
        score += 15
    else:
        score += 5

    # Sleep (max 25)
    if 7 <= sleep <= 9:
        score += 25
    elif 5 <= sleep < 7:
        score += 15
    else:
        score += 5

    # Heart Rate (max 25)
    if 60 <= heart <= 100:
        score += 25
    else:
        score += 10

    # Stress (max 25)
    if stress <= 3:
        score += 25
    elif stress <= 6:
        score += 15
    else:
        score += 5

    return score