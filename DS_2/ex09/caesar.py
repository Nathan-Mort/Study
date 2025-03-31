import sys

def encode_caesar_cipher(string, shift):
    encrypted_string = ''
    for char in string:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_string += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_string += char
    print(encrypted_string)
    
def decode_caesar_cipher(string, shift):
    encrypted_string = ''
    for char in string:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_string += chr((ord(char) - base - shift) % 26 + base)
        else:
            encrypted_string += char
    print(encrypted_string)
    
def check_args():
    if len(sys.argv) == 4:
        action = sys.argv[1]
        string = sys.argv[2]
        shift = int(sys.argv[3])

        if action == 'encode':
            encode_caesar_cipher(string, shift)
        elif action == 'decode':
            decode_caesar_cipher(string, shift)
        else:
            print('Uncorrect input')
    else:
        print('Uncorrect input')

if __name__ == '__main__':
    check_args()