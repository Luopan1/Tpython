import redis


def main():
    try:
        r = redis.StrictRedis(host="104.224.166.169", port=6379)
        r.set("name", "郭靖")
        print(r.get("name").decode("utf-8"))
        print(r)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
