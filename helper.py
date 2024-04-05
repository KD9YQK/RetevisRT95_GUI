import pickle

def pickle_save(data, file):
  with open(file, 'wb') as f:  # open a text file
    pickle.dump(data, f) # serialize the list
    f.close()

def pickle_load(file):
  with open(file, 'rb') as f:
    retval = pickle.load(f) # deserialize using load()
    f.close()
  return retval
