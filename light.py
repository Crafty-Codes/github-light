import requests
import json
import time

while True:
    req = requests.get(url = "https://api.github.com/repos/MarlinFirmware/Marlin/actions/workflows/test-builds.yml/runs")
    
    try:
        status = json.loads(req.content)["workflow_runs"][0]["status"]
    except:
        print("asdf")
        status = ""

    if "completed" == status:
        req = requests.get(url= "http://192.168.179.200/win&R=0&G=255&B=0")
    else:
        req = requests.get(url= "http://192.168.179.200/win&R=255&G=0&B=0")
    time.sleep(6000)
