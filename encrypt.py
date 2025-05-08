def main():
    #only accept integers
    inp1 = int(input("enter first number for encryption: "))
    inp2 = int(input("enter second number for encryption: "))
    encryption(inp1,inp2)
    decryption(inp1, inp2)
    if(check_files()):
        print("File decrypted successfully")
    else:
        print("File decryption failed")

def check_files():
    file1 = open("raw_text.txt", "r")
    file2 = open("decrypted_text.txt", "r")
    file_content_1 = file1.read()
    file_content_2 = file2.read()
    return file_content_1 == file_content_2


def encryption(val1, val2):
    write_file = open("encrypted_file.txt", "w")
    read_file = open("raw_text.txt", "r")
    content = read_file.read()
    for letter in content:
        letter_ascii = ord(letter)
        if letter == letter.lower():
            if letter_ascii in range(ord('a'), ord('m') + 1):
                encrypted_letter = chr(((letter_ascii - ord('a') + (val1 * val2)) % 13) + ord('a'))

            elif letter_ascii in range(ord('n'), ord('z') + 1):
                encrypted_letter = chr(((letter_ascii - ord('n') - (val1 + val2)) % 13) + ord('n'))

           # special chars and numbers also fall into this if statement
            else:
                encrypted_letter = letter
        elif letter == letter.upper():
            if letter_ascii in range(ord('A'), ord('M') + 1):
                encrypted_letter = chr(((letter_ascii - ord('A') - val1) % 13) + ord('A'))
            elif letter_ascii in range(ord('N'), ord('Z') + 1):
                encrypted_letter = chr(((letter_ascii - ord('N') + val2**2) % 13) + ord('N'))



        write_file.write(encrypted_letter)
    read_file.close()
    write_file.close()

def decryption(val1, val2):
    decrypt_file = open("encrypted_file.txt", "r")
    content_to_decrypt = decrypt_file.read()
    decrypt_write_file = open("decrypted_text.txt","w")
    for letter in content_to_decrypt:
        letter_ascii = ord(letter)
        if letter == letter.lower():
            if letter_ascii in range(ord('a'), ord('m') + 1):
                decrypted_letter = chr(((letter_ascii - ord('a') - (val1 * val2)) % 13) + ord('a'))

            elif letter_ascii in range(ord('n'), ord('z') + 1):
                decrypted_letter = chr(((letter_ascii - ord('n') + (val1 + val2)) % 13) + ord('n'))

           # special chars and numbers also fall into this if statement
            else:
                decrypted_letter = letter
        elif letter == letter.upper():
            if letter_ascii in range(ord('A'), ord('M') + 1):
                decrypted_letter = chr(((letter_ascii - ord('A') + val1) % 13) + ord('A'))
            elif letter_ascii in range(ord('N'), ord('Z') + 1):
                decrypted_letter = chr(((letter_ascii - ord('N') - val2**2) % 13) + ord('N'))

        decrypt_write_file.write(decrypted_letter)
    decrypt_file.close()
    decrypt_write_file.close()


if __name__ == "__main__":
    main()