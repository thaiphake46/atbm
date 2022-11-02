def encrypt(plaintext, k):
    result = ''

    # traverse text
    for i in range(len(plaintext)):
        char = plaintext[i]

        # encrypt uppercase character
        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)

        # encrypt uppercase character
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result


def decrypt(plaintext, k):
    result = ''
    # traverse text
    for i in range(len(plaintext)):
        char = plaintext[i]

        # encrypt uppercase character
        if char.isupper():
            result += chr((ord(char) - k - 65) % 26 + 65)

        # encrypt uppercase character
        else:
            result += chr((ord(char) - k - 97) % 26 + 97)
    return result


plaintext = input('Enter message: ')
k = -1
while k <= 0 or k > 25:
    k = int(input('Enter key (0 < key < 26): '))
result = encrypt(plaintext, k)
print('encrypt: ' + result)
print('decrypt: ' + decrypt(result, k))
