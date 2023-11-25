from fastapi import FastAPI, Response
import uvicorn
import time
import util
import async_call
import sync_call
import json

app = FastAPI()
util.init()


@app.get("/")
async def root():
    return {
        "Format for synchronous calls": "/sync/{num_loop}",
        "Format for asynchronous calls": "/async/{num_loop}",
    }


@app.get("/sync/{num_loop}")
async def loop_sync_call(num_loop: int):
    results = []
    for i in range(num_loop):
        s_time = time.time()
        print("=== Request Order:", [res["resource"] for res in util.resources], "===")
        util.response_order = []
        result = sync_call.sync_request(util.resources)
        results += [{'Sync Loop ' + str(i): result}]
        print("Result: ", result)
        print("=== Response Order:", util.response_order, "===")
        print("Time used: ", time.time() - s_time)
        print()
    return results


@app.get("/async/{num_loop}")
async def loop_async_call(num_loop: int):
    results = []
    for i in range(num_loop):
        s_time = time.time()
        print("=== Request Order:", [res["resource"] for res in util.resources], "===")
        util.response_order = []
        result = async_call.async_request(util.resources)
        results += [{'Async Loop ' + str(i): result}]
        print("Result: ", result)
        print("=== Response Order:", util.response_order, "===")
        print("Time used: ", time.time() - s_time)
        print()
    return results


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
