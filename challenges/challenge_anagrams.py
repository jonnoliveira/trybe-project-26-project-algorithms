def order_word(list_letters):
    # verifica o tamanho da lista
    list_length = len(list_letters)
    if list_length <= 1:
        return list_letters

    # identifica o elemento do meio
    pivot = list_letters[list_length // 2]

    left = []
    equal = []
    right = []

    # compara cada letra da lista com o pivot e ordena de acordo com o tamanho
    for char in list_letters:
        if char < pivot:
            left.append(char)
        elif char == pivot:
            equal.append(char)
        else:
            right.append(char)

    return order_word(left) + equal + order_word(right)


def is_anagram(first_string, second_string):
    # lista com todas as letras
    first_letters_list = list(first_string.lower())
    second_letters_list = list(second_string.lower())

    # cria uma string ordenada
    first = "".join(order_word(first_letters_list))
    second = "".join(order_word(second_letters_list))

    # verifica se as strings são iguais e se não estão vazias
    if first == second and first != "" and second != "":
        return (first, second, True)
    else:
        return (first, second, False)


# print(is_anagram("", ""))
