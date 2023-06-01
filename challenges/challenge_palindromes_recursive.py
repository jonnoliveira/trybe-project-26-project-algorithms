def is_palindrome_recursive(word, low_index, high_index):
    word = word.lower()  # converte para deixar todas as letras iguais

    if len(word) == 0:  # verifica se a palavra é vazia
        return False

    if (
        word[low_index] != word[high_index]
    ):  # verifica se a primeira e a ultima letra são diferentes
        return False

    # verifica se o indice da primeira letra é maior ou igual ao indice da
    # ultima letra para saber se a palavra é palindroma
    if low_index >= high_index:
        return True

    return is_palindrome_recursive(
        word, low_index + 1, high_index - 1
    )  # chama a função novamente para verificar as proximas letras


# print(is_palindrome_recursive("ana", 0, 2))
