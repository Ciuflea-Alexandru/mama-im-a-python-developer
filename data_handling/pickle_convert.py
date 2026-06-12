# create a dictionary save it to a binary file and then reads it back into a new variable

import pickle

# 1. The data we want to save
data_to_store = {
    "username": "coder_123",
    "level": 5,
    "inventory": ["sword", "shield", "potion"],
    "is_active": True
}

filename = "savegame.pkl"

# 2. Serialize (Save) the data
# We open the file in 'wb' (write binary) mode
with open(filename, 'wb') as file:
    pickle.dump(data_to_store, file)
    print(f"Data successfully saved to {filename}")

# 3. Deserialize (Load) the data
# We open the file in 'rb' (read binary) mode
with open(filename, 'rb') as file:
    loaded_data = pickle.load(file)
    print("Data successfully loaded!")

# 4. Verify the data
print(f"Loaded Username: {loaded_data['username']}")
print(f"Full Data: {loaded_data}")