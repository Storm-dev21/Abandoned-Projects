import base64

message = input("message :>")
#encrypt
encode_message = message.encode("ascii")
base64_ =base64.b64encode(encode_message)
encrypt = base64_.decode("ascii")

print(encrypt)
message = encrypt
#Decrypt
decode_message = message.encode("ascii")
base64_ =base64.b64decode(decode_message)
decrypt = base64_.decode("ascii")

print(decrypt)