import base64
import argparse
import binascii

### Hackthebox: Bizness
### Format Hash to crackable format

def formathash(hash,salt):
    enc = hash
    enc = enc.replace('_','/')
    enc = enc.replace('-',"+")
    enc += '='
    dec = base64.b64decode(enc.encode('utf-8'))
    formathash = binascii.hexlify(dec).decode('utf-8')
    formathash += ':' + salt
    print(formathash)

    hashfile = open("ofbizhash","w")
    hashfile.write(formathash)
    hashfile.close()
    
    print("Written to file -> ofbizhash")

def main():
    parsecmdargs = argparse.ArgumentParser(description="Format hash (bizness htb)")
    parsecmdargs.add_argument("-hash", type=str, required=True ,help="Hash")
    parsecmdargs.add_argument("-salt", type=str, required=True ,help="salt")

    try:
        cmdargs = parsecmdargs.parse_args()
    except argparse.ArgumentError as e:
        sys.exit(-4)
    except ValueError as e:
        sys.exit(-4)

    formathash(cmdargs.hash,cmdargs.salt)

if __name__ == "__main__":
    main()
