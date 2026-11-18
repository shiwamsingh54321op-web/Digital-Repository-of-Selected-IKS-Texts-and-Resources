import time
print("Importing app...")
t0 = time.time()
from app.main import app
print(f"App imported in {time.time() - t0:.2f}s")

print("Importing TestClient...")
t1 = time.time()
from fastapi.testclient import TestClient
print(f"TestClient imported in {time.time() - t1:.2f}s")

print("Instantiating TestClient...")
t2 = time.time()
client = TestClient(app)
print(f"TestClient instantiated in {time.time() - t2:.2f}s")

print("Calling /api/health...")
t3 = time.time()
resp = client.get("/api/health")
print(f"/api/health returned {resp.status_code} in {time.time() - t3:.2f}s: {resp.json()}")
