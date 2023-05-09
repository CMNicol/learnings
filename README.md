# learnings


# Start a Redis Host which you can connect to with the `redis` Python package.
```shell
docker run --name my-redis -p 6379:6379 -d redis
```
```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set("hello","world")
r.get("hello")
```
