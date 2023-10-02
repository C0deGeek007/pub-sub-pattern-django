import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_connection = redis.Redis(connection_pool=pool)
# value = redis.get('mykey')
# print("redis")
# print(value)