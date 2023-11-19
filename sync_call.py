import requests
import time
import json


resources = [
    {
        "resource": "Columbia",
        "url": "https://www.columbia.edu/"
    },
    {
        "resource": "Twitter",
        "url": 'http://www.twitter.com'
    },
    {
        "resource": "ExternalAPI",
        "url": 'http://ec2-3-27-170-134.ap-southeast-2.compute.amazonaws.com:8012/price/MSFT'
    },
    {
        "resource": "Google",
        "url": 'http://www.google.com'
    }
]

# stock_list = ['MSFT', 'GOOG', 'META']
# resources = [
#     {
#         "resource": stk,
#         "url": "http://ec2-3-27-170-134.ap-southeast-2.compute.amazonaws.com:8012/price/" + stk
#     } for stk in stock_list
# ]

response_order = None


def fetch(session, resource):
    global response_order
    url = resource["url"]
    # print("Calling URL = ", url)
    with session.get(url) as response:
        # t = response.text()
        t = response.text
        # print("URL ", url, "returned")
        result = {
            "resource": resource["resource"],
            "data": t
        }
        response_order += [resource["resource"]]
    return result


def main():
    global response_order
    with requests.session() as session:
        s_time = time.time()
        print("Request Order: ", [res["resource"] for res in resources])
        response_order = []
        responses = [fetch(session, res) for res in resources]
        full_result = {}
        for response in responses:
            full_result[response["resource"]] = response["data"]
        print("Response Order: ", response_order)
        print("Time used: ", time.time() - s_time)


for i in range(10):
    main()
