import asyncio
import threading

from websockets.asyncio.server import serve

import main


async def ws():
    async with serve((), "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    print("Server started at ws://localhost:8765")
    threading.Thread(target=main.startBot, daemon=True).start()
    asyncio.run(ws())
