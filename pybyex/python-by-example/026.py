word = input("Enter a word to convert it to Pig Latin: ")
if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    word = word + "way"
else:
    word = word[1:len(word)] + word[0] + "ay"

print(word.lower())

