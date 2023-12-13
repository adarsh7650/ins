from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

key = RSA.generate(1024)

pubkey = key.publickey().exportKey()
prikey = key.exportKey()

og_doc =b'original'
md_doc = b'originaa'

og_hash = SHA256.new(og_doc)
md_hash = SHA256.new(md_doc)

signature = pkcs1_15.new(RSA.import_key(prikey)).sign(og_hash)

try :
    pkcs1_15.new(RSA.import_key(pubkey)).verify(md_hash , signature)
    print("V")
except:
    print("IN")