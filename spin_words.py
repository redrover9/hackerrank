def spin_words(sentence):
    words = sentence.split()
    scrambled_sentence = []
    for word in words:
        if len(word) < 5:
            scrambled_sentence.append(word)
        else:
            word = word[::-1]
            scrambled_sentence.append(word)
    scrambled_sentence = ' '.join(scrambled_sentence)
    return scrambled_sentence
