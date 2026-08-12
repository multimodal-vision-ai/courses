from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

ids = [
    "gptan1975/fmi-demo1-traffic-classification",
    "gptan1975/fmi-demo2-qoe-optimization",
    "gptan1975/fmi-demo3-quality-assessment",
    "gptan1975/fmi-demo4-neural-compression",
    "gptan1975/fmi-demo5-semantic-communication",
]

for kid in ids:
    try:
        # Try to get kernel info
        kernel = api.kernel_info(kid)
        print(f"Title: {kernel.get('title', '?')}")
        print(f"  URL: {kernel.get('url', '?')}")
        print(f"  Ref: {kernel.get('ref', '?')}")
        print(f"  ID: {kernel.get('id', '?')}")
        print()
    except Exception as e:
        print(f"FAIL {kid}: {e}")
