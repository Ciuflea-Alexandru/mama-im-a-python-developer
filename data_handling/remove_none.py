# Clean the users preferances in a dictionary that have the none value

def clean_preferences(user_pref):
    r = {}
    for n, x in user_pref.items():
        if user_pref[n] is not None:
            r[n] = x
    return r

user_pref = {"timezone": "GMT", "language": "English", "notifications": None, "currency": "USD", "theme": None}
print(clean_preferences(user_pref))