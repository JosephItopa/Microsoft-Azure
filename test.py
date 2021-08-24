# import the Redis client
import redis
import json
# Create a redis client
redisClient = redis.StrictRedis(host='10.160.198.187', port=6379, db=0)

# Retrieve the value for a specific key

patientdata = {"patientID": "SDDB_30", "fileID": "df23", "lead": "II", "fs":"250", "data": "[0.06375,-0.06625]", "time": "07/24/2020 09:00:00", "CA_Score": "0.96"}

# redisClient.hset(patientdata)

# print(redisClient.hget(patientdata))

redisClient.execute_command('JSON.SET', 'object', '.', json.dumps(patientdata))
reply = json.loads(redisClient.execute_command('JSON.GET', 'object'))
