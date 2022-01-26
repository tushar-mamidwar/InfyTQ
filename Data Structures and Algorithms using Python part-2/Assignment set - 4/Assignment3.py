# lex_auth_0127667326864670723497


def find_unknown_words(text, vocabulary):
    text = text.split()
    new_words = []
    for word in text:
        if not word in vocabulary:
            new_words.append(word)
    if new_words:
        return set(new_words)
    else:
        return -1


# Pass different values of text and vocabulary to the function and test your program
text = "The sun rises in the east and sets in the west."
vocabulary = ["sun", "in", "rises", "the", "east"]
unknown_words = find_unknown_words(text, vocabulary)
print("The unknown words in the file are:", unknown_words)
