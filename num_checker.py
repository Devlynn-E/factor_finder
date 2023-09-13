def get_factors(to_factor):
    factors_list = []

    limit = int(to_factor ** 0.5)

    for item in range(1, limit + 1):
        result = to_factor % item
        factor_1 = to_factor // item

        if result == 0:
            result.append(factors_list)


question = int(input(get_factors("num? ")))
