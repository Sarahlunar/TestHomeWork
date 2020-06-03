import json

import yaml


def steps(path="../datas/steps/search.yaml" , fun_name="search" , stock_code="BABA"):
    with open(path, encoding="utf-8") as f:
        steps = yaml.safe_load(f)[fun_name]

    s = json.dumps(steps)
    if "${"+stock_code+"}" in s:
        print("yes")
    else:
        print("no")
    steps = s.replace("${stock_code}", stock_code)
    print(s)
    print(steps)

steps()
