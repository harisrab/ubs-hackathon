def run_generations(payload):
    """ Given the generations params, generate gens """

    print(payload)
    print("\n\n")
    first = payload[0]

    generations = first['generations']
    colony = [int(digit) for digit in first['colony']]

    print(f"{generations=}")
    print(f"{colony=}")

    results = []

    for g in range(generations):
        weight = sum(colony)
        new_colony = []

        for i in range(len(colony) - 1):
            pair_signature = colony[i] - colony[i +
                                                1] if colony[i] > colony[i+1] else 10 - (colony[i+1] - colony[i])
            pair_signature = colony[i] - colony[i +
                                                1] if colony[i] == colony[i + 1] else pair_signature

            new_digit = (pair_signature + weight) % 10

            # new_colony += [colony[i], new_digit]
            new_colony.extend([colony[i], new_digit])

        new_colony.append(colony[-1])
        colony = new_colony

        results.append("".join(str(number) for number in colony))

        # print(f"After {g + 1} generation => {results[-1]} => Weight = {sum(colony)}")
        # print("\n\n")

        # break

    return None
