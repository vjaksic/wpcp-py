#!/usr/bin/env python

import asyncio
import websockets
import cbor

async def connection_handler(websocket, path):
    message_cbor = await websocket.recv()
    print("message_cbor < {}".format(message_cbor))

    message_json = cbor.loads(message_cbor)
    print("message_json  < {}!".format(message_json))

    response = [0, 0, { "methods": ["browse"] }]
    await websocket.send(cbor.dumps(response))


start_server = websockets.serve(connection_handler, 'localhost', 31337, extra_headers= {"Sec-WebSocket-Protocol": "wpcp"})

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
