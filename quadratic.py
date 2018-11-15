def poly(x, *coefs):
    """
    
    f(x) = a * x + b * x**2 + c * x**3 + ...
    
    *args = (x, a, b)
    """

    if len(coefs) == 0:
        raise Exception(
            "you've not provided any coefficients")

    result = x * 0
    for power, c in enumerate(coefs):
        result += c * (x**(power + 1))

    return result

    print(args)

