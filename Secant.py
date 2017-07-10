# John Berkley
# CS 301
# 7/8/2017

from math import cosh, fabs


def secant(func, x0, x1, e, true_value):
    for n in range(100):
        x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
        print('Iteration: {} ; Current Value: {} ; Function Value: {}'.format(n, x2, func(x2)))
        print('\tRelative Error: {} ; True Error: {}'.format(fabs((x2 - x1) / x2), (fabs(true_value - x2) / true_value)))
        if fabs((x2 - x1) / x2) < e:
            print('\nConverged To Root\n')
            return
        else:
            x0 = x1
            x1 = x2


def f(x):
    return (2 * (x ** 3)) - (11.7 * (x ** 2)) + (17.7 * x) - 5


def g(x):
    return x + 10 - (x * cosh(50 / x))


secant(f, 0, 1, .01, 0.3651)
secant(f, 1, 2, .01, 1.92174)
secant(f, 3, 4, .01, 3.56316)

secant(g, 120, 130, .01, 126.632)
