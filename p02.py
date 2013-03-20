# 
# Write a function that takes two equal-length buffers and produces
# their XOR sum.
# 
# The string:
# 
#  1c0111001f010100061a024b53535009181c
# 
# ... after hex decoding, when xor'd against:
# 
#  686974207468652062756c6c277320657965
# 
# ... should produce:
# 
#  746865206b696420646f6e277420706c6179

def xor(x, y):
    return ''.join(["%x" %(int(a, 16) ^ int(b, 16)) for a,b in zip(x, y)])


xor_input =  ["1c0111001f010100061a024b53535009181c", 
              "686974207468652062756c6c277320657965"]

print xor(*xor_input)
