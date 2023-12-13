from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import binascii

keypair = RSA.generate(1024)

pubkey = keypair.publickey()
print("Public key is : ", pubkey.exportKey().decode('utf-8'))

prikey = keypair
print("Private key is " , prikey.exportKey().decode('utf-8'))


msg = input("Enter the msg to encrypt : ")

encryptor = PKCS1_OAEP.new(pubkey)
encrypt = encryptor.encrypt(msg.encode('utf-8'))
print("Encrypted message is : ", binascii.hexlify(encrypt))

decryptor = PKCS1_OAEP.new(prikey)
decrypt = decryptor.decrypt(encrypt)
print("Decrypted message is  :" , decrypt.decode('utf-8'))