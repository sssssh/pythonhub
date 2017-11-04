import hashlib


md5 = hashlib.md5()
md5.update('Python rocks!')
md5.update(b'Python rocks!')
md5.digest()
md5.hexdigest()


sha = hashlib.sha1(b'Hello Python').hexdigest()
