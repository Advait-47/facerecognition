
import requests


def sendFaceInfo(name, facemap):
    url = 'http://10.2.15.215:5000/studentAttendance/lockAttendance'

    params = {
        "facemap": facemap,

        "name": name
    }

    res = requests.post(url, json=params)
    print(res)
