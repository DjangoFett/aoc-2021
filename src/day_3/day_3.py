import numpy


def bit_criteria(d):
    return (sum(d) > len(d) / 2) or (sum(d) == len(d) / 2)


def get_diagnostic_report(items):
    diagnostics = numpy.array(items).transpose()
    gamma = ["1" if bit_criteria(d) else "0" for d in diagnostics]
    epsilon = ["0" if x == "1" else "1" for x in gamma]
    decimal = lambda x: int("".join(x), 2)
    return decimal(gamma) * decimal(epsilon)


def get_gas_reading(items, i, gas):
    if len(items) == 1:
        return int("".join([str(x) for x in items[0]]), 2)

    diagnostics = numpy.array(items).transpose()
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
