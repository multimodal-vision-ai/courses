from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

kids = [
    "guopingtan/fmi-demo1-traffic-classification",
    "guopingtan/fmi-demo2-qoe-optimization",
    "guopingtan/fmi-demo3-quality-assessment",
    "guopingtan/fmi-demo4-neural-compression",
    "guopingtan/fmi-demo5-semantic-communication",
]

for kid in kids:
    try:
        result = api.kernels_initialize(kid)
        print(f"Started: {kid}")
    except Exception as e:
        err = str(e)[:100]
        print(f"Init: {kid} - {err}")
