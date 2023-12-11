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

# Misc Dev Reads
[Zero-Shot Learning in Modern NLP](https://joeddav.github.io/blog/2020/05/29/ZSL.html).  
[Building LLM-Powered Web Apps with Client-Side Technology](https://ollama.ai/blog/building-llm-powered-web-apps).  
[Transformers for Tabular Data Representation: A Survey of Models and Applications](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00544/115239/Transformers-for-Tabular-Data-Representation-A).  

# ML Datasets
[Penn Treebank](https://paperswithcode.com/dataset/penn-treebank)
