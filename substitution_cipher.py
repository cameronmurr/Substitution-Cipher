alphabet = "1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
key =      "/.,mnbvcxz';lkjhgfdsa\\][poiuytrewq=-0987654321?><MNBVCXZ\":LKJHGFDSA|}{POIUYTREWQ+_)(*&^%$#@! "

def encrypt(message):
    result=""

    for letter in message:
        loc=alphabet.find(letter)
        result+=key[loc]
    return result

def decrypt(message):
    result=""
    for letter in message:
        loc=key.find(letter)
        result +=alphabet[loc]
    return result


unencrypted_message = "! Inititate Pentagon hack #$%^&*% ':KFLHSFJ:Gdrtfhgln.;' Success!!!"
encrypted_message = encrypt(unencrypted_message)
decrypted_message=decrypt(encrypted_message)
print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
