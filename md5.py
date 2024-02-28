import math

# Define T constants
"""In the MD5 algorithm, the T constant is a table of 64 32-bit unsigned 
integers derived from the sine function. These constants are 
used as part of the bitwise operations within each round of the algorithm."""
T = [int(2**32 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

# Initialize variables which are initial hash values for the hash function.

a0 = 0x67452301
b0 = 0xEFCDAB89
c0 = 0x98BADCFE
d0 = 0x10325476


def left_rotate(x, amount):
    """Left rotate a 32-bit integer"""
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF


def md5(message):
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    s = (
        [7, 12, 17, 22] * 4
        + [5, 9, 14, 20] * 4
        + [4, 11, 16, 23] * 4
        + [6, 10, 15, 21] * 4
    )

    K = [
        0xD76AA478,
        0xE8C7B756,
        0x242070DB,
        0xC1BDCEEE,
        0xF57C0FAF,
        0x4787C62A,
        0xA8304613,
        0xFD469501,
        0x698098D8,
        0x8B44F7AF,
        0xFFFF5BB1,
        0x895CD7BE,
        0x6B901122,
        0xFD987193,
        0xA679438E,
        0x49B40821,
        0xF61E2562,
        0xC040B340,
        0x265E5A51,
        0xE9B6C7AA,
        0xD62F105D,
        0x02441453,
        0xD8A1E681,
        0xE7D3FBC8,
        0x21E1CDE6,
        0xC33707D6,
        0xF4D50D87,
        0x455A14ED,
        0xA9E3E905,
        0xFCEFA3F8,
        0x676F02D9,
        0x8D2A4C8A,
        0xFFFA3942,
        0x8771F681,
        0x6D9D6122,
        0xFDE5380C,
        0xA4BEEA44,
        0x4BDECFA9,
        0xF6BB4B60,
        0xBEBFBC70,
        0x289B7EC6,
        0xEAA127FA,
        0xD4EF3085,
        0x04881D05,
        0xD9D4D039,
        0xE6DB99E5,
        0x1FA27CF8,
        0xC4AC5665,
        0xF4292244,
        0x432AFF97,
        0xAB9423A7,
        0xFC93A039,
        0x655B59C3,
        0x8F0CCC92,
        0xFFEFF47D,
        0x85845DD1,
        0x6FA87E4F,
        0xFE2CE6E0,
        0xA3014314,
        0x4E0811A1,
        0xF7537E82,
        0xBD3AF235,
        0x2AD7D2BB,
        0xEB86D391,
    ]

    # Pre-processing
    original_length = len(message)
    # Pad for 512 length
    message += b"\x80"
    while (len(message) * 8 % 512) != 448:
        # Add zeros til 512 bits
        message += b"\x00"
    message += original_length.to_bytes(8, byteorder="little")

    # Process the message in successive 512-bit chunks
    chunks = [message[i : i + 64] for i in range(0, len(message), 64)]
    for chunk in chunks:
        # Break chunk into sixteen 32-bit words
        M = [
            int.from_bytes(chunk[i : i + 1], byteorder="little")
            for i in range(0, 64, 4)
        ]

        # Initialize hash value this chunk
        A = a0
        B = b0
        C = c0
        D = d0

        # Main loop
        for i in range(64):
            # Round-specific processing depending on the round number
            if i < 16:
                F = (B & C) | ((-B) & D)
                g = i
            elif i < 32:
                F = (D & B) | ((~D) & C)
                g = (5 * i + 1) % 16
            elif i < 48:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | (-D))
                g = (7 * i) % 16
            # Store original value of D before it gets updated.
            d_temp = D
            D = C
            C = B
            B = (B + left_rotate((A + F + K[i] + M[g]), s[i])) & 0xFFFFFFFF
            A = (A + d_temp) & 0xFFFFFFFF

            # Update hash values
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    # Produce the final hash value
    hash_value = (
        a0.to_bytes(4, byteorder="little")
        + b0.to_bytes(4, byteorder="little")
        + c0.to_bytes(4, byteorder="little")
        + d0.to_bytes(4, byteorder="little")
    )
    return hash_value.hex()


# Example usage
message = b"Hello, world!"
hashed_message = md5(message)
print("MD5 hash:", hashed_message)
