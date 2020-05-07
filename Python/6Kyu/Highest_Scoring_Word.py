# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet.

def high(x):
    x_list = list(x.split(' '))
    high_score_word = ''

    high_score = 0
    for w in x_list:
        word_score = 0
        for c in w:
            val = ord(c) - 96
            word_score += val
        if word_score > high_score:
            high_score = word_score
            high_score_word = w

    return high_score_word

# Community Solution
#
# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
