"""mimic practice"""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx)"""
    if letter_idx >= len (my_words):
        return ("Index too high")
    #If we made it here, that means the letteR_idx is valid
    return my_words[letter_idx]

mimic_letter("hi", 1)

#or

print(mimic_letter("hi", 1))