import asyncio
import aiohttp
import time
import json

response_order = None
resources = None
with open("./resources.json", 'r') as openfile:
    resources = json.load(openfile)


async def fetch(session, resource):
    global response_order
    url = resource["url"]
    async with session.get(url) as response:
        t = await response.text()
        result = {
            "resource": resource["resource"],
            "data": t
        }
        response_order += [resource["resource"]]
    return result


async def main():
    global response_order
    async with aiohttp.ClientSession() as session:
        response_order = []
        s_time = time.time()
        print("Order of Request: ", [res["resource"] for res in resources])
        tasks = [asyncio.ensure_future(fetch(session, res)) for res in resources]
        responses = await asyncio.gather(*tasks)
        full_result = {}
        for response in responses:
            full_result[response["resource"]] = response["data"]
        print("Response Order: ", response_order)
        print("Time used: ", time.time() - s_time)


for i in range(2):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
