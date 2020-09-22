# Password-generation-using-hash
This project mainly demonstrates the generation of a hashed password from a given input
The input is hashed by the SHA-256 algorithm which is one of the Secured Hashing Algorithms
Later the hashed password is encoded into binary which would or else return an error
The output is a hashed password which is highly encrypted and secured

#WORKING OF THE CODE
The code mainly takes the user input which is a password and hashes it.
Firstly we import the hashlib library. Here we have two functions-
hashing_method() and main() method. The hashlib library contains many hashing
algorithms like sha512, md5, sha256 etc.

In hashing_method() function we declare a variable hash_1 which is the final hashed
password. We convert it into hexadecimal form by using hexdigest(). If we do not
use hexdigest, it returns it as an object which is not very useful.

In the main() method first we have the print statement which tells the user what
exactly the script is about. Next we declare a variable pwd_hash which is the input
by the user. The sha256 algorithm is implemented on this input. Next we call the
hashing_method() function and pass the user;s input pwd_hash into it.hence the
password is hashed.
