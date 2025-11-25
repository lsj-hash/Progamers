def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    slopes = [
        (y[1]-y[0])/(x[1]-x[0]), (y[3]-y[2])/(x[3]-x[2]),
        (y[2]-y[0])/(x[2]-x[0]), (y[3]-y[1])/(x[3]-x[1]),
        (y[3]-y[0])/(x[3]-x[0]), (y[2]-y[1])/(x[2]-x[1])
    ]
    return 1 if slopes[0]==slopes[1] or slopes[2]==slopes[3] or slopes[4]==slopes[5] else 0
