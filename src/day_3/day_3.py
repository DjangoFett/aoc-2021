import numpy


bit_criteria = lambda d: (sum(d) > len(d) / 2) or (sum(d) == len(d) / 2)
binary_to_decimal = lambda x: int("".join(x), 2)
transpose = lambda x: numpy.array(x).transpose()


def get_diagnostic_report(items):
    diagnostics = transpose(items)
    gamma = ["1" if bit_criteria(d) else "0" for d in diagnostics]
    epsilon = ["0" if x == "1" else "1" for x in gamma]
    return binary_to_decimal(gamma) * binary_to_decimal(epsilon)


def get_gas_reading(items, i, gas):
    if len(items) == 1:
        return binary_to_decimal([str(x) for x in items[0]])

    diagnostics = transpose(items)
    criteria = (
        bit_criteria(diagnostics[i])
        if gas == "o2"
        else not bit_criteria(diagnostics[i])
    )

    if criteria:
        return get_gas_reading(
            list(filter(lambda x: True if x[i] == 1 else False, items)), i + 1, gas
        )
    else:
        return get_gas_reading(
            list(filter(lambda x: True if x[i] == 0 else False, items)), i + 1, gas
        )


def get_o2_and_co2(items):
    return get_gas_reading(items, 0, "o2") * get_gas_reading(items, 0, "co2")
