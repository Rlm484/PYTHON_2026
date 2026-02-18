# Write a program that will loop over a word the user has entered and print ONLY the vowels.
# Store the user's input in a variable first.

#VARIABLES
word = input('Type a word!: ')
vowels = 'aeiou'
vowelword = ''

#CODE
for i in word.lower():
    if i in vowels:
        vowelword += i

print(vowelword)