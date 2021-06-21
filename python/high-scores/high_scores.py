def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores)[-1]


def personal_top_three(scores):
    s = sorted(scores, reverse=True)
    return [x for i, x in enumerate(s) if i < 3]
