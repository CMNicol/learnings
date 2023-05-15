# Learnings

## Table of Contents. 
[Create a Redis Host with Docker](#redis-host-and-python-redis-package)
[SaaS Reading](#SaaS-Reading)

# Redis Host and Python `redis` package.
```shell
docker run --name my-redis -p 6379:6379 -d redis
```
```python
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set("hello","world")
r.get("hello")
```

# SaaS Reading
[Security practices in AWS multi-tenant SaaS environments](https://aws.amazon.com/blogs/security/security-practices-in-aws-multi-tenant-saas-environments/)