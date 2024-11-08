def word_ladder_2(start_word, target_word, word_list):
    n = len(start_word)
    word_set = set(word_list)

    queue = [[start_word]]
    used_on_level = set()
    level = 0

    if start_word in word_set:
        used_on_level.add(start_word)

    ans = []
    while queue:
        curr_path = queue.pop(0)
        curr_path_len = len(curr_path)

        if curr_path_len > level:
            level += 1
            for word in used_on_level:
                word_set.remove(word)
            used_on_level = set()

        word = curr_path[-1]
        if word == target_word:
            if not ans:
                ans.append(curr_path)
            elif len(ans[-1]) == curr_path_len:
                ans.append(curr_path)

        for i in range(n):
            temp = list(word)
            for j in range(26):
                temp[i] = chr(ord('a') + j)
                string = "".join(temp)

                if string in word_set:
                    queue.append(curr_path + [string])
                    used_on_level.add(string)

    return ans


print(word_ladder_2('lm', 'll', ["lm"]))
