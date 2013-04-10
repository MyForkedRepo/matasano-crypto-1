# 7. AES in ECB Mode
# 
# The Base64-encoded content at the following location:
# 
#     https://gist.github.com/3132853
# 
# Has been encrypted via AES-128 in ECB mode under the key
# 
#     "YELLOW SUBMARINE".
# 
# (I like "YELLOW SUBMARINE" because it's exactly 16 bytes long).
# 
# Decrypt it.
# 
# Easiest way:
# 
# Use OpenSSL::Cipher; give it AES-128-ECB as the cipher.
# 
# Call "decrypt" on the cipher object or it'll think it's encrypting.
# 
# Call "update" to pass data to the cipher core; don't forget to call
# "final" when you're done, because if the buffer isn't evenly aligned,
# OpenSSL has buffered up some data to pad.


from Crypto.Cipher import AES
from base64 import b64decode

def decode_aes_ecb(text, key):
    ''' Decode an AES-128 ECB cipher '''
    c = AES.new(key, AES.MODE_ECB)
    return c.decrypt(text)

if __name__ == '__main__':
    f = open('3132853/gistfile1.txt')
    b64_text = f.read()
    text = b64decode(b64_text)

    decoded = decode_aes_ecb(text, "YELLOW SUBMARINE")
    print decoded

