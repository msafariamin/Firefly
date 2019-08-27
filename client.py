import firefly

client = firefly.Client("http://127.0.0.1:8000/") 
r = client.square(n=4)
print(r)


