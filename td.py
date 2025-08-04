def analyze_scores(scores):
    """
    Takes a list of student scores and returns:
    - average score
    - number of passing students (>= 50)
    - highest and lowest scores
    """
    if not scores:
        return {"error": "Empty score list"}

    average = sum(scores) / len(scores)
    passing = len([s for s in scores if s >= 50])
    highest = max(scores)
    lowest = min(scores)

    return {
        "average": round(average, 2),
        "passing": passing,
        "highest": highest,
        "lowest": lowest,
    }

    # return average, passing, highest, lowest
