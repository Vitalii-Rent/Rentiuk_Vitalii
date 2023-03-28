def first_non_repeating_letter(word: str):
    for letter in word:
        num = word.lower().count(letter.lower())
        if num == 1:
            return letter
    return None