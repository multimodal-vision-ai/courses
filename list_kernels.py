from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# List kernels
try:
    kernels = list(api.kernels_list(user="gptan1975", page=1, page_size=50))
except:
    kernels = list(api.kernels_list(user="gptan1975"))

print(f"Found {len(kernels)} kernels:")
for k in kernels:
    priv = getattr(k, "is_private", "?")
    print(f"  https://www.kaggle.com/code/{k.ref}  (private={priv})")
