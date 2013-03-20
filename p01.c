/*
 * Convert hex to base64 and back.
 *
 * The string:
 *
 *   49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
 *
 *   should produce:
 *
 *     SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
 */


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

char *hex_to_base64(char *input);
char *base64_to_hex(char *input);

char *base64_chars =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
char *hex_chars = "0123456789abcdef";

int main(int argc, char **argv)
{
    char *input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

    char *base64_encoded = hex_to_base64(input);
    printf("Base64 from hex: %s\n", base64_encoded);

    char *hex_encoded = base64_to_hex(base64_encoded);
    printf("Hex from base64: 0x%s\n", hex_encoded);

    if (strcmp(input, hex_encoded) != 0)
    {
        printf("Something went wrong, strings don't match\n");
        return 1;
    }

    return 0;
}

char *hex_to_base64(char *input)
{
    int input_len = strlen(input),
        i, j,
        output_len = 0;

    char *output = malloc((int) ceil(2.0/3 * input_len));

    /* 
     * A group of 3 characters in hex encoded string gives 2 characters of base64
     * base64 -> 6 bits, hex -> 4 bits
     */
    for (i = 0; i < input_len; i += 3)
    {
        unsigned char hex_group[3];
        strncpy(hex_group, input + i, 3);

        // Replace hex character with the corresponding hex digit
        for (j = 0; j < 3; ++j)
            hex_group[j] = strchr(hex_chars, hex_group[j]) - hex_chars;

        int base64_index[2];
        
        // Bit manipulation to convert 3 hex digits to 3 base64 digits
        base64_index[0] = (hex_group[0] << 2) | (hex_group[1] >> 2);
        base64_index[1] = ((hex_group[1] & 3) << 4) | (hex_group[2] >> 0);

        for (j = 0; j < 2; ++j)
            output[output_len++] = base64_chars[base64_index[j]];
    }

    output[output_len] = '\0';
    return output;
}

char *base64_to_hex(char *input)
{
    int input_len = strlen(input),
        i, j,
        output_len = 0;

    char *output = malloc((int) (ceil(3.0/2 * input_len)));

    /*
     * A group of 2 base64 characters gives 3 characters of hex
     */
    for (i = 0; i < input_len; i += 2)
    {
        unsigned char base64_group[3];
        strncpy(base64_group, input + i, 2);
        base64_group[2] = '\0';

        // Replace base64 character with corresponding base64 digit
        for (j = 0; j < 2; ++j)
            base64_group[j] = strchr(base64_chars, base64_group[j]) - base64_chars;

        int hex_index[3];
        
        // Bit manipulation to convert 2 base64 digits to 3 hex digits
        hex_index[0] = base64_group[0] >> 2;
        hex_index[1] = ((base64_group[0] & 3) << 2) |
                        (base64_group[1] >> 4) & 3;
        hex_index[2] = base64_group[1] & 15;
        
        for (j = 0; j < 3; ++j)
            output[output_len++] = hex_chars[hex_index[j]];

    }

    output[output_len] = '\0';
    return output;
}
