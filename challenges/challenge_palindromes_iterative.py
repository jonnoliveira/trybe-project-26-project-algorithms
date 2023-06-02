def is_palindrome_iterative(word):
    word = word.lower()  # converte para deixar todas as letras iguais

    if len(word) == 0:
        return False

    # percorre a palavra e verifica se a primeira letra é diferente da ultima
    for index in range(len(word)):
        # "AGUA" -> A != letra[4 - 0 - 1] -> A != letra[3] -> A != A -> False
        # "AGUA" -> G != letra[4 - 1 - 1] -> G != letra[2] -> G != U -> True
        if word[index] != word[len(word) - index - 1]:
            print(word[index], word[len(word) - index - 1])
            return False
    return True


# print(is_palindrome_iterative("AGUA"))
