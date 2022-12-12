
import pickle

f3=  open('pickled', 'wb')
    # Pickle the 'data' dictionary using the highest protocol available.
pickle.dump('python.py', f3)
f3.close()

# open a file, where you stored the pickled data
file1 = open('pickled', 'rb')

# dump information to that file
dataz = pickle.load(file1)
myfunction()
