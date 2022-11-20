def decrypt(secret_key, cipher_text):
    secret_key = secret_key * 1000

    # strip non alphanumeric characters
    stripped_chiper_text = remove_specials(cipher_text).replace(" ", "")

    # get plain text up to the length of ciphertext
    secret_key = secret_key[:len(stripped_chiper_text)]

    decrypted = ""
    for i in range(len(secret_key)):
        num_key = ((ord(stripped_chiper_text[i]) - ord(secret_key[i])) % 26) + 97
        char_key = chr(num_key)
        decrypted = decrypted + char_key

    return add_removed_characters(cipher_text, decrypted)

def remove_specials(text):
    cleaned = ""
    for c in text:
        if c.isalpha() or c == " ":
            cleaned += c
    return cleaned

def add_removed_characters(original, decrypted):
    o_ptr = 0
    d_ptr = 0

    while o_ptr < len(original):
        if not original[o_ptr].isalpha():
            decrypted = decrypted[:d_ptr] + original[o_ptr] + decrypted[d_ptr:]

        o_ptr += 1
        d_ptr += 1
    
    return decrypted

if __name__ == "__main__":
    key = "fuckmybrain"
    ciphertext = "Ybgbq wpl gw lto udgnju fcpp, C jybc zfu zrryolqp zfuz xjs rkeqxfrl ojwceec J uovg :)mnvze://10.10.10.17/8zb5ra10m915218697q1h658wfoq0zc8/frmfycu/sp_ptr"
    print(decrypt(key, ciphertext))