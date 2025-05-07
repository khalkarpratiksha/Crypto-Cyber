import hashlib 

data="pratiksha"

resultSHA=hashlib.sha256(data.encode())
print("Results for SHA",resultSHA)
print(resultSHA.hexdigest())
