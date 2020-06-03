def find_words(text, search):
    
    dText   = text.split()
    dSearch = search.split()

    found_word = 0

    for text_word in dText:
        for search_word in dSearch:
            if search_word == text_word:
                found_word += 1

    if found_word == len(dSearch):
        return True
    else:
        return False

one = "reset"
two = "rest"
check = find_words(one, two)
print(check) 