def distance(strand_a, strand_b):

    if len(strand_a) == len(strand_b):
        counter = 0
        for unit_a, unit_b in zip(list(strand_a), list(strand_b)):
            if unit_a != unit_b:
                counter += 1
        return counter
    else:
        raise ValueError("ValueError")
