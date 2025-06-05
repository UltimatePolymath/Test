import asyncio
import asyncpg
import time
from urllib.parse import urlparse

DATABASE_URL = "postgresql://postgres:TermuxAuth01@db.ietmxcmutwkmlvsgquhm.supabase.co:5432/postgres"

async def measure_latency():
    result = urlparse(DATABASE_URL)
    conn = await asyncpg.connect(
        user=result.username,
        password=result.password,
        database=result.path.lstrip('/'),
        host=result.hostname,
        port=result.port,
        ssl='require'
    )

    print("🔌 Connected, testing latency for 10 seconds...")

    latencies = []
    start_time = time.time()

    while time.time() - start_time < 10:
        t0 = time.perf_counter()
        await conn.execute("SELECT 1")
        t1 = time.perf_counter()
        latency_ms = (t1 - t0) * 1000
        latencies.append(latency_ms)
        await asyncio.sleep(0.2)  # space out queries slightly

    await conn.close()

    avg_latency = sum(latencies) / len(latencies)
    print(f"\n✅ Average latency: {avg_latency:.2f} ms over {len(latencies)} queries.")

if __name__ == "__main__":
    asyncio.run(measure_latency())
