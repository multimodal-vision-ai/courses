from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

kid = "guopingtan/fmi-demo1-traffic-classification"
print(f"Deleting {kid}...")
try:
    api.kernels_delete(kid)
    print("Deleted OK")
except Exception as e:
    print(f"Delete error: {type(e).__name__}: {e}")
