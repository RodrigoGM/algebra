def poly(*args):
    """
    
    f(x) = a * x + b * x**2 + c * x**3 + ...
    
    *args = (x, a, b)
    """

    if len(args) == 1:
        raise Exception("you've only entered a value for x, and no coefficients")
    
    x = args[0] # X value
    coef = args[1:]
    ##     a = args[1]
    ##     b = args[2]
    
    result = 0
    for power, c in enumerate(coef):
        result += c * (x ** (power+1))

    return result

    print(args)
    
 ###   fx =  a * b + b * (x ** 2)
###    return fx
