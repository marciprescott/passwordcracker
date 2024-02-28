import hashlib
from hashlib import md5


string_to_hash = "Luna1234567"

result = hashlib.md5(string_to_hash.encode())

print("The hexadecimal equivalent of hash is: ", end="")
print(result.hexdigest())
print(md5(b"password").hexdigest())
