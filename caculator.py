__author__ = 'Nancy'


def evaluate(expr):
    pass


if __name__ == "__main__":

    exprs = [
        ('3*(4+5)', 27),
        ('4+5', 9),
        ('8/4 - 2', 0)
    ]

    for e, result in exprs:
        if evaluate(e) != result:
            print("Failed:", e, result)

