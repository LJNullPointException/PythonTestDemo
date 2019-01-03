import sha3
import binascii
import json
from ecdsa import SigningKey, SECP256k1

private=''
paddress=''

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)


def getAddress():
  global private
  global paddress
  s = os.urandom(4096)
  s = s[0:32]
  private = toHex(s)
  keccak = sha3.keccak_256()
  prv = binascii.unhexlify(private)
  keccak.update(SigningKey.from_string(prv,curve=SECP256k1).get_verifying_key().to_string())
  paddress = "0x{0}".format(keccak.hexdigest()[24:])
  return paddress