name = "harsh singhal"

word_list = name.split()
for word in word_list:
    reverse_word = " "
    for char in word:
        reverse_word = char + reverse_word
    print(reverse_word,end = '')