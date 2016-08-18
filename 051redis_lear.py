import time
from redis import Redis
from datetime import datetime
ONLINE_LAST_MINUTES = 5
redis = Redis()

def mark_online(user_id):
    now = int(time.time())
    expries = now + (5 * 60)+10
    all_user_key = 'online-user/%d' % (now // 60)
    user_key = 'user-activity/%s' % user_id
    p = redis.pipeline()
    p.sadd(all_user_key,user_id)
    p.set(user_key,now)
    p.expireat(all_user_key,expries)
    p.expireat(user_key,expries)
    p.execute()

def get_user_last_act(user_id):
    last_act = redis.get('user-activity/%s' % user_id)
    if last_act is None:
        return None
    return datetime.utcfromtimestamp(int(last_act))

def get_online_user():
    current = int(time.time()) // 60
    minutes = range(5)
    return redis.sunion(['online-user/%d'  % (current - x) for x in minutes])
