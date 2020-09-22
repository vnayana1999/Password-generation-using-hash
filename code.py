import hashlib

def hashing_method(pwd_hash):
    hash_1 = hashlib.sha256(pwd_hash)
    print('Your hash password is: ', hash_1.hexdigest())

def main():
    print('Generation of a password using hash')
    pwd_hash = input('Enter your password: ').encode('utf-8')
    hashing_method(pwd_hash)

if __name__ == '__main__':
    main()

