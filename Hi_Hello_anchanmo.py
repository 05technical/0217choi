def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))

def binomial_probability(n, p ,k):
    return combination(n, k) * (p ** k) * ((1-p) ** (n-k))

def binomial_probability_table(n, p):
    probability = []
    for k in range(n+1):
        x = binomial_probability(n, p, k)
        probability.append(x)
        print(f"성공횟수 {k}의 확률: {x:.4f}")
    return probability


def binomial_probability_graph(n, p):
    probability = binomial_probability_table(n, p)
    max_prob = max(probability)
    height = 20

    modify_probability = []
    for prob in probability:
        modify_height = int(prob / max_prob * height)
        modify_probability.append(modify_height)

    for level in range(height, 0, -1):
        line = ""
        for modify_height in modify_probability:
            if modify_height >= level:
                line += '▮'
            else:
                line += ' '
        print(line)

    for k in range(len(probability)):
        print(f"{k:2}", end=' ')
    print()
