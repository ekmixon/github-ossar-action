import hashlib
print("I am very insecure. Bandit thinks so too.")
#B110
xs=[1,2,3,4,5,6,7,8]
try:
    print(xs[7])
    print(xs[8])
except: pass

ys=[1, 2, None, None]
for y in ys:
    try:
        print(y+3)
    except: continue #not how to handle them

#some imports
import telnetlib
import ftplib

#B303 and B324
s = b"I am a string"
print(f"MD5: {hashlib.md5(s).hexdigest()}")
print(f"SHA1: {hashlib.sha1(s).hexdigest()}")
print(f"SHA256: {hashlib.sha256(s).hexdigest()}")
