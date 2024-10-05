def vow(v):
    if v in ['a', 'e', 'i', 'o', 'u']:
         print("The alphabet is a vowel")
    else:
        print("The alphabet is a consonant")
alpha = input("Enter your alphabet: ")
vow(alpha.lower())
