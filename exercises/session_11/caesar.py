ASCII_OFFSET = 97 # 'a' in ASCII and UTF-8

def caesar_cipher(plaintext, n):
    secret = ""
    for char in plaintext.lower():
        # perform ordinal shift
        shifted = (ord(char) - ASCII_OFFSET + n) % 26 + ASCII_OFFSET
        # cast shifted ordinal back to 'character'
        # add to secret
        secret += chr(shifted)
    return secret

def caesar_cipher_error_handling(plaintext, n):
    if type(plaintext) is not str:
        # parameter plaintext is not of type string, raise an exception
        # inform the user by passing an error message
        raise TypeError(f"Parameter 'plaintext' has to be str not {type(plaintext)}")
    if type(n) is not int:
        # parameter n is not of type integer, raise an exception
        # inform the user by passing an error message
        raise TypeError(f"Parameter 'n' has to be int not {type(n)}")
    secret = ""
    for char in plaintext.lower():
        # perform ordinal shift
        shifted = (ord(char) - ASCII_OFFSET + n) % 26 + ASCII_OFFSET
        # cast shifted ordinal back to 'character'
        # add to secret
        secret += chr(shifted)
    return secret
