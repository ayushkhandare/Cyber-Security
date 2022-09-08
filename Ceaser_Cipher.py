from base64 import encode

alphabets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

list_alpha = alphabets.split()
key = 3

def encrypt():
    encode = []
    encode_final = []
    for i in range(len(text)) :
        for j in text[i] :
            position = list_alpha.index(j) + 1
            new_position = position + key
            new_letter = list_alpha[new_position%26 - 1]
            encode.append(new_letter)
        encode_str = ''.join(encode)
        encode.clear()
        encode_final.append(encode_str)
    return encode_final

def decrypt():
    decode = []
    decode_final = []
    for i in range(len(encrypt())) :
        for j in encrypt()[i] :
            position = list_alpha.index(j)
            new_position = position - key
            new_letter = list_alpha[new_position]
            decode.append(new_letter)
        decode_str = ''.join(decode)
        decode.clear()
        decode_final.append(decode_str)
    return decode_final


text = input("Enter word to encrypt & decrypt: ").lower()
text = text.split()


to_encrypt = input("Do you want to encrypt the give word ? (yes/no): ").lower()
if to_encrypt == 'yes' :
    encode_final_str = " ".join(encrypt())     
    print("Encrypted word: ", encode_final_str)
elif to_encrypt == 'no' :
    print("Okay")
else :
    print("Invalid Input")


to_decrypt = input("Do you want to decrypt the encrypted word ? (yes/no): ").lower()
if to_decrypt == 'yes' :
    decode_final_str = " ".join(decrypt())
    print("Decrypted word: ", decode_final_str)
elif to_decrypt == 'no' :
    print("Okay")
else :
    print("Invalid Input")
