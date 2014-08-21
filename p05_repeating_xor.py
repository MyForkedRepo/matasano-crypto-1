# 5. Repeating-key XOR Cipher
# 
# Write the code to encrypt the string:
# 
#   Burning 'em, if you ain't quick and nimble
#   I go crazy when I hear a cymbal
# 
# Under the key "ICE", using repeating-key XOR. It should come out to:
# 
#   0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
# 
# Encrypt a bunch of stuff using your repeating-key XOR function. Get a
# feel for it.

from p03_decode_xor import string_xor
import sys

input_string = '''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal'''
key = 'ICE'

def repeating_key_xor_cipher(input_string, key):
    pad_length = len(input_string) % len(key)
    repeat_factor = len(input_string) / len(key)

    repeated_key = key * repeat_factor + key[:pad_length]

    return string_xor(input_string, repeated_key)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
    print repeating_key_xor_cipher(input_string, key).encode('hex')
