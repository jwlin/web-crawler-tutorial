# coding=utf-8
import requests
import json
from requests.adapters import HTTPAdapter


def request_url(url, timeout=3, max_retries=3):
    s = requests.Session()
    s.mount(url, HTTPAdapter(max_retries=max_retries))
    try:
        response = s.get(url, timeout=timeout)
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    return response


def load_json(path):
    jsonFile = open(path)
    data = json.load(jsonFile)
    jsonFile.close()

    return data


def write_json(data,path):
    with open(path, "w") as outfile:
        json.dump(data, outfile, indent=4)