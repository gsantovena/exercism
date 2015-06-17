import string

plaintext = string.ascii_lowercase + string.digits
ciphertext = string.ascii_lowercase[::-1] + string.digits

def encode(text):
    cipher = ''
    n = 0
    for t in text.lower():
        f = plaintext.find(t)
        
        if f >= 0:
            if n % 5 == 0 and n > 0:
                cipher += ' '

            n += 1
            cipher += ciphertext[f]

    return cipher

def decode(cipher):
    text = ''
    for c in cipher.lower():
        f = ciphertext.find(c)
        if f >= 0:
            text += plaintext[f]

    return text

if __name__ == '__main__':
    print encode('O M G')
    print encode("Truth is fiction.")
    print encode("Testing, 1 2 3, testing.")
    print decode('gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt')

