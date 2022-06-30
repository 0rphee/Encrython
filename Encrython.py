import sys
from cryptography.fernet import Fernet

def crypt_text(key, text, encrypt=True):
    try:
        if encrypt:
            # if no key was provided, one will be generated
            if key == "no_key":
                key = Fernet.generate_key()
            token_w_key = Fernet(key)
            text = token_w_key.encrypt(text.encode()).decode()
            # if key for encrypting wasn't provided, it would need to be decoded
            if type(key) != str:
                key = key.decode()

        else:
            token_w_key = Fernet(key)
            text = token_w_key.decrypt(text.encode())
            text = text.decode()
    except Exception:
        return text, "Invalid key"
    return text, key

def print_results(text, key, encrypt: bool):
    if key == "Invalid key":
        print(f"{key} \nBelow is your text: \n{text}")
    else:
        en_de_crypted_str = "Encrypted" if encrypt else "Decrypted"
        print(f'{en_de_crypted_str} text: \n{text_to_print} \nKey used: \n{key}')


# assigning arguments to variables
key = sys.argv[1]
encrypt = True if sys.argv[2].lower().strip() == 'encrypt' else False
text = " ".join(sys.argv[3:])


text_to_print, key = crypt_text(key, text, encrypt=encrypt)
print_results(text_to_print, key, encrypt)
