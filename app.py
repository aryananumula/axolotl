import asyncio

from websockets.asyncio.server import serve


async def main():
    async with serve((), "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    print("Server started at ws://localhost:8765")
    asyncio.run(main())
