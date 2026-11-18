import asyncio
import httpx

async def minimal_app(scope, receive, send):
    if scope['type'] == 'http':
        await send({'type': 'http.response.start', 'status': 200, 'headers': [(b'content-type', b'text/plain')]})
        await send({'type': 'http.response.body', 'body': b'ok'})

async def main():
    print("Testing minimal ASGI app with httpx...")
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=minimal_app), base_url="http://test") as client:
        r = await client.get("/")
        print("Response:", r.status_code, r.text)

if __name__ == "__main__":
    asyncio.run(main())
