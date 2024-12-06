user_text_1 = input("Enter first word: ")
user_text_2 = input("Enter second word: ")

lower_text_1 = user_text_1.lower()
lower_text_2 = user_text_2.lower()

check_text_1 = []
check_text_2 = []

for char in lower_text_1:
    if char != " ":
        check_text_1.append(char)
        check_text_1.sort()

for char in lower_text_2:
    if char != " ":
        check_text_2.append(char)
        check_text_2.sort()

if check_text_1 == check_text_2:
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")

