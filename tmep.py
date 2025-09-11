import redis


# Create a Redis client
client = redis.Redis.from_url(redis_url)

# Test the connection (PING should return True)
try:
    pong = client.ping()
    if pong:
        print("Connected to Redis successfully!")
except redis.ConnectionError as e:
    print("Connection failed:", e)

# Example set/get
client.set("foo", "bar")
print("foo:", client.get("foo").decode("utf-8"))
