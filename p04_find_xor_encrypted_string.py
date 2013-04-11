#################################
#################################
# https://gist.github.com/3132713.git
#################################
#################################

# 4. Detect single-character XOR
# 
# One of the 60-character strings at:
# 
#   https://gist.github.com/3132713
# 
# has been encrypted by single-character XOR. Find it. (Your code from
# #3 should help.)

from p03_decode_xor import get_char_frequency_from_file, get_char_frequency_from_string, decode_xor_cipher

reference_map = get_char_frequency_from_file('book.txt')

min_score = 1000
min_score_string = None

for hex_encoded_string in open('3132713/gistfile1.txt').readlines():
    encoded_string = hex_encoded_string.strip().decode('hex')
    decoded_string, score, key = decode_xor_cipher(reference_map, encoded_string)

    if score < min_score:
        min_score_string = decoded_string
        min_score = score

print min_score_string
