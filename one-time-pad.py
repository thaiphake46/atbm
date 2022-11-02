import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


MY_KEY = get_random_string(11)


def makeVernamCypher(text, key):
    """ Returns the Vernam Cypher for given string and key """
    answer = ""  # the Cypher text
    p = 0  # pointer for the key
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p == len(key):
            p = 0
    return answer


def main():
    print("\n\n---Vernam Cypher---")
    PlainText = input("Enter text to encrypt: ")
    # Encrypt
    Cypher = makeVernamCypher(PlainText, MY_KEY)
    print("Cypher text: "+Cypher)

    # Decrypt
    decrypt = makeVernamCypher(Cypher, MY_KEY)
    print("Decrypt: "+decrypt)


main()
