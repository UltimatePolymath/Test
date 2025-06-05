import asyncio
import asyncpg
import ssl

USER = "postgres.ietmxcmutwkmlvsgquhm"
PASSWORD = "TermuxAuth01"  # replace with your real password
HOST = "aws-0-ap-south-1.pooler.supabase.com"
PORT = 5432
DBNAME = "postgres"

async def connect():
    try:
        # Create an SSL context that ignores cert verification
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        conn = await asyncpg.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            database=DBNAME,
            ssl=ssl_context
        )

        print("✅ Connected successfully!")

        result = await conn.fetchrow("SELECT NOW();")
        print("🕒 Current Time:", result["now"])

        await conn.close()
        print("🔌 Connection closed.")

    except Exception as e:
        print(f"❌ Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(connect())
