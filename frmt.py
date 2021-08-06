def ul(x):
    x = list(x)
    for i in range(len(x)):
        y = x[i] + "\u0332"
        x[i] = y
    return ''.join(x)
