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

from p03 import get_char_frequency_from_file, get_char_frequency_from_string, decode_xor_cipher

reference_map = get_char_frequency_from_file('book.txt')

max_score = 0
max_score_string = None

for hex_encoded_string in open('3132713/gistfile1.txt').readlines():
    encoded_string = hex_encoded_string.strip().decode('hex')
    decoded_string, score, key = decode_xor_cipher(reference_map, encoded_string)
    
    if score > max_score:
        max_score_string = decoded_string
        max_score = score

if max_score != 0:
    print max_score_string
else:
    print "Failed to decode string"
