def alphabet_position(text):
    final_text = []
    answer = []
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    text = [char for char in text]
    for char in text:
        char = char.lower()
        if char.isalpha():
            final_text.append(char)
    for j in final_text:
        answer.append(alphabet.index(j) + 1)

    answer = ' '.join([str(j) for j in answer])
    return answer
