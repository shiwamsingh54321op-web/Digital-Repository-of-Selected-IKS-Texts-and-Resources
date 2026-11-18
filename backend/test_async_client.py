import asyncio
import httpx
from app.main import app


async def test_api():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as client:
        r = await client.get("/api/health")
        print("Health check response:", r.status_code, r.json())

        r2 = await client.get("/api/statistics")
        print("Statistics response:", r2.status_code, r2.json()["total_resources"], "resources")

        r3 = await client.get("/api/search?q=Ayurveda")
        print("Search response:", r3.status_code, "Found:", r3.json()["total"])


if __name__ == "__main__":
    asyncio.run(test_api())
