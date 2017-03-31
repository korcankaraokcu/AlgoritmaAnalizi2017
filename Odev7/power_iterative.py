def power(base, power):
    result = 1
    while power > 0:
        if power % 2 == 0:
            power = power / 2
            base = base * base
        else:
            power = power - 1
            result = result * base
            power = power / 2
            base = base * base
    return result
print(power(2,5))
