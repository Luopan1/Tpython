# coding = utf-8
import pickle

d = {"name": "Bob", "age": 28, "gender": "man"}
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.closed

f = open("dump.txt", "rb")
d = pickle.load(f)
f.closed
print(d)
