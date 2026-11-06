import joblib

ad = joblib.load("AD_seed111_k100.joblib")

print("Object type:", type(ad))
print("Object content:", ad)

if isinstance(ad, dict):
    print("\nKeys:")
    for key, value in ad.items():
        print(key, type(value))

if hasattr(ad, "__dict__"):
    print("\nAttributes:")
    for key, value in ad.__dict__.items():
        print(key, type(value))