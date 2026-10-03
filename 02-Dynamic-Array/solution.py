def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    
    for q, x, y in queries:
        idx = (x ^ lastAnswer) % n
        if q == 1:
            arr[idx].append(y)
        elif q == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
            
    return answers
