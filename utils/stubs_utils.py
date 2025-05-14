import os
import pickle

# Stub: a saved state or snapshot of an object -> to avoid recomputation

# Saves an object(model or dictionary) into a file using pickel serialization
def save_stub(stub_path, object): # stub_path: models/yolo_stub.pkl
    if not os.path.exists(os.path.dirname(stub_path)):
        os.mkdir(os.path.dirname(stub_path))

    if stub_path is not None:
        with open(stub_path, "wb") as f:
            pickle.dump(object, f)

# Reads the object back from that file only if certain conditions are met
def read_stub(read_from_stub, stub_path):
    if (read_from_stub is True) and (stub_path is not None) and (os.path.exists(stub_path) is True):
        with open(stub_path, "rb") as f:
            object = pickle.load(f)
            return object
    return None

