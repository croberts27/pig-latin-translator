# get sentence from user
original = input("Hello! Please provide a sentence you would like converted into Pig Latin: ").strip().lower()

# split  sentence into words
words = original.split()

# loop through words and convert to pig latin

new_words = []
# if it starts with a vowel, just add "yay"
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:  # otherwise, move the first consonant cluster to the end, and add "ay"
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
# merge words back together into a sentence
output = " ".join(new_words)

# output pig latin string
print(output)