import random


def monte_carlo(n, r):
    """
    In this procedure the domain of inputs is the square that circumscribes the quadrant.
    We generate a large amount of random inputs by scattering points over the square,
    then perform a computation on each input (test whether it falls within the quadrant).
    Aggregating the results yields our final result, the approximation of π.

    1. Draw a square, then inscribe a quadrant within it
    2. Uniformly scatter a given number of points over the square
    3. Count the number of points inside the quadrant, i.e. having a distance from the origin of <= than the radius
    4. The ratio the inside-count / the total-sample-count is an estimate of the ratio of the two areas, π / 4
    5. Multiply the result by 4 to estimate π.

    :param n: number of random tests
    :param r: radius of circle
    :return: estimation of π using the Monte Carlo method (3 digits after decimal point)
    """

    pi_counter = 0

    for _ in range(n):
        x = random.uniform(0, 1) * r
        y = random.uniform(0, 1) * r
        if x ** 2 + y ** 2 <= r ** 2:  # Pythagor's theorem
            pi_counter += 1

    return round((pi_counter / n) * 4, 3)  # return rounded result


print(monte_carlo(1000000, 5))  # returns 3.141 most of the time (π = 3.1415926535)
