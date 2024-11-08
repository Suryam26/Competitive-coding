def word_ladder_length(start_word, target_word, word_list):
    n = len(start_word)
    word_set = set(word_list)

    queue = [(start_word, 1)]
    if start_word in word_set:
        word_set.remove(start_word)

    while queue:
        node, dist = queue.pop(0)

        if node == target_word:
            return dist

        for i in range(n):
            temp = list(node)
            for j in range(26):
                temp[i] = chr(ord('a') + j)
                string = "".join(temp)

                if string in word_set:
                    word_set.remove(string)
                    queue.append((string, dist + 1))

    return 0


print(word_ladder_length('kk', 'ji',
                         ["kj", "ij", "ik", "ji", "kk", "jj", "ki"]))
