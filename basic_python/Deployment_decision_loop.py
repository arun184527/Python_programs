models = [
    {"accuracy": 0.93, "latency": 180},
    {"accuracy": 0.88, "latency": 220},
    {"accuracy": 0.85, "latency": 350}
]

i = 0
while i < len(models):
    acc = models[i]["accuracy"]
    lat = models[i]["latency"]

    if acc > 0.9 and lat < 200:
        print("Deploy to production")
    elif acc > 0.85:
        print("Deploy with optimization")
    else:
        print("Do not deploy")

    i += 1