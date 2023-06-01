def find_duplicate(numbers):
    duplicated_numbers = count_duplicate(numbers)

    # verifica se a lista é um dicionário ou booleano
    if not duplicated_numbers:
        return False

    # percorrendo o dicionário (objeto) de números duplicados
    for number, count in count_duplicate(numbers).items():
        # verificando se o número se repete mais de uma vez
        if count > 1:
            return number

    return False


def count_duplicate(numbers):
    duplicated_number = {}

    # percorrendo a lista de números
    for number in numbers:
        # verifica se o número é um inteiro e se é maior que 0
        if not isinstance(number, int) or number < 0:
            return False

        # verifica se o número já existe no dicionário (objeto)
        if number in duplicated_number:
            duplicated_number[number] += 1
        else:
            duplicated_number[number] = 1

    return duplicated_number


print(find_duplicate([2, 3, 1, 3, 3]))
