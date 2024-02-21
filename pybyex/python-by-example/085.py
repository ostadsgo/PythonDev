name = input("Enter your name: ")

vowels_count = 0

for ch in name:
    if ch in "aeiou":
        vowels_count += 1


print("You name have", vowels_count, "vowels.")

