def winner(names: list[str], scores: list[float]) -> str:
    if not names:
        return ""
    return names[scores.index(max(scores))]


def average(scores: list[float]) -> float:
    if len(scores) = 0:
        return 0.0
    return round(sum(scores)/len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    a = []
    n = sorted(range(len(scores)), key=lambda index:scores[index], reverse = True)
    for i in n:
        a.append(names[i])
    return a

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    a = []
    for i in range(len(names)):
        if scores[i] > avg:
            a.append(names[i])
    return a

#lkjllihkuhkuh
